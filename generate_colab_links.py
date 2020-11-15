from pathlib import Path


REPO = Path("/Users/dkapitan/git/jads/intro-to-python")
OUTPUT = REPO /"colab-links.md"
COLAB_URL = "https://colab.research.google.com/github/jads-nl/intro-to-python/blob/main/"


def generate_colab_links(file_):
    """Generates Markdown with Colab links.md

        Args:
            - file_: file to write to
    """
    notebooks = sorted(Path(REPO).glob("**/*.ipynb"))
    chapters = sorted(list(set([notebook.parts[-2:-1][0] for notebook in notebooks])))
    for chapter in chapters:
        file_.write(f"## {chapter}\n\n")
        for notebook in sorted((REPO / chapter).glob("*.ipynb")):
            filename = Path(*notebook.parts[-2:])
            file_.write("".join([f"  - [{filename.stem}](", COLAB_URL, f"{filename})\n"]))
        file_.write("\n")


if __name__ == '__main__':
    with open(OUTPUT, "w") as file_:
        file_.write("# Index of notebooks with Python exercises.\n\n \
        Please click on any of the notebook links to open it directly in Google Colab\n")
        generate_colab_links(file_)