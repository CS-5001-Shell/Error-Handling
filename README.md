# Practice with Error Handling

This lab assignment requires the following concepts:
- Error Handling
- File Input

For this assignment, you will complete a gradebook program that reads data from a file,
builds a data structure, and displays the contents. 

The file *grades.txt* provides an example of the file you will need to process.

You will complete the following two functions. You may add additional functions.
Make sure to carefully read the docstrings to ensure that you handle all errors
as expected by the test cases.

```python
def read_grades_file(filename: str) -> list[str] | list[list[float]]:
    """
    Takes as a parameter a file name containing student grades and builds a data
    structure of names and scores.
    The file will have one line per student. Each line will be comma separated
    with the following information:
    <name>, <score1>, <score2>, <score3>, <score4>, <score5>

    The return value of the function will be a list of names and list of list of
    scores. Example:
    File:
    Student1, 65, 87, 98, 87.5, 90
    Student2, 99, 82.5, 98.25, 94, 80
    Result:
    ['Student1', 'Student2']
    [[65, 87, 98, 87.5, 90], [99, 82.5, 98.25, 94, 80]]

    If the file is not found, the function will return None.

    A row will be skipped and not added to the return value if it does not
    contain exactly one name and five scores.
    A row will be skipped if any of the five scores is not a floating point number.
    
    Parameters:
      filename (str): location of the file containing student data
    Returns:
      list[str]: student names; the first item in each row
      list[list[float]]: scores; the remaining items in each row in floating
      point format
    
    """
    pass

def display_averages(names: list[str], grades: list[list[float]]):
    """
    Displays the average score for each student given a list of student names
    and a list of scores for each student.

    Expected output:
    <Name>: <average score:
    Example:
    Pari: 91.0
    Igor: 88.55
    Giovanni: 90.45

    Parameters:
      names (list[str]): a list of strings representing names
      grades (list[list[float]]): a list of lists of floats representing the
      scores for each student
    Return:
      None
    Raises:
      ValueError: raised if the length of the names list does not match the
      length of the grades list.
    """
    pass
```      

## Assignment Submission

To earn credit for this assignment you must commit all of your changes to your GitHub repository prior to the deadline. It is strongly recommended that you commit your changes regularly. Do not wait until you complete all parts of the assignment to upload your (partial) solution.

Step 1 - *Stage Changes*: Select the Source Control icon in the VSCode left menu. In the Changes section, click the + to *Stage All Changes*.

Step 2 - Commit Message: In the text box that says Message enter a meaningful message that describes the change you just completed.

Step 3 - *Commit & Push*: Select the down arrow in the blue box that says Commit. Choose *Commit & Push*.

Step 4 - Verify: Visit the repository on GitHub to confirm that your changes were uploaded successfully
