import click
import pandas as pd
from pathlib import Path


@click.command()
@click.argument("input", type=click.Path(exists=True, path_type=Path))
@click.option("--output", default=Path("./output.csv"), type=click.Path(path_type=Path))
def wrangle(input: Path(), output: Path()) -> None:
    df = pd.read_csv(input)
    # ADD MARKER COLUMN IN FOR BLANK CELLS WITIN THE VALUE COLUMN. 
    df['Marker'] = df.apply(lambda x: 'O' if pd.isnull(x['VALUE']) else '', axis=1)     
    #df.drop("UNIT", axis=1, inplace=True)
    df.to_csv(output, index=False)
    return


if __name__ == "__main__":
    wrangle()
