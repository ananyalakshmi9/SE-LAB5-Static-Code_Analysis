# Lab 5: Static Code Analysis

This repository contains the work for a lab focused on improving Python code quality, security, and style using Pylint, Bandit, and Flake8.

* **Final Code:** [`inventory_system.py`](./inventory_system.py)

## Final Analysis Reports

The final, cleaned code achieves a **10/10** from Pylint and has **0 issues** identified by Bandit and Flake8.

bandit_report:
<img width="1563" height="901" alt="Screenshot 2025-10-27 122744" src="https://github.com/user-attachments/assets/2ec99041-efa9-413b-bff2-59b6237db22e" />

flake8_report:
<img width="1491" height="908" alt="Screenshot 2025-10-27 122847" src="https://github.com/user-attachments/assets/12bd9d34-85fb-4927-bd59-77a77fe2e9e4" />

pylint_report:
<img width="1503" height="913" alt="Screenshot 2025-10-27 122915" src="https://github.com/user-attachments/assets/fc2e59d5-35aa-47a7-8521-7694afcb8cf2" />


## Issue Log & Fixes

The following tables document the process of identifying and fixing all issues reported by the static analysis tools.

### 1. Cross-Referenced Issues (Reported by Multiple Tools)

| **Issue** | **Type** | **Line(s)** | **Description** | **Fix Approach** |
| :--- | :--- | :--- | :--- | :--- |
| **Bare Except & Pass** | Bug / Security | 19 | **Pylint (W0702), Flake8 (E722), Bandit (B110).** Catches all exceptions (even system-exiting ones) and silently ignores the error. | Replace `except:` with a specific exception (e.g., `except KeyError:`) and log the error instead of using `pass`. |
| **Insecure `eval` Use** | Security | 59 | **Pylint (W0123), Bandit (B307).** The `eval()` function is a major security risk as it can execute arbitrary code. | Remove the `eval()` call entirely. |
| **Unused Import** | Style / Cleanup | 2, \~72 | **Pylint (W0611), Flake8 (F401).** The `logging` and `datetime` modules were imported but not used (or were made redundant). | Removed the `import logging` and `from datetime import datetime` lines. |
| **Trailing Newlines** | Style | End | **Pylint (C0305), Flake8 (W391/W292).** The tools reported an incorrect number of blank lines at the end of the file. | Fixed by ensuring there is **exactly one** blank newline at the end of the script. |

### 2. Single-Tool Issues

| **Issue** | **Type** | **Line(s)** | **Description** | **Fix Approach** |
| :--- | :--- | :--- | :--- | :--- |
| **Mutable Default Arg** | Bug | 8 | **Pylint (W0102).** Using `[]` as a default argument creates one list that is shared across all calls to the function. | Removed the parameter and replaced the functionality with a proper logging setup. |
| **Invalid Naming** | Style | 8, 14, 22+ | **Pylint (C0103).** Function names like `addItem` did not conform to the `snake_case` style. | Renamed all functions to use `snake_case` (e.g., `add_item`, `load_data`). |
| **Missing Docstrings** | Style / Docs | 1, 8, 14+ | **Pylint (C0114, C0116).** The module and all functions were missing docstrings. | Added a module-level docstring and docstrings to every function. |
| **Improper File Handling** | Bug / Style | 26, 32 | **Pylint (R1732, W1514).** `open()` was used without a `with` statement or an `encoding`. | Rewrote file operations to use `with open(..., encoding="utf-8") as f:`. |
| **Lazy Logging** | Style / Performance | Multiple | **Pylint (W1203).** Pylint recommended using "lazy" %-formatting instead of f-strings for logging. | Changed all `logging.info(f"...")` calls to the `logging.info("...", var1)` format. |
| **Global Statement** | Style | \~180 | **Pylint (W0603).** Pylint discourages the use of `global`. | Kept the `global` statement as it was part of the original design, but added a `# pylint: disable=global-statement` comment to acknowledge the warning. |
| **Line Too Long** | Style | Multiple | **Flake8 (E501).** Several lines were slightly longer than the 79-character limit. | Reformatted the long logging lines to be shorter and compliant. |
