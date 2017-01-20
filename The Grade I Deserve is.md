The grade I desrve is markdown file. This file contains a ot of repeated commands
I used git push and git pull several times and the results were not always different

manager@bl8vbox:~/Repository1$ nano Extra
manager@bl8vbox:~/Repository1$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	Extra

nothing added to commit but untracked files present (use "git add" to track)
manager@bl8vbox:~/Repository1$ git add Extra
manager@bl8vbox:~/Repository1$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   Extra

manager@bl8vbox:~/Repository1$ git commit -m 'MESSAGE'
[master 41f626c] MESSAGE
 Committer: System Manager <manager@bl8vbox.unassigned-domain>
Your name and e-mail address were configured automatically, based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+)
 create mode 100644 Extra
manager@bl8vbox:~/Repository1$ git push
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behaviour now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

In Git 2.0, Git will default to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
Counting objects: 4, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 298 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/RedmarHuisman/Repository1.git
   4e2ae7e..41f626c  master -> master
manager@bl8vbox:~/Repository1$ ls
Extra  README.md

manager@bl8vbox:~/Repository1$ git pull
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From https://github.com/RedmarHuisman/Repository1
   41f626c..03caaca  master     -> origin/master
Updating 41f626c..03caaca
Fast-forward
 proteincalc.py | 39 +++++++++++++++++++++++++++++++++++++++
 1 file changed, 39 insertions(+)
 create mode 100644 proteincalc.py
manager@bl8vbox:~/Repository1$ ls
Extra  proteincalc.py  README.md
manager@bl8vbox:~/Repository1$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	all_seq_ali.2.phy_phyml_tree.svg

nothing added to commit but untracked files present (use "git add" to track)
manager@bl8vbox:~/Repository1$ git commit -m 'A Phylogenetic tree'
On branch master
Your branch is up-to-date with 'origin/master'.

Untracked files:
	all_seq_ali.2.phy_phyml_tree.svg

nothing added to commit but untracked files present
manager@bl8vbox:~/Repository1$ git push
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behaviour now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

In Git 2.0, Git will default to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
Everything up-to-date

manager@bl8vbox:~/Repository1$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	all_seq_ali.2.phy_phyml_tree.svg

no changes added to commit (use "git add" and/or "git commit -a")
manager@bl8vbox:~/Repository1$ git add all_seq_ali.2.phy_phyml_tree.svg 
manager@bl8vbox:~/Repository1$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   all_seq_ali.2.phy_phyml_tree.svg

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

manager@bl8vbox:~/Repository1$ git push
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behaviour now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

In Git 2.0, Git will default to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Username for 'https://github.com': Redmar Huisman
Password for 'https://Redmar Huisman@github.com': 
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/RedmarHuisman/Repository1.git/'
manager@bl8vbox:~/Repository1$ git push
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behaviour now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

In Git 2.0, Git will default to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
Everything up-to-date
manager@bl8vbox:~/Repository1$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   all_seq_ali.2.phy_phyml_tree.svg

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

manager@bl8vbox:~/Repository1$ git checkout README.md 
manager@bl8vbox:~/Repository1$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   all_seq_ali.2.phy_phyml_tree.svg

manager@bl8vbox:~/Repository1$ git commit -m 'A Phylogenetic tree'
[master b79fd07] A Phylogenetic tree
 Committer: System Manager <manager@bl8vbox.unassigned-domain>
Your name and e-mail address were configured automatically, based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 7 insertions(+)
 create mode 100644 all_seq_ali.2.phy_phyml_tree.svg
manager@bl8vbox:~/Repository1$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working directory clean
manager@bl8vbox:~/Repository1$ git push
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behaviour now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

In Git 2.0, Git will default to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
Counting objects: 4, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.86 KiB | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/RedmarHuisman/Repository1.git
   03caaca..b79fd07  master -> master
manager@bl8vbox:~/Repository1$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

nothing to commit, working directory clean
manager@bl8vbox:~/Repository1$ git checkout branch1
error: pathspec 'branch1' did not match any file(s) known to git.
manager@bl8vbox:~/Repository1$ git pull
From https://github.com/RedmarHuisman/Repository1
 * [new branch]      branch1    -> origin/branch1
