"""
Script to build the website.

All source files are in the `src` directory and used to build static html here.
"""
import collections
import pathlib

import jinja2
import markdown

ROOT = "rsd"
Chapter = collections.namedtuple("chapter", ["dir", "title"])

def get_id(path):
    """
    Return the id of a file

    If the file is `01-introduction.md` this will return `01`
    """
    stem = path.stem
    try:
        return stem[:stem.index('-')]
    except ValueError:
        stem = stem.lower()
        stem = stem.replace(" ", "-")
        stem = stem.replace(",", "")
        return stem

def get_name(path):
    """
    Return the name of a file

    If the file is `01-introduction.md` this will return `Introduction`.
    """
    stem = path.stem
    try:
        return stem[stem.index('-'):].replace('-', ' ').title()
    except ValueError:
        return stem.replace('-', ' ').title()


def render_template(template_file, template_vars, output_path, ROOT=ROOT):
    """
    Render a jinja2 template
    """
    templateLoader = jinja2.FileSystemLoader(searchpath="./src/templates/")
    template_env = jinja2.Environment(loader=templateLoader)
    template = template_env.get_template(template_file)
    if "root" not in template_vars:
        template_vars["root"] = ROOT
    output_path.write_text(template.render(template_vars))

def obtain_html(path, ROOT=ROOT):
    """
    Convert a markdown file to html
    """
    md = path.read_text()
    md = md.replace("{{root}}", "/" + ROOT)
    return markdown.markdown(md, extensions=['markdown.extensions.fenced_code'])

def make_index(src, out):
    """
    Write the `index.html` file in root of `out`
    """
    content = obtain_html(path=src / "index.md")
    render_template(template_file="home.html",
                    template_vars={"content": content},
                    output_path=out / "index.html")

def make_chapters(src, out, title="Chapters"):
    """
    Write all the chapters to `out`/chapters
    """

    pathlib.Path(out).mkdir(exist_ok=True)
    chapters = []
    for path in sorted(src.glob("*md")):
        p = pathlib.Path(out / get_id(path))
        p.mkdir(exist_ok=True)
        content = obtain_html(path=path)
        render_template(template_file="content.html",
                        template_vars={"content": content},
                        output_path=p / "index.html")

        chapters.append(Chapter(str(p), get_name(path)))

    render_template(template_file="list.html",
                    template_vars={"list_name": title,
                                   "list": chapters},
                    output_path = out / "index.html")


if __name__ == "__main__":
    src = pathlib.Path("./src")
    out = pathlib.Path(".")

    make_index(src=src, out=out)
    make_chapters(src=src / "chs", out=out / "chapters")
    make_chapters(src=src / "xtr", out=out / "extras",
                  title="Extras")
    make_chapters(src=src / "participants", out=out / "participants",
                  title="Participants")
