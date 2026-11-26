"""Stage the stable calculator, preview, and stable archives from GitHub Releases."""
import json
from pathlib import Path
import re
import subprocess
import sys

output = Path("public/playground")
version_pattern = re.compile(r"currency-v(\d+)\.(\d+)\.(\d+)(?:-(alpha|beta|rc)\.(\d+))?")
stage_order = {"alpha": 0, "beta": 1, "rc": 2, None: 3}

# gh api --paginate --slurp returns one list per API page.
releases = {}
for page in json.load(sys.stdin):
    for release in page:
        tag = release["tag_name"]
        if release["draft"] or not tag.startswith("currency-v"):
            continue
        match = version_pattern.fullmatch(tag)
        if not match or bool(match[4]) != release["prerelease"]:
            sys.exit(f"Currency tag and GitHub pre-release status must agree: {tag}")
        major, minor, patch = map(int, match.groups()[:3])
        version = (major, minor, patch, stage_order[match[4]], int(match[5] or 0))
        source = "currency.html" if major == 1 else f"currency-v{major}.html"
        releases[version] = (tag, f"refs/tags/{tag}:playground/{source}")

stable_versions = [version for version in releases if version[3] == stage_order[None]]
if not stable_versions:
    sys.exit("A published stable currency release is required to build the site.")


def publish(version, destination):
    tag, source = releases[version]
    html = subprocess.check_output(["git", "show", source])
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(html)
    print(f"{destination} <- {tag}")


publish(max(stable_versions), output / "currency.html")
publish(max(releases), output / "preview/currency.html")
for version in stable_versions:
    tag, _ = releases[version]
    publish(version, output / "versions" / f"{tag}.html")
