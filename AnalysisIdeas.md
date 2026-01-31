# ⚽ Serie A Data Analysis Project

A comprehensive statistical analysis of Serie A matches from 2020-2025 seasons.

---

## 📋 Table of Contents
- [Data Preprocessing](#data-preprocessing-and-cleanup)
- [Season Tables](#season-tables)
- [Expected Goals (xG) Analysis](#expected-goals-xg-analysis)
- [Statistical Tests](#statistical-tests)
- [Performance and Attendance](#performance-and-attendance)
- [Formation Analysis](#starting-formation-analysis)
- [Correlation Analysis](#correlation-analysis)
- [Regression Models](#regression-models)

---

## 🔧 Data Preprocessing and Cleanup

Data loading, cleaning, and transformation to prepare the dataset for analysis.

---

## 📊 Season Tables

### 1. Interactive Season Standings
Create interactive tables for each season showing:
- League standings after each gameweek
- Points, wins, draws, losses
- Goals scored, conceded, and goal difference
- xG for and xG against

---

## 🎯 Expected Goals (xG) Analysis

### Key Research Questions:
- ✅ Which team had the **highest xG** and scored the most goals?
- ✅ Which game had the **highest combined xG** (xG + opp_xG)?
- ✅ Which game had the **biggest difference** between xG and actual goals?
- ✅ Were there any **significant xG trends** or series?
- ✅ How have **average and median xG** changed across seasons?
- ✅ xG comparison **with and without penalties**

### Visualizations:
- 📈 Line plots: xG trends over seasons
- 📊 Bar charts: Teams with biggest xG vs goals difference
- 🔵 Density plot: xG vs actual goals scored
- 📉 Scatter plot: xG overperformance/underperformance

---

## 📐 Statistical Tests

### Parametric Test
- **t-test**: Do home teams score significantly more goals than away teams?
  - *Hypothesis*: Home advantage leads to higher goal counts

### Non-parametric Test
- **Mann-Whitney U test**: xG comparison between top 5 and bottom 5 teams
  - *Hypothesis*: Top teams generate significantly higher xG

---

## 🏟️ Performance and Attendance

### Analysis Areas:
- 📈 Correlation between **team performance** and **home attendance**
- 🎫 Which team had the **highest average attendance**?
- 📊 Where did attendance **fluctuate the most** and why?
- 🔄 Impact of previous match results on attendance
- 📅 Seasonal trends in attendance

---

## 🧩 Starting Formation Analysis

### Research Questions:
- 📊 What was the **distribution of formations** across seasons?
- ⚔️ How did **formation matchups** impact match results?
- 🏆 What was the **most successful formation** (win rate)?
- 📈 How did formations affect:
  - xG generation
  - Possession percentage
  - Shots and shots on target
  - Goals scored and conceded

### Visualizations:
- 🥧 Pie chart: Formation distribution
- 📊 Heatmap: Formation vs formation results matrix

---

## 🔗 Correlation Analysis

Examine relationships between key variables:

| Variable 1 | Variable 2 | Expected Relationship |
|------------|------------|----------------------|
| xG | Goals scored | Strong positive |
| Shots | Shots on target | Strong positive |
| Shots on target | Goals | Positive |
| Possession | xG | Moderate positive |
| Shots | Goals | Moderate positive |

### Visualizations:
- 🔥 Correlation heatmap
- 📊 Scatter plots with regression lines
- 📈 Pair plots for multiple variables

---

## 📉 Regression Models

### Model 1: Goals Prediction
**Target variable**: Goals scored (gf)

**Features**:
- xG (expected goals)
- sh (shots)
- sot (shots on target)
- poss (possession %)

**Model type**: Linear Regression / Multiple Regression

### Model 2: Attendance Prediction
**Target variable**: Attendance

**Features**:
- Last game result (W/D/L)
- Goals scored in last game
- Current league position
- Day of week
- Opponent strength

**Model type**: Linear Regression

---

## 📝 Notes

- Dataset covers **Serie A seasons 2020-2025**
- Includes home and away match data
- Features: goals, xG, shots, possession, formation, attendance, etc.
- Data source: [Serie A Matches Dataset 2020-2025](https://www.kaggle.com/datasets/marcelbiezunski/serie-a-matches-dataset-2020-2025)

---

## 🎓 Project Requirements Met

| Requirement | Status | Details |
|-------------|--------|---------|
| ≥5 variables (3 numeric, 1 categorical) | ✅ | Numeric: gf, ga, xg, poss, sh, sot<br>Categorical: team, venue, formation |
| ≥100 observations | ✅ | ~1900 match records |
| Descriptive statistics | ✅ | Planned for all numeric variables |
| Categorical plots | ✅ | By team, venue, formation |
| Exploratory analysis | ✅ | Boxplots, histograms, density plots |
| Parametric test | ✅ | t-test (home vs away goals) |
| Non-parametric test | ✅ | Mann-Whitney U (top vs bottom teams) |
| Correlation analysis | ✅ | Multiple variable pairs |
| Regression analysis | ✅ | Goals and attendance prediction |

---

*Prettified markdown with claude sonnet 4.5*
*Last updated: February 2026*