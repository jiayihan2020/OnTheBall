import pandas as pd
import glob
import os
import json
import datetime

working_directory = "./"
input_csv = "SIT Diary Tri 3*.csv"
all_participants = [
    "SIT049",
    "SIT051",
    "SIT054",
    "SIT055",
    "SIT057",
    "SIT061",
    "SIT059",
    "SIT064",
    "SIT066",
    "SIT068",
    "SIT072",
    "SIT073",
    "SIT074",
    "SIT075",
    "SIT076",
    "SIT077",
]

omit_data = [
    "SIT999",
    "SIT055",
]  # Omitted "SIT999" due to it being a test run. The rest is omitted due to a change in actiwatch.

non_omitted = [approve for approve in all_participants if approve not in omit_data]


def opening_sleep_diary(sleep_diary_location):
    """Clean up the column headers to produce a human readable/friendly format

    Returns: modified pandas dataframe
    """
    csv_file = glob.glob(os.path.join(working_directory, sleep_diary_location))[-1]
    print(f"Opening {csv_file}...\n")
    df = pd.read_csv(csv_file, index_col=False, skiprows=1)
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

    df = opening_sleep_diary(input_csv)
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
    df = opening_sleep_diary(input_csv)
    df.drop(columns=df.columns[2:], inplace=True)
    df = df.rename(columns={f"{df.columns[1]}": "Bedtime Date"})
    df.sort_values(by=["Subject", "Bedtime Date"], inplace=True)
    df["Bedtime Date"] = pd.to_datetime(df["Bedtime Date"], format="%d-%m-%Y").dt.date
    today_date = datetime.datetime.today().date()
    three_days_before = today_date - datetime.timedelta(days=3)
    df = df.loc[df["Bedtime Date"].between(three_days_before, today_date)]

    got_balls = []
    for got_ball in df["Subject"]:
        if got_ball not in got_balls:
            got_balls.append(got_ball)
    no_balls = [no_ball for no_ball in non_omitted if no_ball not in got_balls]
    with open(
        f"Not playing ball {today_date.strftime('%d-%m-%Y')}.txt", "w", encoding="utf-8"
    ) as text_file:
        text_file.write(f"Report generated on {today_date.strftime('%d-%m-%Y')}\n")
        for student in no_balls:
            text_file.write(student + "\n")

    return df


threshold()
