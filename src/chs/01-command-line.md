# The command line

When using a computer we are mostly used to using a _graphical user interface_.
This is made up of icons and windows and is mainly interacted with using a
mouse. This is often referred to as a _point and click_ approach.

One of the downsides of a _point and click_ approach in the scope of
reproducible research is that giving instructions is often difficult and they
can be ambiguous.

Another approach is to use the command line. This is a small window in to which
we type commands and lets us give precise (reproducible) commands to the
computer.

## Identify and open your command line interface.

First, it is important to note that this will now differ (but not substantially)
depending on whether or not you're on a Windows machine:

- Windows: we will choose to use **Anaconda Prompt** (which was installed on
  your machine when you installed Anaconda).
- nix (another way to describe Mac OS and/or Linux machines): we will use the
  system **terminal**.


## Finding your current location

Let us first find out which directory (folder) we are currently in:

**Windows**

```bash
cd
```

This stands for "current directory".

**nix**

```bash
pwd
```

This stands for "present working directory"

1. Type this command in
2. Press `Enter`

It should list where you are currently located in your
command line interface.

## Seeing what is in your current location

To view the contents of the current directory:

**Windows**

```bash
dir
```

This stands for "directory".

**nix**

```bash
ls
```

This stands for "list"

1. Type this command in.
2. Press `Enter`

You should see a list of the various files and directory in your current
directory.

Open your current directory in a graphical user interface and compare.

## Creating a directory

To create a directory:

```bash
mkdir <directory_name>
```

Experiment with creating a directory for this workshop:

```bash
mkdir rsd-workshop
```

If your directory structure looked like this:

```bash
|--- home/
     |--- research
     |--- photos
```

It will now look something like:

```bash
|--- home/
     |--- research
     |--- photos
     |--- rsd-workshop
```

## Moving to another location

On both Windows and nix if you want to enter a directory that is in your current
diractory type:

```bash
cd <directory>
```

To move in to the `rsd-workshop` directory we created previously:

```bash
cd rsd-workshop
```

As an exercise, move in to that directory and create two further directories:

```
|--- rsd-workshop
     |--- tex
     |--- src

```

These two directories stand for LaTeX (`tex`) and source code (`src`): we will
use these later on in the course.

If you now wanted to go back to the "parent" directory:

```bash
cd ..
```

Where `..` is short hand for a previous directory.

Experiment with these, in combination with the command to find your current
location as well as the command to list the contents of your directory.

## Copying files

To copy a file:

**Windows**

```bash
copy <file> <new_file_directory_and_name>
```

**nix**

```bash
cp <file> <new_file_directory_and_name>
```

## Moving/renaming files

To move a file:

**Windows**

```bash
move <file> <new_file_directory_and_name>
```

**nix**

```bash
mv <file> <new_file_directory_and_name>
```

Note that if you want to rename a file you can do this by passing the new name
in the same directory.

**WARNING** When using the command line interface you will not be prompted for
confirmation if `move`/`mv` were to overwrite another file. Be careful.

## Deleting files

To delete a file:

**Windows**

```bash
del <file>
```

**nix**

```bash
rm <file>
```

## Copying and removing directories

To copy a directory:

**Windows**

```
xcopy <dir> <target>
```

**nix**

```
cp -r <dir> <target>
```

To remove a directory:

**Windows**

```
rmdir /s <dir>
```

**nix**

```
rm -r <dir>
```

# Tip: Tab completion

Most command line tools allow for command tab completion. This means you can
start typing the first few letters of a file or a directory and press tab which
will complete the rest. This is a very useful tool to ensure you don't make
mistakes when typing.

You can also use the up/down arrow keys to cycle through your previous commands.
This also helps avoid repetitive typing.
