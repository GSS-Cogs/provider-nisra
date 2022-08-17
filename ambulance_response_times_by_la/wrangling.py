from pathlib import Path
import click
import pandas as pd 

def wrangle(input: Path)->pd.DataFrame():
    df = pd.read_csv(input)
    #00:07:22
    df["VALUE"] = int(df["VALUE"][0:1])*60 + int(df["VALUE"][3:4]) + int(df.iloc["VALUE"][6:8])/60

    #df['VALUE'].apply(lambda x: x...)

    return df

if __name__ == '__main__':
    wrangle(Path("ARTLGD.20220816T100828.csv"))

