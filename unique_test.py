import os
import pandas as pd

dir_path = os.path.join(os.getcwd(), "data")
filenames = list(next(os.walk(dir_path), (None, None, []))[2])
for filename in filenames:
    if filename.endswith(".csv"):
        df = pd.read_csv(os.path.join(dir_path, filename))
        if "gdrive_file_id" in df.columns:
            total_record_count = len(df)
            unique_record_count = len(df["gdrive_file_id"].unique())
            print(filename.center(50, "-"))
            if total_record_count != unique_record_count:
                print(f"total records: {total_record_count}")
                print(f"unique records: {unique_record_count}")
            else:
                print("OK")
