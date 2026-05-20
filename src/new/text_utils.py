"""Assorted helpers for simple text analytics."""

from __future__ import annotations

from collections import Counter
from typing import Dict, Iterable, List, Tuple


def word_count(text: str) -> Dict[str, int]:
    """Return a dict containing the frequency of each lowercase word."""
    words = [
        token.lower()
        for token in text.split()
        if token.strip()
    ]
    return dict(Counter(words))


def most_common_words(text: str, top_n: int = 5) -> List[Tuple[str, int]]:
    """Return the top N most frequent words."""
    if top_n <= 0:
        raise ValueError("top_n must be positive")
    counts = Counter(word_count(text))
    return counts.most_common(top_n)


def unique_words(texts: Iterable[str]) -> List[str]:
    """Return a sorted list of unique words from the provided texts."""
    seen = {word.lower() for text in texts for word in text.split() if word.strip()}
    return sorted(seen)