Already up-to-date.
manager@bl8vbox:~/Repository1$ ls
all_seq_ali.2.phy_phyml_tree.svg  Extra  proteincalc.py  README.md
manager@bl8vbox:~/Repository1$ git checkout -branch branch1
fatal: Cannot update paths and switch to branch 'ranch' at the same time.
Did you intend to checkout 'branch1' which can not be resolved as commit?

manager@bl8vbox:~/Repository1$ git clone https://github.com/RedmarHuisman/Fairytale_test.git
Cloning into 'Fairytale_test'...
remote: Counting objects: 52, done.
remote: Compressing objects: 100% (33/33), done.
remote: Total 52 (delta 12), reused 52 (delta 12), pack-reused 0
Unpacking objects: 100% (52/52), done.
Checking connectivity... done.
manager@bl8vbox:~/Repository1$ ls
all_seq_ali.2.phy_phyml_tree.svg  Fairytale_test  README.md
Extra                             proteincalc.py  The Grade I Deserve is.md

manager@bl8vbox:~/Repository1$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	The Grade I Deserve is.md

nothing added to commit but untracked files present (use "git add" to track)
manager@bl8vbox:~/Repository1$ git clone https://github.com/RedmarHuisman/Fairytale_test.git
Cloning into 'Fairytale_test'...
remote: Counting objects: 52, done.
remote: Compressing objects: 100% (33/33), done.
remote: Total 52 (delta 12), reused 52 (delta 12), pack-reused 0
Unpacking objects: 100% (52/52), done.
Checking connectivity... done.
manager@bl8vbox:~/Repository1$ ls
all_seq_ali.2.phy_phyml_tree.svg  Fairytale_test  README.md
Extra                             proteincalc.py  The Grade I Deserve is.md
manager@bl8vbox:~/Repository1$ cd Fairytale_test
manager@bl8vbox:~/Repository1/Fairytale_test$ ls
Part1.txt  Part2.txt  README.md
manager@bl8vbox:~/Repository1/Fairytale_test$ nano Part1.txt
manager@bl8vbox:~/Repository1/Fairytale_test$ nano Part2.txt
manager@bl8vbox:~/Repository1/Fairytale_test$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   Part1.txt
	modified:   Part2.txt

no changes added to commit (use "git add" and/or "git commit -a")
manager@bl8vbox:~/Repository1/Fairytale_test$ git add Part1.txt
manager@bl8vbox:~/Repository1/Fairytale_test$ git add Part2.txt
manager@bl8vbox:~/Repository1/Fairytale_test$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   Part1.txt
	modified:   Part2.txt

manager@bl8vbox:~/Repository1/Fairytale_test$ git commit -m 'modified'[master 332660a] modified
 Committer: System Manager <manager@bl8vbox.unassigned-domain>
Your name and e-mail address were configured automatically, based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 2 files changed, 2 insertions(+), 2 deletions(-)
manager@bl8vbox:~/Repository1/Fairytale_test$ git push
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behaviour now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

In Git 2.0, Git will default to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
Counting objects: 10, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 411 bytes | 0 bytes/s, done.
Total 4 (delta 0), reused 0 (delta 0)
To https://github.com/RedmarHuisman/Fairytale_test.git
   50c674b..332660a  master -> master

To https://github.com/RedmarHuisman/Fairytale_test.git
   50c674b..332660a  master -> master
manager@bl8vbox:~/Repository1/Fairytale_test$ git clone https://github.com/Lumphie/Fairytale_test
Cloning into 'Fairytale_test'...
remote: Counting objects: 80, done.
remote: Compressing objects: 100% (53/53), done.
remote: Total 80 (delta 21), reused 79 (delta 20), pack-reused 0
Unpacking objects: 100% (80/80), done.
Checking connectivity... done.
manager@bl8vbox:~/Repository1/Fairytale_test$ ls
Fairytale_test  Part1.txt  Part2.txt  README.md
manager@bl8vbox:~/Repository1/Fairytale_test$ cd Fairytale_test/
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ ls
Part1.txt  Part1.txt~  Part2.txt  README.md
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ nano Part1.txt
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ ls
Part1.txt  Part1.txt~  Part2.txt  README.md
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   Part1.txt

