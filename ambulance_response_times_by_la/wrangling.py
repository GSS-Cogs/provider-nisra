import click
import pandas as pd


@click.command()
@click.argument("input", type=click.Path(exists=True))
@click.argument("output", type=click.Path())
def wrangle(input: click.Path, output: click.Path) -> None:
    df = pd.read_csv(input)
    # 00:07:22
    df["VALUE"] = (
        df["VALUE"]
        .str.split(":")
        .apply(lambda x: (int(x[0]) * 60) + int(x[1]) + (int(x[2]) / 60))
        .round(decimals=2)
    )
    df.to_csv(output, index=False)
    return


if __name__ == "__main__":
    wrangle()
