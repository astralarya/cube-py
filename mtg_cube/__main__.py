import click
from pathlib import Path

from mtg_cube.io import mtgo_csv


@click.command()
@click.argument("input", type=click.File("r"))
@click.option("--output", "-o", type=click.Path(), default="out.csv")
def main(input, output):
    cards = mtgo_csv.read(input)
    pools = [cards]
    outpath = Path(output)
    for idx, pool in enumerate(pools):
        with outpath.with_suffix(f".{idx}{outpath.suffix}").open("w") as outfile:
            mtgo_csv.write(outfile, pool)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