no changes added to commit (use "git add" and/or "git commit -a")
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git add Part1.txt
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git push
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behaviour now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

In Git 2.0, Git will default to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
remote: Permission to Lumphie/Fairytale_test.git denied to RedmarHuisman.
fatal: unable to access 'https://github.com/Lumphie/Fairytale_test/': The requested URL returned error: 403
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ 

manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git push
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behaviour now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

In Git 2.0, Git will default to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
hremote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/Lumphie/Fairytale_test/'
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git push
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behaviour now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

In Git 2.0, Git will default to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
To https://github.com/Lumphie/Fairytale_test
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Lumphie/Fairytale_test'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git pull
remote: Counting objects: 55, done.
remote: Compressing objects: 100% (37/37), done.
remote: Total 55 (delta 19), reused 54 (delta 18), pack-reused 0
Unpacking objects: 100% (55/55), done.
From https://github.com/Lumphie/Fairytale_test
   88d145b..0abee68  master     -> origin/master
 * [new branch]      brach1     -> origin/brach1
 * [new branch]      frederic.labbe -> origin/frederic.labbe
Updating 88d145b..0abee68
error: Your local changes to the following files would be overwritten by merge:
	Part1.txt
Please, commit your changes or stash them before you can merge.
Aborting
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git push
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behaviour now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

In Git 2.0, Git will default to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
To https://github.com/Lumphie/Fairytale_test
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Lumphie/Fairytale_test'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git status
On branch master
Your branch is behind 'origin/master' by 20 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   Part1.txt

manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git commit -m 'modified'
[master e23a3cf] modified
 Committer: System Manager <manager@bl8vbox.unassigned-domain>
Your name and e-mail address were configured automatically, based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+), 1 deletion(-)
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ push
The program 'push' is currently not installed. You can install it by typing:
sudo apt-get install heimdal-clients
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ sudo apt-get install heimdal-clients
[sudo] password for manager: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  linux-headers-3.13.0-55 linux-headers-3.13.0-55-generic
  linux-image-3.13.0-55-generic linux-image-extra-3.13.0-55-generic
Use 'apt-get autoremove' to remove them.
The following extra packages will be installed:
  krb5-config libhdb9-heimdal libkadm5clnt7-heimdal libkadm5srv8-heimdal
  libkafs0-heimdal libotp0-heimdal libsl0-heimdal
Suggested packages:
  heimdal-docs heimdal-kcm
The following NEW packages will be installed
  heimdal-clients krb5-config libhdb9-heimdal libkadm5clnt7-heimdal
  libkadm5srv8-heimdal libkafs0-heimdal libotp0-heimdal libsl0-heimdal
