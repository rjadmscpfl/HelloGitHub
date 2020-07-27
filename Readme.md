# HelloGitHub
Let's start GitHub

## register account and email
* _git init_
* git config --global user.name "rjadmscpfl"
* git config --global user.email "rjadmscpfl@icloud.com"

## to stage
* git add --all

## to master
* git commit -m "First commit"

## verify stage
* git status
* git log (--graph --oneline)

## Revoke 
* git log
* git reset cb5d6a (--hard)
* git revert cb5d6a

## push to github
* git remote add origin https://github.com/rjadmscpfl/HelloPython.git
* git push -u origin master 

* git add --all
* git commit -m "Remote commit"
* git push -u origin master

## .gitignore
*  _.gitignore_ <- add file name which you don't want to update 

## clone code
* git clone https://github.com/rjadmscpfl/HelloGitHub.git

## fetch
* git fetch
* git status

## pull to local Repo
* git pull origin master
----------------------------------------------------

## branch 
* git branch (myidea)
* git checkout (myidea) -> git checkout -b (myidea)
* git add --all
* git commit -m "Second commit"
* git branch -d (myidea)
* _git checkout master_

## remote branch
* git branch -a
* git push origin (myidea)
* (git fetch)
* git checkout -b (myidea) origin/myidea
* git push -d origin (myidea)

## merge
* git checkout master
* git merge (myidea)

## rebase
* git rebase (myidea)

## check github
* git status
* git remote

