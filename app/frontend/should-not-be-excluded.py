"""Utility helpers for small math exercises used by the dummy app."""

from __future__ import annotations

from functools import lru_cache
from typing import Iterable, List


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using memoization for speed."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def moving_average(samples: Iterable[float], window: int) -> List[float]:
    """Compute a simple moving average across the iterable of samples."""
    if window <= 0:
        raise ValueError("window must be positive")

    values = list(samples)
    if not values:
        return []
    if window > len(values):
        raise ValueError("window cannot exceed sample length")

    averages: List[float] = []
    window_sum = sum(values[:window])
    averages.append(window_sum / window)

    for idx in range(window, len(values)):
        window_sum += values[idx] - values[idx - window]
        averages.append(window_sum / window)

    return averages


def normalize(scores: Iterable[float]) -> List[float]:
    """Scale scores to the range [0, 1]."""
    values = list(scores)
    if not values:
        return []
    min_val = min(values)
    max_val = max(values)
    if min_val == max_val:
        return [0.0 for _ in values]
    return [(value - min_val) / (max_val - min_val) for value in values]

