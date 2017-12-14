# Markdown

Markdown is a:

> Markdown is a lightweight markup language with plain text formatting syntax. 

Markdown is a simple set of conventions for how to write text in plain text.
It is designed to ensure that it can be straightforwardly converted to html and
also easy to read in plain text.

A lot of descriptive files in software are written in markdown. For example most
repositories have a `README.md` which explains what the repository is for.
Github automatically renders these.

There are a number of great guides for markdown:

- [github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [help.github.com/articles/basic-writing-and-formatting-syntax/](https://help.github.com/articles/basic-writing-and-formatting-syntax/)
- [daringfireball.net/projects/markdown/syntax](https://daringfireball.net/projects/markdown/syntax)

Here is some basic syntax:

## Headers and titles

Use `#` to denote headers of various levels:

```markdown

# This is the title

## This is a section at the next level

### This is a section at the next next level

```

## Text formatting

You can create bold and italicized text:

```markdown
Here is some text, this word is **bold** and this word is *italicized*.
```

## Lists

To create an enumerated list:

```markdown
1. Here is a list
2. The order does matter
3. So I use numbers
```

To create an itemized list:

```markdown
- Here is a list
- The order does not matter
- So I just use dashes
```

## Hyperlinks

Here is how to create a hyperlink:

```markdown
Here is the [course site for the rsd workshop](https://vknight.org/rsd/).
```

## Including code

You can include inline code:

```
Here is how to print hello world in python `print("hello world")`.
```

You can also include a big block of displayed code, by writing an indented
block:

```
This is how to print hello world in python:

    print("hello world")
```

## Rendering markdown

To view your markdown as html:

- View your markdown file on github (it automatically renders markdown).
- Use code to render markdown (for example python has a library that will read
  markdown and write html).
- Use your editors: many editors have plugins to view rendered markdown.
- Don't :) Markdown is designed to be consistent and easy to read so for some
  things you might not need to render it at all.
