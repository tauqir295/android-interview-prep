import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

DATA_DIR = Path("data")
DOCS_DIR = Path("docs/generated")
TEMPLATE_DIR = Path("templates")

DOCS_DIR.mkdir(parents=True, exist_ok=True)

env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    trim_blocks=True,
    lstrip_blocks=True
)

template = env.get_template("category.md.j2")

for yaml_file in DATA_DIR.glob("*.yaml"):

    with open(yaml_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    category_name = yaml_file.stem

    rendered = template.render(
        category_title=category_name.replace("-", " ").title(),
        questions=data.get("questions", [])
    )

    output_file = DOCS_DIR / f"{category_name}.md"

    with open(output_file, "w", encoding="utf-8") as out:
        out.write(rendered)

    print(f"Generated: {output_file}")