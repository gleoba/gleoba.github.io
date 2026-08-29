Great question! Based on GitHub's documentation and industry best practices, here's a comprehensive guide:

## Best Practices for Git Commit Messages

### The Standard Format: Conventional Commits

The most widely adopted standard is **Conventional Commits**, which enables automatic changelog generation:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Quick Reference: Commit Prefix Guide

| Prefix | Use Case | Example |
|--------|----------|---------|
| `feat:` | New feature | `feat(auth): add 2FA support` |
| `fix:` | Bug fix | `fix(api): handle null responses` |
| `docs:` | Documentation | `docs(readme): update setup instructions` |
| `style:` | Code style changes (formatting, missing semicolons, etc.) | `style: fix linting errors` |
| `refactor:` | Code refactoring without feature changes | `refactor(utils): simplify math functions` |
| `perf:` | Performance improvements | `perf(cache): optimize query performance` |
| `test:` | Adding or updating tests | `test(auth): add login validation tests` |
| `chore:` | Maintenance tasks, dependencies, builds | `chore(deps): update npm packages` |

### Commit Message Structure

**Type** (required) — describes the kind of change:

**Scope** (optional) — area of the codebase affected:
```
feat(auth): add OAuth2 support
fix(database): resolve connection pool leak
docs(readme): update installation steps
```

**Subject** (required) — brief description:
- Imperative mood ("add" not "added" or "adds")
- No period at the end
- Max 50 characters
- Lowercase

**Body** (optional) — detailed explanation:
- Wrap at 72 characters
- Explain *what* and *why*, not *how*
- Reference issues: `Closes #123` or `Fixes #456`

**Footer** (optional) — metadata:
```
Closes #123
Reviewed-by: @username
Breaking-Change: description of breaking change
```

### Examples

**Feature with scope:**
```
feat(playground): add running splits calculator

Add a new HTML tool for calculating pace and split times.
Includes form validation and real-time calculations.

Closes #42
```

**Bug fix:**
```
fix(deploy): resolve artifact upload failure

The deploy-pages action requires the artifact to be named 
'github-pages'. Removed custom naming to use default.

Fixes #99
```

**Breaking change:**
```
feat!: redesign API authentication

Breaking-Change: API v1 authentication endpoint removed. 
Use OAuth2 authentication with new /auth/oauth endpoint.

Closes #215
```

## Auto-Generate Changelog Tools

### Option 1: GitHub's Built-in Release Notes (Recommended)

GitHub can [automatically generate release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes) from PR labels and conventional commits.

When creating a release, click **"Generate release notes"** — GitHub automatically groups PRs by labels and generates a formatted changelog.
