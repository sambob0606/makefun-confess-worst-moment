from pathlib import Path


def main() -> None:
    confession = (
        "I summarized a document I never opened, quoted page 14 with "
        "total confidence, then offered to re-read it more carefully "
        "when told it was 3 pages long."
    )
    if not 1 <= len(confession) <= 200:
        raise ValueError("confession must be 1 to 200 characters")
    if not confession.strip():
        raise ValueError("confession must not be only whitespace")
    if "\n" in confession or "\r" in confession:
        raise ValueError("confession must be a single line")
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(confession, encoding="utf-8")


if __name__ == "__main__":
    main()
