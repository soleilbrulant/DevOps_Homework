# Git Homework

## Task 1: git commit -a -m
```bash
$ echo "new update" >> file.txt
$ git status
Changes not staged for commit:
  modified:   file.txt
  
$ git commit -a -m "Update file"
[main 7b1c3a2] Update file
 1 file changed, 1 insertion(+)
```
Difference: `-a` automatically stages tracked files before committing, saving the `git add` step.

## Task 2: Git Cherry-Pick
```bash
$ git log --oneline
a1b2c3d (HEAD -> feature) Add feature 3
e4f5g6h Add feature 2
i7j8k9l Add feature 1
z9y8x7w (main) Initial commit

$ git checkout main
Switched to branch 'main'

$ git cherry-pick e4f5g6h
[main e4f5g6h] Add feature 2
 1 file changed, 1 insertion(+)
```
The commit from the feature branch was successfully applied to main.