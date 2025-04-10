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

### run server

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