A simple python command line application that collects student grades, calculates summary statistics, determines overall letter grades, and evaluates pass/fail status.

FEATURES
-Prompts user to enter the number of grades and accepts individual floating point values.
-Computes the mean rounded to two decimal places.
-Uses a standard scale letter grade assingment:
  -A: 90 and above
  -B: 80-89.99
  -C: 70-79.99
  -D: 60-69.99
  -F: Below 60
-Identifies the highest and lowest scores entered
-Determines whether the average meets the passing threshold

REQUIREMENTS
-Python 3.x (no external libraries required)

POSSIBLE IMPROVEMENTS
-Add input validation for if a user inputs letters or symbols 
-Prevent division by zero and empty lists
-Use f strings for cleaner print statements
-Simplify passing logic