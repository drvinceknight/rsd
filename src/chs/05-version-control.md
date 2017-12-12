# Version control

When carrying out research it can be beneficial to be able to:

- examine the entire history of the project.
- rewind and retrieve a file from the past.
- combine changes from two different parallel pieces of work.

The potential for human error when doing these things can be handled by
software. The particular tool we will use is `git.

## Setting up git

Before we get started there are a couple of things we need to do to set up
`git`. Recall that `git` keeps track of the entire history of a project, this
does not only mean keeping track of what was done but also who did it (this is
particularly important in collaborative work).

We start by telling git who we are. Open your command line and type:

```bash
git config --global user.name "Your Name"
```

```bash
git config --global user.email "Your Email"
```

**Note** this is not data that is being collected by any cloud service or
similar. It just stays with your project.

At various times, `git` might want to open a text editor (this will be come
clear very soon). Let us set up `git` to use your editor of choice.

**Windows**

To use Atom:

```bash
git config --global core.editor "C:\Program Files (x86)\atom.exe --wait"
```

To use VS code:

```bash
git config --global core.editor "'C:\Program Files (x86)\Microsoft VS Code\code.exe' --wait"
```

Note the path might be a bit different (depending on where atom/vs code was installed on
your machine).

**nix**

To use Atom:

```bash
git config --global core.editor "atom --wait"
```

To use VS code:

```bash
git config --global core.editor "code --wait"
```

## Initialising a git repository

Let us start by creating a new directory: `rsd-checklist`.

Inside that let us create a `main.tex` document which we will use to create a
checklist of things learned on this course.

```tex
\documentclass{article}

\title{Research software development checklist}

\begin{document}
\maketitle
\end{document}
```

Now let us tell `git` to start keeping an eye on this repository. In the command
line:

```bash
git init
```

You should then see a message saying that you have successfully initialised a
git repository.

## Staging and committing changes

Let us see what is the status of our repository:

```bash
git status
```

We should see something like:

```bash
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        main.tex

nothing added to commit but untracked files present (use "git add" to track)
```

There are various pieces of useful information here, first of all `main.tex` is not currently a tracked file.

We are now going to track that file:

```bash
git add main.tex
```

If we run `git status` again we see:

```bash
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   main.tex

```

So the changes we have made to `main.tex` (ie starting the file) are ready to
be "committed".

```bash
git commit
```

When doing this, your editor of choice should open up prompting you to write
what is called a commit message.

Type the following:

```md
Write blank checklist

This file is currently empty but will include the various aspects of sustainable
software development learnt on the 2 day rsd workshop.
```

Once you have written that, save and exit from your editor. `git` should confirm
that you have successfully made your first commit.

```bash
[master (root-commit) 3c1e5ad] write blank checklist
 1 file changed, 7 insertions(+)
 create mode 100644 main.tex
```

Now if we run `git status`, we see a message saying that everything in our
repository is tracked and up to date:

```bash
On branch master
nothing to commit, working directory clean
```

**Note** A commit message is made up of 2 main components:

```md
<Title of the commit>

<Description of what was done>
```

- The title should be a description in the form of "if this commit is applied
  `<title of the commit>` will happen". The convention is for this to be rather
  short and to the point.
- The description can be as long as needed and should be a helpful explanation
  of what is happening.


A commit is a snapshot that `git` makes of your project, you should use this at
meaningful steps of the progress of a project.

## Tracking changes to files

Let us add our name to the checklist document:

```tex
\documentclass{article}

\title{Research software development checklist}
\author{Grace Hopper}

\begin{document}
\maketitle
\end{document}
```

Save your file and then run `git status`. We now see that `git` is aware of a
change to our file:


```bash
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   main.tex

no changes added to commit (use "git add" and/or "git commit -a")
```

To "stage" the file for a commit we use `git add` again:

```bash
git add main.tex
```

Now let us commit:

```bash
git commit
```

With the following commit message:

```md
add author name
```

In this particular case there is not much more needed than the title.

Finally, we can check the status: `git status` to confirm that everything has
been done correctly.

## Ignoring files

Let us compile our LaTeX document:

```bash
pdflatex main.tex
```

Now if we check the status of our repository:

```bash
git status
```

We see that all the LaTeX auxiliary files are listed along with the pdf:

```bash
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        main.aux
        main.log
        main.pdf

