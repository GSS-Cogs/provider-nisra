from pathlib import Path
import click
import pandas as pd 

@click.command()
@click.argument('--input', type=click.Path, help='File to wrangle')
def wrangle(input: Path)->None:
    df = pd.read_csv(input)
    #00:07:22
    df['VALUE'].str.split(':').apply(lambda x: (int(x[0]) * 60) + int(x[1])+(int(x[2])/60))
    df.to_csv("output.csv", index=False)
    return 

if __name__ == '__main__':
    wrangle()

