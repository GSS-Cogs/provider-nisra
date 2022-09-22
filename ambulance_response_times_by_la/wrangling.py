from email.policy import default
import click
import pandas as pd
from pathlib import Path


@click.command()
@click.argument("input", type=click.Path(exists=True, path_type=Path))
@click.option("--output", default=Path("./output.csv"), type=click.Path(path_type=Path))
def wrangle(input: Path(), output: Path()) -> None:
    df = pd.read_csv(input)
    # 00:07:22
    df["VALUE"] = (
        df["VALUE"]
        .str.split(":")
        .apply(lambda x: (int(x[0]) * 3600) + (int(x[0]) * 60) + int(x[2]))
    )
    # Changed from HH:MM:SS to decimal minutes, need to drop UNIT column
    df.drop("UNIT", axis=1, inplace=True)
    df.to_csv(output, index=False)
    return


if __name__ == "__main__":
    wrangle()
