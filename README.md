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

gleoba@DESKTOP-7RNTTE1:~/workspace/docs$ diff -q -r gleoba-pile gleoba.github.io -x public -x resources

#### OK:
Only in gleoba.github.io: .git
Only in gleoba.github.io: .github
Only in gleoba.github.io: .gitignore
Only in gleoba.github.io: LICENSE
Only in gleoba.github.io: README.md
Only in gleoba.github.io: playground
Only in gleoba-pile: .hugo_build.lock
Files gleoba-pile/hugo.toml and gleoba.github.io/hugo.toml

#### TO-DO:
diff gleoba-pile/content/client-work/a1bulgaria.md gleoba.github.io/content/client-work/a1bulgaria.md
diff gleoba-pile/content/client-work/att.md gleoba.github.io/content/client-work/att.md
diff gleoba-pile/content/client-work/belgacom.md gleoba.github.io/content/client-work/belgacom.md
diff gleoba-pile/content/experience/_index.md gleoba.github.io/content/experience/_index.md


