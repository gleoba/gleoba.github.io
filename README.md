# gleoba.github.io

* to view, go to [https://gleoba.github.io]: https://gleoba.github.io
* for playground index go to [https://gleoba.github.io/playground]: https://gleoba.github.io/playground

## SETUP DEV

```bash
git clone git@github.com:gleoba/gleoba.github.io.git

cd gleoba.github.io/
```

## upgrade with the latest version

> hugo mod get -u github.com/zetxek/adritian-free-hugo-theme

* an example response that also updates go.mod and go.sum files:
> go: downloading github.com/zetxek/adritian-free-hugo-theme v1.10.3
> go: upgraded github.com/zetxek/adritian-free-hugo-theme v1.10.2 => v1.10.3


## upgraade / rebuild sequence

* full instructions at the [adritian-free-hugo-theme]: https://github.com/zetxek/adritian-free-hugo-theme
 
> hugo mod get -u github.com/zetxek/adritian-free-hugo-theme
> hugo mod npm pack
> hugo mod tidy
> hugo mod get -u ./...
> npm install
> npm audit fix
> npm fund



## Local development

### Re / Build

* with a clean, modern command
> hugo --gc --minify --baseURL https://gleoba.github.io/

* If you want stricter publish cleanup in CI, add: --cleanDestinationDir
* This is optional and is documented as removing stale files from the publish directory; it is not required for every build.
> hugo --gc --minify --cleanDestinationDir --baseURL https://gleoba.github.io/

### run a server

* run locally
 ![tip]: running should be from a standalone terminal since VSCode internal terminal causes CORS error with "No 'Access-Control-Allow-Origin' header" 

> hugo server --disableFastRender
or
> hugo server

* open local [site]: http://localhost:1313/

### GIT standards
[instructions for change log documentation]: .github/workflows/release_notes_readme.md

### deploy and run action in GitHub
* it's possible to run it manualy via [workflows-at-github.com]: https://github.com/gleoba/gleoba.github.io/actions/workflows/hugo.yaml

>  0. if needed, login in cli and follow the instructions for ssh connection.
gh auth login -h github.com

>  1. check first the latest commit 
gh browse --commit --no-browser
gh search commits --committer=$USER --sort=committer-date --limit=3

> 2. worflow run
gh workflow run WORKFLOW_FILE_NAME.yml -r BRANCH_NAME
e.g.
gh workflow run hugo.yaml

> 3. check status of the worflow run
gh run list --workflow=hugo.yaml

> 4. [optional] cleanup
git status --ignored --short | grep '^!!' | awk '{print substr($0, 4)}' | xargs rm -r

> 5. to run locally afain after the cleanup, need to 'npm install' 
npm install
npm fund