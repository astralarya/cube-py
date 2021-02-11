import click
from pathlib import Path

from mtg_cube.io import mtgo_csv
from mtg_cube.format import sealed


@click.command()
@click.argument("input", type=click.File("r"))
@click.option("--output", "-o", type=click.Path(), default="out.csv")
@click.option("--sealed-size", type=int, default=90)
def main(input, output, sealed_size):
    cards = mtgo_csv.read(input)
    pools = sealed.run(cards, sealed_size)
    outpath = Path(output)
    for idx, pool in enumerate(pools):
        with outpath.with_suffix(f".{idx}{outpath.suffix}").open("w") as outfile:
            mtgo_csv.write(outfile, pool)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