nothing added to commit but untracked files present (use "git add" to track)
```

To tell `git` to ignore these files (we only need the `tex` file) we will add them to a blank file entitled `.gitignore`. Open your editor and type

```
main.aux
main.log
main.pdf
```

Save that file as `.gitignore` and then run `git status` again. We see now that
`git` is ignoring those 3 files but is aware of the `.gitignore` file. Let us
add and commit that file:

```
git add .gigignore
git commit
```

Use `add .gitignore` as the commit message.

At a later stage we can always modify this
`.gitignore` file (perhaps we might choose to tell `git` to track the pdf):

## Exploring and using history

We have done a good job of keep track of the history of our project but let us
see how that can be useful.

First, let us confirm our repository is in the expected state with `git status`:

```bash
On branch master
nothing to commit, working directory clean
```

Now, let us look at our history:

```bash
git log
```

This displays the full log of the project:

```bash
commit b116460039bb9ed1f79a980a7a71b5b75f0618b4
Author: Vince Knight <vincent.knight@gmail.com>
Date:   Sat Dec 9 11:40:47 2017 +0000

    add .gitignore

commit 84c678c01ef099aeedc46c922feb38557cffd5c7
Author: Vince Knight <vincent.knight@gmail.com>
Date:   Sat Dec 9 11:34:43 2017 +0000

    add author name

commit 3c1e5adc13069023d25a76570f092135d0eeb68c
Author: Vince Knight <vincent.knight@gmail.com>
Date:   Sat Dec 9 10:59:04 2017 +0000

    write blank checklist

    This file is currently empty but will include the various aspects of
    sustainable
    software development learnt on the 2 day rsd workshop.
```

We see that there are 3 commits there, each with a seemingly random set of
numbers and characters. This set of characters is called a "hash":

The first commit with title `write blank checklist` has hash:
`3c1e5adc13069023d25a76570f092135d0eeb68c`. **Note** that on your machines this
hash will be different, in fact every hash is mathematically guaranteed to be
unique, thus it is uniquely assigned to the changes made.

One of the things that this hash allows us to do is to go back in time. Let us
go back to the `main.tex` file before we added the author name. We do this with
the `checkout` command and make use of the hash (simply copy it or type the
first few characters). In the case of the example here, using the hash:

```bash
git checkout 3c1e5adc13069023d25 main.tex
```

If we now run `git status` we see that the file has changed:

```bash
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   main.tex

```

(Open `main.tex` and see that the author name is no longer there.)
We could at this stage make more changes to `main.tex` and commit them as before.

Or in this particular case we might want to return the file to the state it was.
We can use `HEAD` which is shorthand for the hash corresponding to the last
commit:

```
git checkout HEAD main.tex
```

If you run `git status` you will see that everything is back to how it was with
the author name.

## Creating branches

At the start of this chapter we discussed the ability to work in parallel thanks
to `git`. This is done using something called "branches".

When typing `git status` we have seen that one piece of information regularly
given was `On branch master`. This is telling us which branch of "history" we
are currently on. To view all branches:

```bash
git branch
```

This shows:

```bash
* master
```

So currently there is only one branch. Let us create a new branch called
`add-list-of-topics`:

```bash
git branch add-list-of-topics
```

When we now type `git branch` we see that 2 branches exist but the active branch
is indicated by `*`:

```bash
  add-list-of-topics
* master
```

Let us now move to this new branch:

```bash
git checkout add-list-of-topics
```

Run `git branch` and then `git status` to see how this has worked.

Let us now create a `tex` folder and in that folder let us write a
`list-of-topics.tex` document:

```tex
\begin{itemize}
    \item Using the command line to be able to control my machine. \checkmark
    \item Use basic Python. \checkmark
    \item Write modular code. \checkmark
    \item Write documented code. \checkmark
    \item Write automatde tested. \checkmark
    \item Write modular LaTeX. \checkmark
    \item Include outputs of software directly in LaTeX. \checkmark
    \item Understanding of git.
    \item Use github to collaboratively work on projects.
