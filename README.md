# Uncommon Exception Handling Error in Python

This repository demonstrates a subtle error in Python related to exception handling. The `function_with_uncommon_error` function attempts to handle various exceptions, such as `ZeroDivisionError` and `TypeError`. However, it does not explicitly handle all possible exceptions that might occur when performing a division operation, leading to a less informative error message that may be difficult to debug.

The `bug.py` file contains the code with the error. The `bugSolution.py` file provides a corrected version that addresses the issue by adding a more comprehensive `except` block.