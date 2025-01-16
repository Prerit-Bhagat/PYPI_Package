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

To install the package, use:

pip install TOPSIS_Prerit_102217030


## Usage
Run the TOPSIS analysis using the command-line interface:

topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>

Example
Suppose you have a CSV file data.csv containing a decision matrix where:

The first column is the identifier for alternatives.
The subsequent columns contain numeric data for each criterion.

If you want to apply TOPSIS with weights [1, 1, 1, 2] and impacts [+, +, -, +], use:
topsis data.csv "1,1,1,2" "+,+,-,+" result.csv

This will generate a result file result.csv with the calculated TOPSIS scores and rankings.
<!-- ## Functions -->
<!-- ### Funtion(parameter) -->