0 to upgrade, 8 to newly install, 0 to remove and 146 not to upgrade.
Need to get 452 kB of archives.
After this operation, 1,888 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://gb.archive.ubuntu.com/ubuntu/ trusty-updates/main libhdb9-heimdal amd64 1.6~git20131207+dfsg-1ubuntu1.1 [59.2 kB]
Get:2 http://gb.archive.ubuntu.com/ubuntu/ trusty-updates/main libkadm5clnt7-heimdal amd64 1.6~git20131207+dfsg-1ubuntu1.1 [18.5 kB]
Get:3 http://gb.archive.ubuntu.com/ubuntu/ trusty-updates/main libkadm5srv8-heimdal amd64 1.6~git20131207+dfsg-1ubuntu1.1 [28.8 kB]
Get:4 http://gb.archive.ubuntu.com/ubuntu/ trusty-updates/main libkafs0-heimdal amd64 1.6~git20131207+dfsg-1ubuntu1.1 [15.1 kB]
Get:5 http://gb.archive.ubuntu.com/ubuntu/ trusty-updates/main libotp0-heimdal amd64 1.6~git20131207+dfsg-1ubuntu1.1 [29.8 kB]
Get:6 http://gb.archive.ubuntu.com/ubuntu/ trusty-updates/main libsl0-heimdal amd64 1.6~git20131207+dfsg-1ubuntu1.1 [13.3 kB]
Get:7 http://gb.archive.ubuntu.com/ubuntu/ trusty/main krb5-config all 2.3 [23.4 kB]
Get:8 http://gb.archive.ubuntu.com/ubuntu/ trusty-updates/universe heimdal-clients amd64 1.6~git20131207+dfsg-1ubuntu1.1 [264 kB]
Fetched 452 kB in 0s (959 kB/s)          
Preconfiguring packages ...
Selecting previously unselected package libhdb9-heimdal:amd64.
(Reading database ... 382098 files and directories currently installed.)
Preparing to unpack .../libhdb9-heimdal_1.6~git20131207+dfsg-1ubuntu1.1_amd64.deb ...
Unpacking libhdb9-heimdal:amd64 (1.6~git20131207+dfsg-1ubuntu1.1) ...
Selecting previously unselected package libkadm5clnt7-heimdal:amd64.
Preparing to unpack .../libkadm5clnt7-heimdal_1.6~git20131207+dfsg-1ubuntu1.1_amd64.deb ...
Unpacking libkadm5clnt7-heimdal:amd64 (1.6~git20131207+dfsg-1ubuntu1.1) ...
Selecting previously unselected package libkadm5srv8-heimdal:amd64.
Preparing to unpack .../libkadm5srv8-heimdal_1.6~git20131207+dfsg-1ubuntu1.1_amd64.deb ...
Unpacking libkadm5srv8-heimdal:amd64 (1.6~git20131207+dfsg-1ubuntu1.1) ...
Selecting previously unselected package libkafs0-heimdal:amd64.
Preparing to unpack .../libkafs0-heimdal_1.6~git20131207+dfsg-1ubuntu1.1_amd64.deb ...
Unpacking libkafs0-heimdal:amd64 (1.6~git20131207+dfsg-1ubuntu1.1) ...
Selecting previously unselected package libotp0-heimdal:amd64.
Preparing to unpack .../libotp0-heimdal_1.6~git20131207+dfsg-1ubuntu1.1_amd64.deb ...
Unpacking libotp0-heimdal:amd64 (1.6~git20131207+dfsg-1ubuntu1.1) ...
Selecting previously unselected package libsl0-heimdal:amd64.
Preparing to unpack .../libsl0-heimdal_1.6~git20131207+dfsg-1ubuntu1.1_amd64.deb ...
Unpacking libsl0-heimdal:amd64 (1.6~git20131207+dfsg-1ubuntu1.1) ...
Selecting previously unselected package krb5-config.
Preparing to unpack .../krb5-config_2.3_all.deb ...
Unpacking krb5-config (2.3) ...
Selecting previously unselected package heimdal-clients.
Preparing to unpack .../heimdal-clients_1.6~git20131207+dfsg-1ubuntu1.1_amd64.deb ...
Unpacking heimdal-clients (1.6~git20131207+dfsg-1ubuntu1.1) ...
Processing triggers for man-db (2.6.7.1-1ubuntu1) ...
Setting up libhdb9-heimdal:amd64 (1.6~git20131207+dfsg-1ubuntu1.1) ...
Setting up libkadm5clnt7-heimdal:amd64 (1.6~git20131207+dfsg-1ubuntu1.1) ...
Setting up libkadm5srv8-heimdal:amd64 (1.6~git20131207+dfsg-1ubuntu1.1) ...
Setting up libkafs0-heimdal:amd64 (1.6~git20131207+dfsg-1ubuntu1.1) ...
Setting up libotp0-heimdal:amd64 (1.6~git20131207+dfsg-1ubuntu1.1) ...
Setting up libsl0-heimdal:amd64 (1.6~git20131207+dfsg-1ubuntu1.1) ...
Setting up krb5-config (2.3) ...
Setting up heimdal-clients (1.6~git20131207+dfsg-1ubuntu1.1) ...
update-alternatives: using /usr/bin/krsh to provide /usr/bin/rsh (rsh) in auto mode
update-alternatives: using /usr/bin/krcp to provide /usr/bin/rcp (rcp) in auto mode
update-alternatives: using /usr/bin/kpagsh to provide /usr/bin/pagsh (pagsh) in auto mode
Processing triggers for libc-bin (2.19-0ubuntu6.9) ...
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git push
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behaviour now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