\end{itemize}
```

Let us add and commit this file:

```bash
git add tex/list-of-topics.tex
git commit
```

Let us now return to the `master` branch, we will come back to this list
shortly.

```bash
git checkout master
```

Let us create a new branch called `change-page-width`. We'll use this branch to
modify the page width:

```bash
git branch change-page-width
git checkout change-page-width
```

Let us modify `main.tex` to include the following in the preamble:

```tex
\documentclass{article}

\usepackage[margin=1.5cm, includefoot, footskip=30pt]{geometry}

\title{Research software development checklist}

\begin{document}
\maketitle
\end{document}
```

If you compile the document you should see it occupies the page better (there's
not much text yet to be able to compare but you get the idea).

Stage and commit this change and take a look at the log:

```bash
commit f252f5a6fcb79fb19c0bc8e7262a265da560b800
Author: Vince Knight <vincent.knight@gmail.com>
Date:   Sat Dec 9 12:16:45 2017 +0000

    change page width

commit b116460039bb9ed1f79a980a7a71b5b75f0618b4
Author: Vince Knight <vincent.knight@gmail.com>
Date:   Sat Dec 9 11:40:47 2017 +0000

    add .gitignore

commit 84c678c01ef099aeedc46c922feb38557cffd5c7
Author: Vince Knight <vincent.knight@gmail.com>
Date:   Sat Dec 9 11:34:43 2017 +0000

    add author name

commit 3c1e5adc13069023d25a76570f092135d0eeb68c
Author: Vince Knight <vincent.knight@gmail.com>
Date:   Sat Dec 9 10:59:04 2017 +0000

    write blank checklist

    This file is currently empty but will include the various aspects of
    sustainable
    software development learnt on the 2 day rsd workshop.

```

We see that the commit made on the `add-list-of-topics` branch does not appear
here. This is the behaviour of `git log` it only shows the history of the
current branch.

Let us return to the `master` branch and see how to combine the work that has
been done on each of these branches:

```bash
git checkout master
```

## Merging branches

Getting the work from one branch on to another branch is called "merging". Let
us merge the `change-page-width` branch in to the `master` branch (which is our
current branch).

**Note** before doing a merge it is always a good idea to check `git status` to
ensure everything is in the state we required (e.g. that we are on the correct
branch etc...).

```bash
git merge change-page-width
```

We should see something like:

```bash
Updating b116460..f252f5a
Fast-forward
 main.tex | 2 ++
 1 file changed, 2 insertions(+)
```

Recall, if you forget the name of branches you can always run `git
branch` to see all the branches.

Let us also merge our `add-list-of-topics` branch:

```bash
git merge add-list-of-topics
```

When doing merges sometimes `git` will open the editor asking for you to confirm
the merge commit message. This is because there are various algorithms `git`
uses to be able to merge and some require making a snapshot.

If this happens during a merge, do not feel that you have to modify the commit
message (unless you want to!).

```
Merge made by the 'recursive' strategy.
 tex/list-of-topics.tex | 11 +++++++++++
 1 file changed, 11 insertions(+)
 create mode 100644 tex/list-of-topics.tex
```

Your directory should now look like this:


```bash
|---rsd-checklist
    |--- main.tex
    |--- main.aux
    |--- main.log
    |--- main.pdf
    |--- tex/
         |--- list-of-topics.tex
```

We will make one final modification to `main.tex` to include the
`list-of-topics.tex` file:

```tex
\documentclass{article}

\usepackage[margin=1.5cm, includefoot, footskip=30pt]{geometry}
\usepackage{amssymb}  % for the checkmark

\title{Research software development checklist}
\author{Grace Hopper}

\begin{document}
\maketitle

\input{tex/list-of-topics.tex}
\end{document}
```

Compile your document and take a look at your checklist!

Before we commit this final change let us take a look at one final command:

```bash
git diff
```

This displays the difference between the current state of our repository and the
last commit:

```bash
diff --git a/main.tex b/main.tex
index bc59d80..4f26c4f 100644
--- a/main.tex
+++ b/main.tex
@@ -1,10 +1,13 @@
 \documentclass{article}

 \usepackage[margin=1.5cm, includefoot, footskip=30pt]{geometry}
