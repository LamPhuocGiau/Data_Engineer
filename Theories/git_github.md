# Git and Github
## Git
- [Setup](#Setup)
- [Create project at local and remote](#Create-project-at-local-and-remote)
- [Https and ssh](#Https-and-ssh)
- [Common commands](#Common-commands)

- [Source](https://www.youtube.com/watch?v=pC1s6JOwglE&list=PLncHg6Kn2JT6nWS9MRjSnt6Z-9Rj0pAlo&index=3)

### Setup

- Install git.

- Check git.

```
git version
```

- Create github account.

- Connect git and git hub.

```
git config --global user.name “ ...abcdexyz...”
git config --global user.email “l.....@gmail.com”
```
- Check git.

```
git config --list
```
### Create project at local and remote

**Download an existing project from remote to local**.

```
git clone <https or ssh path>
```
**Create a project at github, clone to local, code and push to remote**.

- Create a repository on github.

- Clone to local.

- creat files on local.

- push to remote.

```
git status
git add .
git commit -m 'init project'
git push origin main
```
**We have a local project, we want to push to remote**.

- Create a new repository.

```
git init
git status
git add .
git commit -m 'update'
Git remote add origin <https://abcdexyz@github.com/........git>
git push -u origin main
```
Note: Token is **abcdexyz**

### Https and ssh

- Create a ssh key: open terminal and paste below command.

```
ssh-keygen -t ed25519 -C "......6@gmail.com"
```

- copy ssh key on **.SSH folder** (Ubuntu: go to home , Ctr H to show hiden files).

- github >> setting >> SSH and GPG keys. paste the SSH key.

### Common commands

**Individual work**.

git init.

git clone.

git status.

git add.

git commit.

git push.

**Team work**.

git pull origin main: Pull the latest codes from remote to local.

git checkout -b <new_branch_name> : Create a new branch. And switch to new branch name

git branch: check how many existing branch have?

Merge new_branch_name to main_branch.

```
git checkout main: Switch to main branch.
git merge new_branch_name
git branch -d new_branch_name
```
Merge conflict: open file at local by editor. Delete and keep the contents which we want to keep. And executive git add, commit and push again.

**Conflict solving**.

git log.

Open on visual code to delete and keep correct codes and add, commit, push again.










