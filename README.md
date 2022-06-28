# OnTheBall

## About OnTheBall

OnTheBall provides a quick statistics from the Qualtrics csv output on how many students have responded to the Sleep Diary questionnaire and their total responses recorded. OnTheBall also detects which students have not entered their entry in the questionnaire for more than three days so that a follow up reminder can be sent to these students.

## Pre-requisites

- Python 3.7+
  - Pandas library
  - numpy library
- raw csv file containing students' responses obtained from Qualtrics.

## Features

OnTheBall has two features which users can choose to run:

1) Extract Count
   - This option obtains the number of respondents in the questionnaires (excluding those who have changed their ActiWatches), and the total responses recorded, both for each students and the Grand Total recorded, and then exports them as a json file.
2) Threshold
   - This option detects if there are any students who do not enter their data for more than three days. A text file is generated containing the subject code of the students in question so that a follow up reminder can be sent to them.

## How to use

Ensure that the csv file and `on_the_ball.py` resides in the same directory.

Open `on_the_ball.py` using Python IDLE and press `F5` on the keyboard to run the script. Choose the option that you want from the menu, and the respective output file(s) will be generated.
