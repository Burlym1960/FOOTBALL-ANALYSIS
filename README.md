# Football Analysis: International Football Results (1872–2024)

This project analyzes international football match results using the Kaggle dataset: [International Football Results (1872–2024)](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017).

## Assignment Overview

You will perform data exploration, goals analysis, match results analysis, and visualizations using Python and pandas. All code and explanations are provided in `analysis.ipynb` and `analysis.py`.

### Dataset
- **File:** `data/results.csv`
- **Source:** [Kaggle - International Football Results](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017)

## Steps Performed

### 1. Load the CSV
```python
import pandas as pd
df = pd.read_csv("data/results.csv")
df.head()
```

### 2. Basic Exploration
- **How many matches are in the dataset?**
- **What is the earliest and latest year in the data?**
- **How many unique countries are there?**
- **Which team appears most frequently as home team?**

### 3. Goals Analysis
- **Create total goals column:**
  ```python
  df["total_goals"] = df["home_score"] + df["away_score"]
  ```
- **Questions:**
    - What is the average number of goals per match?
    - What is the highest scoring match?
    - Are more goals scored at home or away?
    - What is the most common total goals value?

### 4. Match Results
- **Create match outcome column:**
  ```python
  def match_result(row):
      if row["home_score"] > row["away_score"]:
          return "Home Win"
      elif row["home_score"] < row["away_score"]:
          return "Away Win"
      else:
          return "Draw"
  df["result"] = df.apply(match_result, axis=1)
  ```
- **Questions:**
    - What percentage of matches are home wins?
    - Does home advantage exist?
    - Which country has the most wins historically?

### 5. Visualization
- **Histogram of goals**
- **Bar chart of match outcomes**
- **Top 10 teams by total wins**

Example:
```python
import matplotlib.pyplot as plt

df["total_goals"].hist(bins=15)
plt.title("Distribution of Goals Per Match")
plt.xlabel("Goals per Match")
plt.ylabel("Frequency")
plt.show()
```

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the analysis notebook:**
   - Open `analysis.ipynb` in Jupyter or VS Code and run all cells.
   - Or, run the script:
     ```bash
     python analysis.py
     ```

## Requirements
- Python 3.7+
- pandas
- matplotlib
- (Optional) Jupyter Notebook

## File Structure
- `analysis.ipynb` — Main analysis notebook (recommended)
- `analysis.py` — Script version of the analysis
- `requirements.txt` — Python dependencies
- `data/results.csv` — Football results dataset

## Notes
- All code is commented and includes markdown explanations.
- Visualizations are generated and displayed inline.
- Answers to all assignment questions are provided in the notebook/script.

---

**Author:** bullim agana
