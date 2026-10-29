# Sales Analysis System

A simple command-line Python program that records a week of daily sales and generates a summary report. Built as a beginner-friendly project to practice Python functions, loops, lists, and user input handling.

## Features

- Takes sales input for 7 days
- Calculates total weekly sales
- Calculates average daily sales
- Finds the highest and lowest sale of the week
- Prints a clean, formatted report

## Technologies Used

- Python 3.x (no external libraries required)

## How to Run

1. Make sure Python 3 is installed:
   ```bash
   python --version
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/sales-analysis-system.git
   cd sales-analysis-system
   ```
3. Run the program:
   ```bash
   python sales_analysis_system.py
   ```

## Example

**Input**

```
Enter sales for 7 days
Day 1 Sales:5000
Day 2 Sales:8000
Day 3 Sales:7000
Day 4 Sales:9000
Day 5 Sales:10000
Day 6 Sales:9000
Day 7 Sales:1100
```

**Output**

```
---Sales Analysis Report---
Daily Sales: [5000.0, 8000.0, 7000.0, 9000.0, 10000.0, 9000.0, 1100.0]
Total Weekly Sales: 49100.0
Average Daily Sales: 7014.29
Highest sale: 10000.0
Lowest sale: 1100.0
```

## Project Structure

```
sales-analysis-system/
├── sales_analysis_system.py
└── README.md
```

## Functions Overview

| Function | Purpose |
|---|---|
| `record_sales()` | Collects 7 days of sales from the user |
| `calculate_total()` | Returns the sum of all sales |
| `calculate_average()` | Returns the average daily sales |
| `find_highest_lowest()` | Returns the highest and lowest sale |
| `show_report()` | Runs everything and prints the report |

## Future Improvements

- Input validation (reject negative or non-numeric values)
- Save the report to a CSV/Excel file
- Add a chart of daily sales using Matplotlib
- Support any number of days, not just 7

## Author

**Haleema Mahmood**
BS Data Analytics, PMAS Arid Agriculture University, Rawalpindi
