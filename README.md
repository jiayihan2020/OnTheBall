# OnTheBall

## About OnTheBall

OnTheBall provides a quick statistics from the Qualtrics csv output on how many students have responded to the Sleep Diary questionnaire and their total responses recorded. OnTheBall also detects which students have not entered their entry in the questionnaire for more than three days so that a follow up reminder can be sent to these students.

## Pre-requisites

- Python 3.7+
  - Pandas library
  - numpy library
- raw csv file containing students' responses obtained from Qualtrics.
- Supported Operating Systems:
  - Windows
  - Linux
  - macOS (not tested)

## Features

OnTheBall has two features which users can choose to run:

1) Extract Count
   - This option obtains the number of respondents in the questionnaires (excluding those who have changed their ActiWatches), and the total responses recorded, both for each students and the Grand Total recorded, and then exports them as a json file.
2) Threshold
   - This option detects if there are any students who do not enter their data for more than three days. A text file is generated containing the subject code of the students in question so that a follow up reminder can be sent to them.

## How to use

Ensure that the csv file and `on_the_ball.py` resides in the same directory. You may edit the on_the_ball.py by using a text editor such as Notepad, VSCode, or Python's built in IDLE to edit the filepaths as required.

### Windows

For Windows users, ensure that the `on_the_ball.bat`, `on_the_ball.py`, and the Sleep Diary csv from Qualtrics are located in the same directory.

Double click on `on_the_ball.bat`. A command prompt containing a menu prompting you to choose which feature(s) you want to use should appear. Follow the instructions on the menu.

### macOS and Linux

For macOS and Linux users, ensure that `on_the_ball.py` and and the Sleep Diary csv from Qualtrics are located in the same directory.

Launch the terminal and type in the following command:

```bash
./on_the_ball.py
```

A menu prompting you to choose which feature(s) you want to use should appear. Follow the instructions on the terminal's screen.
