Best practice with LaTeX
========================

Objectives
----------

- Compile LaTeX from command line;
- Have a consistent and meaningful directory structure for LaTeX;
- Inputting software outputs automatically/directly in to LaTeX.

Plan
----

1. Discuss LaTeX: ask if everyone has used it before? If anyone hasn't perhaps
   make sure a tutor is closer to them. For those who have used it before,
   explain that we're going to not talk about how to write specific things but
   talk about best practice.
2. Open up editor and create the basic file saved in `rsd-workshop`: compile it.
3. Discuss how editors can be used for various tasks. In this workshop we have covered two,
   writing code and LaTeX. Editors come with plugins to help users with their different
   tasks, for LaTeX the following plugins exist:
    - VSCode, `LaTeX Workshop <https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop>`_
    - Atom, `latex <https://atom.io/packages/latex>`_
4. Describe calling one document from another. Explain why we do this: clearer
   directory structure and further modularisation. Helps separate: content
   (`tex/`) from instructions (`main.tex`).
5. Talk about the directory structure: move all python files to `src`.
   Create/copy the file to create a scatter plot and show how to run that and
   use output directly in code. **Note** the name of the python: same name for
   pdf graph, same name for label in latex document. This helps ensure users
   won't be left wondering where one thing comes from.
6. Go through other examples. For all of these, invite participants to download
   the files: no need to write them. The purpose of this workshop is not to
   teach advanced Python, but emphasise that similar functionality exists in
   most languages. (For example, if you don't have functionality to write the
   LaTeX code for a table directly you can just use the programming language to
   write the LaTeX using for loops etc...)

FAQ
---

- **Question:** Why do can I not use Word?
  **Answer:** Using a GUI implies a lot of the things we've discussed here is
  not possible (dynamically reading input from file for example) and thus leaves
  the possibility for human error. Also: portability, sharing research using a
  closed commercial solution implies that it can only be consumed by those that
  have the same closed commercial solution.
