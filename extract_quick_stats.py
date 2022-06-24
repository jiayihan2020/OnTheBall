import pandas as pd
import os
import json
import datetime

working_directory = "./"
input_csv = "SIT Diary Tri 3 (LTLB only)_June 23, 2022_21.00.csv"

omit_data = [
    "SIT999",
    "SIT057",
]  # Omitted "SIT999" due to it being a test run. The rest is omitted due to a change in actiwatch.


def opening_sleep_diary(sleep_diary_location):
    """Clean up the column headers to produce a human readable/friendly format

    Returns: modified pandas dataframe
    """
    df = pd.read_csv(sleep_diary_location, index_col=False, skiprows=1)
    df.drop(index=0, inplace=True)
    df.columns = df.columns.str.replace("\n", "")
    df.columns = df.columns.str.replace(r"Qualtrics\.Survey.*", "", regex=True)
    df.columns = df.columns.str.strip()
    df = df.rename(columns={"Subject Code (e.g. SITXXX)": "Subject"})
    df["Subject"] = df["Subject"].str.upper()
    df.drop(columns=df.columns[0:17], axis=1, inplace=True)
    pd.set_option("display.max_columns", None)

    return df


def extract_count():

    df = opening_sleep_diary(working_directory + input_csv)
    counted = df["Subject"].value_counts()
    counted.to_json("extracted_stats.json", indent=4)
    with open("extracted_stats.json", "r+") as json_file:
        loading_json = json.load(json_file)
        unique_participants = len(loading_json) - len(omit_data)
        total_actual_responses = 0

        for k, v in loading_json.items():
            if k != "SIT999":
                total_actual_responses += int(v)
        combined_stats = f"""No. of unique participants: {unique_participants}
        Total number of actual responses: {total_actual_responses}"""
        json.dump(json.dumps(combined_stats), json_file)


def threshold():
    """Check students if they have keyed in for last three days."""
    df = opening_sleep_diary(working_directory + input_csv)
    return df


threshold()
