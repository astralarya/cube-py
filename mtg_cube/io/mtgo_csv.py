import csv
from typing import IO, Iterable


HEADER = [
    "Card Name",
    "Quantity",
    "ID #",
    "Rarity",
    "Set",
    "Collector #",
    "Premium",
    "Sideboarded",
    "Annotation",
]


def read(input: IO):
    data = csv.reader(input)
    header = next(data)
    cards = [row for row in data if len(row) == len(header)]
    return cards


def write(file: IO, cards: Iterable[Iterable[str]], header=HEADER):
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(cards)