In Git 2.0, Git will default to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
To https://github.com/Lumphie/Fairytale_test
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Lumphie/Fairytale_test'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git pull
remote: Counting objects: 39, done.
remote: Compressing objects: 100% (32/32), done.
remote: Total 39 (delta 18), reused 3 (delta 3), pack-reused 4
Unpacking objects: 100% (39/39), done.
From https://github.com/Lumphie/Fairytale_test
   b243f21..da1c66d  master     -> origin/master
Auto-merging Part1.txt
CONFLICT (content): Merge conflict in Part1.txt
Automatic merge failed; fix conflicts and then commit the result.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ nano Part1.txt
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git pull
U	Part1.txt
M	Part1.txt~
M	Part2.txt
M	Part2.txt~
M	README.md
A	README.md~
Pull is not possible because you have unmerged files.
Please, fix them up in the work tree, and then use 'git add/rm <file>'
as appropriate to mark resolution, or use 'git commit -a'.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git commit -a
[master 9b38630] Merge branch 'master' of https://github.com/Lumphie/Fairytale_test
 Committer: System Manager <manager@bl8vbox.unassigned-domain>
Your name and e-mail address were configured automatically, based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ tail history
tail: cannot open ‘history’ for reading: No such file or directory
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$  history|tail
 1205  git commit -m "modified"
 1206  git status
 1207  git push
 1208  git status
 1209  git push
 1210  git pull
 1211  nano Part1.txt
 1212  git pull
 1213  git commit -a
 1214  tail history
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git commit -m "modification"
On branch master
Your branch is ahead of 'origin/master' by 3 commits.
  (use "git push" to publish your local commits)

nothing to commit, working directory clean
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git status
On branch master
Your branch is ahead of 'origin/master' by 3 commits.
  (use "git push" to publish your local commits)

nothing to commit, working directory clean
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git push
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behaviour now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

In Git 2.0, Git will default to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
To https://github.com/Lumphie/Fairytale_test
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Lumphie/Fairytale_test'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git pull
remote: Counting objects: 57, done.
remote: Compressing objects: 100% (32/32), done.
remote: Total 57 (delta 31), reused 51 (delta 25), pack-reused 0
Unpacking objects: 100% (57/57), done.
From https://github.com/Lumphie/Fairytale_test
   da1c66d..3cf0ab9  master     -> origin/master
 * [new branch]      Brach1     -> origin/Brach1
 * [new branch]      coconuts   -> origin/coconuts
Auto-merging Part1.txt
CONFLICT (content): Merge conflict in Part1.txt
Automatic merge failed; fix conflicts and then commit the result.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ nano Part1.txt
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git pull
A	FairyNinja.sh
U	Part1.txt
M	Part2.txt
M	Part2.txt~
Pull is not possible because you have unmerged files.
Please, fix them up in the work tree, and then use 'git add/rm <file>'
as appropriate to mark resolution, or use 'git commit -a'.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ gti status
No command 'gti' found, did you mean:
 Command 'gtf' from package 'xserver-xorg-core' (main)
 Command 'git' from package 'git' (main)
 Command 'gsi' from package 'gambc' (universe)
 Command 'gt' from package 'genometools' (universe)
 Command 'gtg' from package 'gtg' (universe)
 Command 'gt5' from package 'gt5' (universe)
 Command 'bti' from package 'bti' (universe)
 Command 'gri' from package 'gri' (universe)
 Command 'gtm' from package 'postgres-xc' (universe)
 Command 'ti' from package 'ticgit' (universe)
 Command 'gtv' from package 'smpeg-gtv' (universe)
gti: command not found
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git push
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behaviour now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

In Git 2.0, Git will default to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/Lumphie/Fairytale_test/'
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git config --global push.default matching
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git push
Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
To https://github.com/Lumphie/Fairytale_test
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Lumphie/Fairytale_test'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git pull
A	FairyNinja.sh
U	Part1.txt
M	Part2.txt
M	Part2.txt~
Pull is not possible because you have unmerged files.
Please, fix them up in the work tree, and then use 'git add/rm <file>'
as appropriate to mark resolution, or use 'git commit -a'.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git status
On branch master
Your branch and 'origin/master' have diverged,
and have 3 and 20 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

You have unmerged paths.
  (fix conflicts and run "git commit")

