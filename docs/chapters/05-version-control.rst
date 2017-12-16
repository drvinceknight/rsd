Version control
===============

Objectives
----------

- Understand motivation/purpose of version control.
- Set up git on their own machines.
- Be able to use git for basic history, commits and branches.

Plan
----

- Have a discussion referring to two aspects of the life cycle of a research
  project:
  - It's change over time: history.
  - Working on various things at the same time (with potentially more than one
    person): parallel workflow.
- Draw picture of this life cycle using examples from prime factorisation done
  in previous chapter.
- Ask: what problems can occur? (including not know what happened at a given
  stage)
- Ask: what do individuals currently do to work around this? Expect people to
  talk about dropbox having versions, naming files with suffixes, copying work
  from collaborators. Discuss possible drawback to this.
- Explain that this chapter will concentrate on the first of these two aspects
  but will begin to touch on the second. And the goal will be to remove
  possibility for human error as much as possible.
- Setup: ensure editors are setup. For some windows users they might have to use
  Nano. It is expected that this setup might take a little while.
- Demonstrate init: explain that this corresponds to telling git to start paying
  attention.
- Demonstrate staging and committing. The important of a commit message being
  able to know what any given stage was.
- Tracking changes: might need to discuss that tediousness of writing a commit
  message is offset by benefit. Also, discuss when to commit.
- Show gitignore: explain that that can be changed over time.
- Show how to see the history. Using `git log` then discuss how we can now
  solve one of the identified problems which is to recover a file using `git
  checkout`.
- Now demonstrate the ability to do work in parallel using branches.
- Demonstrate merging. Mention merge conflicts.
- Summarise and discuss tips.

FAQ
---
