# Git Homework

## Task 1: git commit -a -m
`git commit -a -m` stages tracked files and commits them in one go. `git commit -m` only commits what's already staged.
Tested and observed the difference when modifying existing files.

## Task 2: Git Cherry-Pick
Created a new branch `feature-1`. Made 3 commits.
Used `git log` to find the commit hash of the second commit.
Switched back to `main` branch.
Ran `git cherry-pick <commit-hash>`.
The specific change was successfully brought into `main`.