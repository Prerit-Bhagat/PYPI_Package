# TOPSIS Implementation

This package provides a Python implementation of the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method for multi-criteria decision analysis.

---

## Features
- **Ease of Use**: Simple and clear implementation of the TOPSIS algorithm.
- **Weighted Decision Making**: Allows users to define weights for each criterion.
- **Impact Analysis**: Accounts for both positive and negative impacts of criteria.
- **Command-Line Interface**: Execute TOPSIS directly from the terminal with input and output files.

---

## Installation

Install the package directly from PyPI:

```In Shell:
pip install Topsis-Prerit-102217030==1.0.8
```

---

## Usage

Run the TOPSIS analysis using the command-line interface:

```Command Line:
topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

### Example

Suppose you have a CSV file `data.csv` containing a decision matrix where:

- The first column is the identifier for alternatives.
- The subsequent columns contain numeric data for each criterion.

To apply TOPSIS with weights `[1, 1, 1, 2]` and impacts `[+, +, -, +]`, run:

```bash
topsis data.csv "1,1,1,2" "+,+,-,+" result.csv
```
If you get an error (topsis not recognized) then this possibly due to path of your Python Package Then Try :

![Screenshot 2025-01-19 184210](https://github.com/user-attachments/assets/72fc156b-38e7-4b05-8eee-4b5f84e595d1)

This will generate a result file `result.csv` with the calculated TOPSIS scores and rankings.

---

## Files in the Package

- `setup.py`: Contains metadata and configuration for the package.
- `README.md`: This file, providing an overview of the package.
- Additional files like `LICENSE` and `.gitignore` as needed.

---

Happy analyzing with TOPSIS!
## Note This is currently under development
