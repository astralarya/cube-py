import click
import sys

from mtg_cube.io import mtgo_csv


@click.command()
@click.argument("input", type=click.File("r"))
def main(input):
    cards = mtgo_csv.read(input)
    mtgo_csv.write(sys.stdout, cards)


if __name__ == "__main__":
    main()
