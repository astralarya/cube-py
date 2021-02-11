import click
from pathlib import Path

from mtg_cube.io import mtgo_csv
from mtg_cube.format import sealed


@click.command()
@click.argument("input_", type=click.File("r"))
@click.option("--output", "-o", type=click.Path())
@click.option("--sealed-size", type=int, default=90)
def main(input_, output, sealed_size):
    cards = mtgo_csv.read(input_)
    pools = sealed.run(cards, sealed_size)
    outpath = Path(output if output is not None else input_.name)
    for idx, pool in enumerate(pools):
        with outpath.with_suffix(f".{idx}{outpath.suffix}").open("w") as outfile:
            mtgo_csv.write(outfile, pool)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
