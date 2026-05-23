import pandas as pd
from glob import glob

files = glob(
    "data/**/*.csv",
    recursive=True
)

frames=[]

for file in files:

    try:

        df=pd.read_csv(file)

        df["source"]=file

        frames.append(df)

        print(
            "Loaded:",
            file
        )

    except Exception as e:

        print(
            "Skipped:",
            file
        )

merged=pd.concat(
    frames,
    ignore_index=True,
    sort=False
)

merged.to_csv(
    "data/merged/agriculture_master.csv",
    index=False
)

print(
    "Rows:",
    len(merged)
)

print(
    "Done"
)