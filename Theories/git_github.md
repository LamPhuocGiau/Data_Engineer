# Git and Github
## Git
- [Setup](#Setup)
- [Create project at local and remote](#Create-project-at-local-and-remote)
- [Https and ssh](#Https-and-ssh)

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
git config --global user.name “Giau_Lam”
git config --global user.email “lamphuocgiau86@gmail.com”
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
Git remote add origin <https://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@github.com/LamPhuocGiau/Python.git>
git push -u origin main
```
Note: Token is **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**

### Https and ssh

- Create a ssh key: open terminal and paste below command.

```
ssh-keygen -t ed25519 -C "lamphuocgiau86@gmail.com"
```

- copy ssh key on **.SSH folder** (Ubuntu: go to home , Ctr H to show hiden files).

- github >> setting >> SSH and GPG keys. paste the SSH key











