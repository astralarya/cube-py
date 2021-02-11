from typing import Any, List
import random


def run(cards: List[Any], size: int):
    random.shuffle(cards)
    pools = [it for it in chunk(cards, size) if len(it) == size]
    return pools


def chunk(input: List[Any], size: int):
    for i in range(0, len(input), size):
        yield input[i : i + size]
