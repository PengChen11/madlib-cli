# Lab: File IO and Exceptions
[Link to python file](madlib_cli/madlib.py)

## Overview
In this lab assignment you will be creating a command line application which takes advantage of Python’s built in capabilities for reading and writing files.

## Feature Tasks and Requirements
- Create a file called ```madlib.py``` at root of **madlib_cli** folder, which will contain all of the Python code that you will write relating to your Madlib game.
- Create a file called ```test_madlib.py``` in root of **tests** folder which will be used to test your executable command line script.
- Keeping in mind the concept of [Single Responsibility Principle](https://en.wikipedia.org/wiki/Single_responsibility_principle), build a command line tool which will perform the following:
    - Print a welcome message to the user, explaining the Madlib process and command line interactions
    - Read a template Madlib file ([Example](https://codefellows.github.io/code-401-python-guide/curriculum/class-03/lab/assets/sample_template.txt)), and parse that file into usable parts.
        - You need to decide what components of this file are useful, and how to break those useful pieces apart
    - Once you know what parts of the template need user input, such as **Adjective**, prompt the user to submit a series of words to fit each of the required components of the Madlib template.
    - With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
    - After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
    - Write the completed template ([Example](https://codefellows.github.io/code-401-python-guide/curriculum/class-03/lab/assets/sample_output.txt))to a new file on your file system (in the repo).

## Testing Requirements
You are NOT required to test terminal input/output, AKA print and input functions.

However you are expected to meaningful tests for your application.

So how can we skip testing print and output functionality while still proceeding with confidence?

The resolution to that dilemma is to break down your code so that it is more easily testable.

  - Create and test a **read_template** function that takes in a path to text file and returns a stripped string of the file’s contents.
  - Create and test a **merge** function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.

## Distributors
Peng Chen

## License requirement
None