Changes to be committed:

	new file:   FairyNinja.sh
	modified:   Part2.txt
	modified:   Part2.txt~

Unmerged paths:
  (use "git add <file>..." to mark resolution)

	both modified:      Part1.txt

manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git add .
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git commit -m "modi"
[master 40a7fa1] modi
 Committer: System Manager <manager@bl8vbox.unassigned-domain>
Your name and e-mail address were configured automatically, based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git push
Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
To https://github.com/Lumphie/Fairytale_test
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Lumphie/Fairytale_test'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git pull
remote: Counting objects: 36, done.
remote: Compressing objects: 100% (18/18), done.
remote: Total 36 (delta 24), reused 30 (delta 18), pack-reused 0
Unpacking objects: 100% (36/36), done.
From https://github.com/Lumphie/Fairytale_test
   3cf0ab9..5213a4d  master     -> origin/master
Auto-merging Part1.txt
error: There was a problem with the editor 'editor'.
Not committing merge; use 'git commit' to complete the merge.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git commit -m "m"
[master 47a8012] m
 Committer: System Manager <manager@bl8vbox.unassigned-domain>
Your name and e-mail address were configured automatically, based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git pull
remote: Counting objects: 15, done.
remote: Compressing objects: 100% (15/15), done.
remote: Total 15 (delta 7), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (15/15), done.
From https://github.com/Lumphie/Fairytale_test
   5213a4d..113c4bc  master     -> origin/master
Auto-merging Part1.txt
CONFLICT (content): Merge conflict in Part1.txt
Automatic merge failed; fix conflicts and then commit the result.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ nano Part1.txt
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git pull
U	Part1.txt
Pull is not possible because you have unmerged files.
Please, fix them up in the work tree, and then use 'git add/rm <file>'
as appropriate to mark resolution, or use 'git commit -a'.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git add Part1.txt
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git pull
You have not concluded your merge (MERGE_HEAD exists).
Please, commit your changes before you can merge.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git commit -m "m"
[master 3421bf7] m
 Committer: System Manager <manager@bl8vbox.unassigned-domain>
Your name and e-mail address were configured automatically, based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git pull
remote: Counting objects: 30, done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 30 (delta 17), reused 30 (delta 17), pack-reused 0
Unpacking objects: 100% (30/30), done.
From https://github.com/Lumphie/Fairytale_test
   113c4bc..e4b8e30  master     -> origin/master
Auto-merging Part1.txt
CONFLICT (content): Merge conflict in Part1.txt
Automatic merge failed; fix conflicts and then commit the result.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git push
Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
To https://github.com/Lumphie/Fairytale_test
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/Lumphie/Fairytale_test'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ nano Part1.txt
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git add Part1.txt
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git commit -m "m"
[master 6fc60bd] m
 Committer: System Manager <manager@bl8vbox.unassigned-domain>
Your name and e-mail address were configured automatically, based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git push
Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
To https://github.com/Lumphie/Fairytale_test
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Lumphie/Fairytale_test'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git pull
remote: Counting objects: 31, done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 31 (delta 17), reused 31 (delta 17), pack-reused 0
Unpacking objects: 100% (31/31), done.
From https://github.com/Lumphie/Fairytale_test
   e4b8e30..52db864  master     -> origin/master
 * [new branch]      forhelen   -> origin/forhelen
Removing Part2.txt~
Auto-merging Part1.txt
Merge made by the 'recursive' strategy.
 Fairytale_test |  1 +
 Part1.txt      |  1 +
 Part2.txt      |  2 ++
 Part2.txt~     | 21 ---------------------
 4 files changed, 4 insertions(+), 21 deletions(-)
 create mode 160000 Fairytale_test
 delete mode 100644 Part2.txt~
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git pull
remote: Counting objects: 12, done.
remote: Compressing objects: 100% (12/12), done.
remote: Total 12 (delta 3), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (12/12), done.
From https://github.com/Lumphie/Fairytale_test
   52db864..24a8566  master     -> origin/master
 * [new branch]      adriaan-dev -> origin/adriaan-dev
