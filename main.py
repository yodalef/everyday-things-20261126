LINE1 = "Wi-Fi is like office gossip: the farther it travels from the source, the weaker and stranger it gets, until the basement swears it never existed."
LINE2 = "Honestly, both cut out at the exact moment you need them most, and everyone just nods, as if that were a law of physics."


def validated_text() -> str:
    text = LINE1.strip() + "\n" + LINE2.strip()
    assert text.count("\n") == 1, "entry must be exactly two lines"
    assert 1 <= len(text) <= 400, f"two lines must total 1-400 characters, got {len(text)}"
    return text


def main() -> None:
    import os
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validated_text() + "\n")
    print(validated_text())


if __name__ == "__main__":
    main()
