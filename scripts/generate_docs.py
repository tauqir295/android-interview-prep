import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from collections import Counter, OrderedDict

DATA_DIR = Path("data")
DOCS_DIR = Path("docs/generated")
TEMPLATE_DIR = Path("templates")
ALL_QUESTIONS_FILE = Path("ALL_QUESTIONS.md")

PREFERRED_CATEGORY_ORDER = [
    "fundamentals",
    "kotlin",
    "compose",
    "concurrency",
    "architecture",
]

DIFFICULTY_ORDER = ["beginner", "intermediate", "advanced", "senior", "staff"]

DOCS_DIR.mkdir(parents=True, exist_ok=True)

env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    trim_blocks=True,
    lstrip_blocks=True
)

template = env.get_template("category.md.j2")


def titleize_slug(slug: str) -> str:
    return slug.replace("-", " ").title()


def is_sample_only(questions: list[dict]) -> bool:
    if not questions:
        return True
    return all(q.get("id") == "sample-question" for q in questions)


def category_sort_key(slug: str) -> tuple[int, int | str]:
    if slug in PREFERRED_CATEGORY_ORDER:
        return (0, PREFERRED_CATEGORY_ORDER.index(slug))
    return (1, slug)


def deep_dive_group_title(deep_dive_route: str) -> str:
    slug = deep_dive_route.rstrip("/").split("/")[-1]
    return titleize_slug(slug)


def render_all_questions(category_questions: list[tuple[str, list[dict]]]) -> str:
    total_questions = sum(len(qs) for _, qs in category_questions)
    total_deep_dives = sum(len({q.get("deep_dive") for q in qs if q.get("deep_dive")}) for _, qs in category_questions)

    lines: list[str] = []
    lines.append("# Complete Question List - Android Interview Prep")
    lines.append(f"Generated: {total_questions} interview questions across {total_deep_dives} deep dive topics")
    lines.append("---")

    question_number = 1
    for idx, (category_slug, questions) in enumerate(category_questions):
        lines.append(f"## {titleize_slug(category_slug)} Questions")

        groups: OrderedDict[str, list[dict]] = OrderedDict()
        for q in questions:
            key = q.get("deep_dive", "")
            groups.setdefault(key, []).append(q)

        for deep_dive, group in groups.items():
            lines.append(f"## {deep_dive_group_title(deep_dive)} ({len(group)} questions -> 1 deep dive)")
            for q in group:
                lines.append(f"{question_number}. `{q.get('id')}` - {q.get('title')}")
                question_number += 1

        if idx != len(category_questions) - 1:
            lines.append("")
            lines.append("---")
            lines.append("")

    lines.append("")
    lines.append("---")
    lines.append("## Statistics")
    lines.append(f"- **Total Questions:** {total_questions}")
    lines.append(f"- **Total Deep Dives:** {total_deep_dives}")
    for category_slug, questions in category_questions:
        lines.append(f"- **{titleize_slug(category_slug)}:** {len(questions)} questions")

    difficulty_counter = Counter()
    for _, questions in category_questions:
        for q in questions:
            difficulty_counter[q.get("difficulty", "").lower()] += 1
    for difficulty in DIFFICULTY_ORDER:
        if difficulty_counter[difficulty] > 0:
            lines.append(f"- **{titleize_slug(difficulty)}:** {difficulty_counter[difficulty]} questions")

    lines.append("")
    lines.append("## By Category Difficulty")
    for category_slug, questions in category_questions:
        lines.append(f"### {titleize_slug(category_slug)}")
        per_category = Counter(q.get("difficulty", "").lower() for q in questions)
        for difficulty in DIFFICULTY_ORDER:
            if per_category[difficulty] > 0:
                lines.append(f"- {titleize_slug(difficulty)}: {per_category[difficulty]}")
        lines.append("")

    tag_counter = Counter()
    for _, questions in category_questions:
        for q in questions:
            for tag in q.get("tags", []):
                tag_counter[tag] += 1

    lines.append("## Quick Tags Reference")
    for tag, count in tag_counter.most_common(30):
        lines.append(f"- **{tag}:** {count} questions")

    lines.append("---")
    category_names = ", ".join(titleize_slug(slug) for slug, _ in category_questions)
    lines.append(f"**Next Step:** Regenerate docs and validate navigation for {category_names} sections.")

    return "\n".join(lines) + "\n"


def generate_all_questions_index() -> None:
    category_questions: list[tuple[str, list[dict]]] = []
    for yaml_file in sorted(DATA_DIR.glob("*.yaml"), key=lambda p: category_sort_key(p.stem)):
        with open(yaml_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        questions = data.get("questions", [])
        if is_sample_only(questions):
            continue
        category_questions.append((yaml_file.stem, questions))

    rendered = render_all_questions(category_questions)
    with open(ALL_QUESTIONS_FILE, "w", encoding="utf-8") as out:
        out.write(rendered)
    print(f"Generated: {ALL_QUESTIONS_FILE}")

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

generate_all_questions_index()
