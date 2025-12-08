"""Generate a quick demo report that ties the helper modules together."""

from __future__ import annotations

from typing import List

from math_utils import moving_average, normalize
from text_utils import most_common_words


def build_demo_report() -> List[str]:
    """Create a small textual report using the helper modules."""
    sentences = [
        "This dummy project keeps growing with helpful examples",
        "Python makes it easy to mix math helpers with text analytics",
        "Dummy data is great for demo reports",
    ]

    all_text = " ".join(sentences)
    word_summary = most_common_words(all_text, top_n=3)

    sample_scores = [3, 7, 4, 9, 6, 2]
    normalized = normalize(sample_scores)
    averages = moving_average(sample_scores, window=3)

    report_lines = [
        "Top words:",
        *(f"  - {word}: {count}" for word, count in word_summary),
        "Normalized scores:",
        *(f"  - {score:.2f}" for score in normalized),
        "Moving average (window=3):",
        *(f"  - {score:.2f}" for score in averages),
    ]
    return report_lines


def print_demo_report() -> None:
    """Print the demo report to stdout."""
    for line in build_demo_report():
        print(line)


if __name__ == "__main__":
    print_demo_report()

