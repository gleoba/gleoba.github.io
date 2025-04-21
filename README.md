# gleoba.github.io
## to view, go to https://gleoba.github.io

## SETUP DEV

```bash
git clone git@github.com:gleoba/gleoba.github.io.git

cd gleoba.github.io/

git status
git remote -v
git branch -v

git commit -a -m 'Update setup instructions in README.md [issue 1]'
```

diff -q -r gleoba-pile gleoba.github.io -x public -x resources


## install and run
npm install
npm fund

## upgrade with the latest version
hugo mod get -u github.com/zetxek/adritian-free-hugo-theme
# example response that also updates go.mod and go.sum files:
# @> go: upgraded github.com/zetxek/adritian-free-hugo-theme v1.7.6 => v1.7.11

### run server
# tip: running should be from a standalone terminal since VSCode internal terminal causes CORS error with "No 'Access-Control-Allow-Origin' header"

hugo server --disableFastRender
or
hugo server

### open local site

http://localhost:1313/

### run the deployment action in GitHub

https://github.com/gleoba/gleoba.github.io/actions/workflows/hugo.yaml

gh workflow run WORKFLOW_FILE_NAME.yml -r BRANCH_NAME
e.g.
gh workflow run hugo.yaml

# cleanup
git status --ignored --short | grep '^!!' | awk '{print substr($0, 4)}' | xargs rm -r

# need to 'npm install' after the cleanup