Merge made by the 'recursive' strategy.
 Part2.txt | 9 ++++-----
 1 file changed, 4 insertions(+), 5 deletions(-)
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git push
Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
Counting objects: 45, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (26/26), done.
Writing objects: 100% (26/26), 3.56 KiB | 0 bytes/s, done.
Total 26 (delta 12), reused 0 (delta 0)
remote: Resolving deltas: 100% (12/12), completed with 5 local objects.
To https://github.com/Lumphie/Fairytale_test
   24a8566..07325d3  master -> master
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ 
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git commit -m "o"
[master 51079dc] o
 Committer: System Manager <manager@bl8vbox.unassigned-domain>
Your name and e-mail address were configured automatically, based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git push
Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
To https://github.com/Lumphie/Fairytale_test
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Lumphie/Fairytale_test'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git pull
remote: Counting objects: 33, done.
remote: Compressing objects: 100% (33/33), done.
remote: Total 33 (delta 16), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (33/33), done.
From https://github.com/Lumphie/Fairytale_test
   69d7572..20300cc  master     -> origin/master
Merge made by the 'recursive' strategy.
 Part1.txt   |  9 +++++++--
 Part1.txt~  | 62 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 Part1.txt~~ | 34 +++++++++++++++++++++++++++++++++
 Part2.txt~  |  6 +-----
 Part3.txt   |  1 +
 5 files changed, 105 insertions(+), 7 deletions(-)
 create mode 100644 Part1.txt~~
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git push
Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
Counting objects: 23, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 1.00 KiB | 0 bytes/s, done.
Total 8 (delta 5), reused 0 (delta 0)
remote: Resolving deltas: 100% (5/5), completed with 4 local objects.
To https://github.com/Lumphie/Fairytale_test
   20300cc..b2d3c1b  master -> master
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ ls
FairyNinja.sh   Part1.txt   Part1.txt~~  Part2.txt   Part3.txt  README.md~
Fairytale_test  Part1.txt~  Part.2txt    Part2.txt~  README.md
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ nano Part3.txt
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git add .
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git commit -m "o"
[master 60d3a5f] o
 Committer: System Manager <manager@bl8vbox.unassigned-domain>
Your name and e-mail address were configured automatically, based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 2 insertions(+)
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git push
Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
To https://github.com/Lumphie/Fairytale_test
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Lumphie/Fairytale_test'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git pull
remote: Counting objects: 7, done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 7 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (7/7), done.
From https://github.com/Lumphie/Fairytale_test
   b2d3c1b..e6b9de0  master     -> origin/master
   0abee68..5471261  brach1     -> origin/brach1
Merge made by the 'recursive' strategy.
 FairyNinja.sh | 2 +-
 Part1.txt     | 4 ++++
 2 files changed, 5 insertions(+), 1 deletion(-)
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git push
Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
To https://github.com/Lumphie/Fairytale_test
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Lumphie/Fairytale_test'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git pull
remote: Counting objects: 8, done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 8 (delta 3), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (8/8), done.
From https://github.com/Lumphie/Fairytale_test
   e6b9de0..ed9bfca  master     -> origin/master
Merge made by the 'recursive' strategy.
 Part2.txt | 1 +
 1 file changed, 1 insertion(+)
manager@bl8vbox:~/Repository1/Fairytale_test/Fairytale_test$ git push
Username for 'https://github.com': RedmarHuisman
Password for 'https://RedmarHuisman@github.com': 
Counting objects: 18, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (7/7), done.
Writing objects: 100% (7/7), 965 bytes | 0 bytes/s, done.
Total 7 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), completed with 2 local objects.
To https://github.com/Lumphie/Fairytale_test
   ed9bfca..aa1aed7  master -> master

Travis CI
sudo: require

install:
  - sudo apt-get install cowsay

script: 
  - export PATH=/usr/bin:/bin:/usr/games
  - cowsay "Howdy"
  - cowsay "Howdy" | cowsay -n
  - cowsay "Howdy" | cowsay -n | cowsay -n
  - cowsay "Howdy" | cowsay -n | cowsay -n | cowsay -n
  - cowsay "Moo" | cowsay -n | cowsay -n | cowsay -n | cowsay -n
  - cowsay "Moo" | cowsay -n | cowsay -n | cowsay -n | cowsay -n | cowsay -n
  - cowsay "Moo" | cowsay -n -f stegosaurus
Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help
