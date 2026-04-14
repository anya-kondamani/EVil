import pandas as pd
'''This script filters the data files to include only records from September 2022 to February 2023. We ran this on the original 
CSV files to create new filtered versions, which are then used for the analysis and forecasting.'''
# 6 month window (September 2022 to February 2023)
start_date = pd.to_datetime("2022-09-01")
end_date = pd.to_datetime("2023-02-28")

files = ["data/duration.csv", "data/e_price.csv", "data/occupancy.csv", "data/s_price.csv", "data/volume.csv"]
for file in files:
    df = pd.read_csv(file)
    df["time"] = pd.to_datetime(df["time"], errors="coerce")
    # filter
    df_filtered = df[(df["time"] >= start_date) & (df["time"] <= end_date)]

    # overwrite original file
    df_filtered.to_csv(file, index=False)

    print(f"Processed {file}: {len(df)} -> {len(df_filtered)} rows")