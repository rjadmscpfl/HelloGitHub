# HelloGitHub
Let's start GitHub

## register account and email
* _git init_
* git config --global user.name "rjadmscpfl"
* git config --global user.email "rjadmscpfl@icloud.com"

## git stage
* git add --all

## git master
* git commit -am "First commit"

## verify stage
* git status
* git log (--graph --oneline)

## Revoke 
* git log --graph --oneline
* git reset cb5d6a (--hard | soft)
* git revert cb5d6a

* ex)
* git reset --hard cb5d6a
* git add --all
* git commit -am "reset cb5d6a"
* git push -u origin master master

## push to github
* git remote add origin https://github.com/rjadmscpfl/HelloPython.git
* git push -u origin master 

* git add --all
* git commit -m "Remote commit"
* git push 

## .gitignore
*  _.gitignore_ <- add file name which you don't want to update 

## clone code
* git clone https://github.com/rjadmscpfl/HelloGitHub.git

## fetch
* git fetch
* git status

## pull to local Repo
* git pull origin master

* git add --all
* git commit -m "Remote commit"

* ex)
* git pull
* git push origin master
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

* git diff (myidea)
* git checkout -p (myidea)   
* git checkout -b (myidea) origin/myidea
* git push -d origin (myidea)

## merge branch
* git checkout master
* git merge (myidea)

## rebase
* git rebase (myidea)

## check github
* git status 
* git remote