+\usepackage{amssymb}  % for the checkmark

 \title{Research software development checklist}
 \author{Grace Hopper}

 \begin{document}
 \maketitle
+
+\input{tex/list-of-topics.tex}
 \end{document}
(END)

```

We have added `\usepackage{amssymb}  % for the checkmark` and
`\input{tex/list-of-topics.tex}`.

Now let us stage and then commit this and look at the log:

```bash
commit c1689ea9c56603882e19a6ccf90625190db29ec7
Author: Vince Knight <vincent.knight@gmail.com>
Date:   Sat Dec 9 12:31:34 2017 +0000

    include list of topics in main doc

commit 2e94caa07c10beb47e767f7800bf9852b9931783
Merge: f252f5a b71bdc8
Author: Vince Knight <vincent.knight@gmail.com>
Date:   Sat Dec 9 12:23:42 2017 +0000

    Merge branch 'add-list-of-topics'

commit f252f5a6fcb79fb19c0bc8e7262a265da560b800
Author: Vince Knight <vincent.knight@gmail.com>
Date:   Sat Dec 9 12:16:45 2017 +0000

    change page width

commit b71bdc809c48e01fd34d60476d09baae34402b63
Author: Vince Knight <vincent.knight@gmail.com>
Date:   Sat Dec 9 12:07:52 2017 +0000

    write list of topics

    Include checkmark for things we have currently covered.

commit b116460039bb9ed1f79a980a7a71b5b75f0618b4
Author: Vince Knight <vincent.knight@gmail.com>
Date:   Sat Dec 9 11:40:47 2017 +0000

    add .gitignore

commit 84c678c01ef099aeedc46c922feb38557cffd5c7
Author: Vince Knight <vincent.knight@gmail.com>
Date:   Sat Dec 9 11:34:43 2017 +0000

    add author name

commit 3c1e5adc13069023d25a76570f092135d0eeb68c
Author: Vince Knight <vincent.knight@gmail.com>
Date:   Sat Dec 9 10:59:04 2017 +0000

    write blank checklist

    This file is currently empty but will include the various aspects of
    sustainable
    software development learnt on the 2 day rsd workshop.

```

We can see the entire history of what we have written and could potentially go
back to any stage. Furthermore, our directory is tidy without the need for
various confusin suffixes at the end of each file.

**Note** Branching is "cheap" in terms of the amount of space it takes up. Thus
it's always a good idea to branch when working on a project if you want to try
out something.

**Note** It is possible to create something called a "merge conflict". This
occurs when mergeing changes that `git` is unable to merge automatically. For
example changing the same line in a file. In this case, git will ask for you to
modify the file and commit it to complete the merge.

## Summary

Here are the commands we have seen in this chapter:

- `git init`: Create a git repository
- `git add <file>`: Start tracking `<file>` and/or stage the changes to `<file>`
  ready to be committed.
- `git status`: See the current status of your git repository.
- `git commit`: Create a snapshot of the current changes.
- `git checkout <hash> <file>`: Set `<file>` to be in the same state as it was
  in the commit corresponding to `<hash>`. Note that `HEAD` is shorthand for the
  last commit.
- `git branch`: List all branches.
- `git branch <branch-name>`: Create a new branch called `<branch-name>`.
- `git checkout <branch-name>`: Move to `<branch-name>`.
- `git merge <branch-name>`: Merge `<branch-name>` in to the current branch.
- `git diff`: Show the differences between the current state of the repository
  and the last commit.

## Tip

- `git` keep track of things on a line by line basis. Thus changing any given
  character in any given line corresponds to changing the whole line. In the
  interest of keeping commits meaningful (thus helpful) it is useful to
  regularly line return in LaTeX documents otherwise changing various words in a
  paragraph can correspond to the same overall change.
- There are a number of excellent helpful tools for interfacing with `git`. It
  is recommended to start by learning these basic commands directly so that you
  understand what is going on in the background before making use of the helpful
  tools.
