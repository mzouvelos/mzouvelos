"""
Inspired by the README of the author of rich:
    https://github.com/willmcgugan/willmcgugan
"""

from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=150)

tree = Tree("😎 [link=https://mzouvelos.github.io/]Michalis Zouvelos", guide_style="bold cyan")
packages_tree = tree.add("📊 Honing Skills")
packages_tree.add("R / Shiny")
packages_tree.add("Docker")
packages_tree.add("SQL")
packages_tree.add("Git")
packages_tree.add("Cloud Technology")
articles_tree = tree.add("📚 Education")
articles_tree.add("MSc Information Management & Business Intelligence")
articles_tree.add("MEng Engineering")


about = """\
An Engineer turned to data science. Interest in technology, machine learning and any data related activity that generates value and insights. I enjoy writing data posts and notebooks, mainly using R.

You can find me on [bold link=https://www.linkedin.com/in/michalis-zouvelos-8912371b6/]LinkedIn[/].

Feel free to contact me!"""


panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hello 👋 I am Michalis", width=60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)