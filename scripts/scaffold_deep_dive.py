import argparse
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scaffold a deep-dive markdown file with standard navigation/script sections."
    )
    parser.add_argument("--category", required=True, help="Category slug, e.g. compose")
    parser.add_argument("--category-title", help="Display title for back link, e.g. Compose")
    parser.add_argument("--topic-slug", required=True, help="Topic slug, e.g. recomposition-and-skip-optimization")
    parser.add_argument("--topic-title", required=True, help="Topic display title, e.g. Recomposition and Skip Optimization")
    parser.add_argument("--output", help="Optional explicit output path")
    parser.add_argument("--force", action="store_true", help="Overwrite output file if it exists")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    root = Path(__file__).resolve().parent.parent
    template_dir = root / "templates"
    output_path = (
        Path(args.output)
        if args.output
        else root / "docs" / "deep-dives" / args.category / f"{args.topic_slug}.md"
    )

    if output_path.exists() and not args.force:
        raise SystemExit(f"Output already exists: {output_path}\nUse --force to overwrite.")

    category_title = args.category_title or args.category.replace("-", " ").title()

    env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template("deep-dive.md.j2")

    rendered = template.render(
        category_slug=args.category,
        category_title=category_title,
        topic_title=args.topic_title,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")

    print(f"Created: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

