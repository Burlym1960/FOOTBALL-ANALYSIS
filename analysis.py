import pandas as pd
import matplotlib.pyplot as plt

print("\n================ FOOTBALL DATA ANALYSIS ================\n")

# =========================
# 1. LOAD DATASET
# =========================
df = pd.read_csv("data/results.csv")
print(df.head())

# =========================
# 2. BASIC EXPLORATION
# =========================
print("\n================ BASIC EXPLORATION ================\n")

print("SHAPE:", df.shape)
print("COLUMNS:", df.columns)
print("EARLIEST DATE:", df["date"].min())
print("LATEST DATE:", df["date"].max())
print("UNIQUE TEAMS:", df["home_team"].nunique())

print("\nMOST FREQUENT HOME TEAM:")
print(df["home_team"].value_counts().head(1))

# =========================
# 3. GOALS ANALYSIS
# =========================
print("\n================ GOALS ANALYSIS ================\n")

df["total_goals"] = df["home_score"] + df["away_score"]

print("AVERAGE GOALS:", df["total_goals"].mean())

print("\nHIGHEST SCORING MATCH:")
print(df.sort_values("total_goals", ascending=False).head(1))

print("HOME GOALS TOTAL:", df["home_score"].sum())
print("AWAY GOALS TOTAL:", df["away_score"].sum())

print("\nMOST COMMON TOTAL GOALS:")
print(df["total_goals"].value_counts().head(1))

# =========================
# 4. MATCH RESULTS
# =========================
print("\n================ MATCH RESULTS ================\n")

def match_result(row):
    if row["home_score"] > row["away_score"]:
        return "Home Win"
    elif row["home_score"] < row["away_score"]:
        return "Away Win"
    else:
        return "Draw"

df["result"] = df.apply(match_result, axis=1)

result_percent = df["result"].value_counts(normalize=True) * 100
print("RESULT DISTRIBUTION (%):")
print(result_percent)

# =========================
# 5. HOME ADVANTAGE ANALYSIS
# =========================
print("\n================ HOME ADVANTAGE ================\n")

home_win_rate = (df["result"] == "Home Win").mean() * 100
away_win_rate = (df["result"] == "Away Win").mean() * 100
draw_rate = (df["result"] == "Draw").mean() * 100

print(f"HOME WINS: {home_win_rate:.2f}%")
print(f"AWAY WINS: {away_win_rate:.2f}%")
print(f"DRAWS: {draw_rate:.2f}%")

if home_win_rate > away_win_rate:
    print("\n👉 Conclusion: Home advantage exists")
else:
    print("\n👉 Conclusion: No strong home advantage")

# =========================
# 6. TOP WINNING TEAMS
# =========================
print("\n================ TOP WINNING TEAMS ================\n")

home_wins = df[df["result"] == "Home Win"]["home_team"].value_counts()
away_wins = df[df["result"] == "Away Win"]["away_team"].value_counts()

total_wins = home_wins.add(away_wins, fill_value=0)

top_teams = total_wins.sort_values(ascending=False).head(10)
print(top_teams)

print("\nMOST SUCCESSFUL TEAM OVERALL:")
print(total_wins.idxmax())

# =========================
# 7. VISUALIZATION
# =========================
print("\n================ VISUALIZATIONS ================\n")

# Goals distribution
plt.figure()
df["total_goals"].hist(bins=15)
plt.title("Distribution of Goals Per Match")
plt.xlabel("Goals")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Match outcomes
plt.figure()
df["result"].value_counts().plot(kind="bar")
plt.title("Match Outcomes")
plt.xlabel("Result")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Top teams
plt.figure()
top_teams.plot(kind="bar")
plt.title("Top 10 Teams by Wins")
plt.xlabel("Team")
plt.ylabel("Wins")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()