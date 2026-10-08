from database import load_matches


def calculate_statistics():

    df = load_matches()

    if df.empty:
        return None

    total_matches = len(df)

    goals_scored = df["Goals_Scored"].sum()
    goals_conceded = df["Goals_Conceded"].sum()

    average_goals = df["Goals_Scored"].mean()
    average_possession = df["Possession"].mean()

    wins = (
        df["Goals_Scored"] > df["Goals_Conceded"]
    ).sum()

    draws = (
        df["Goals_Scored"] == df["Goals_Conceded"]
    ).sum()

    losses = (
        df["Goals_Scored"] < df["Goals_Conceded"]
    ).sum()

    win_percentage = (
        wins / total_matches
    ) * 100

    return {
        "Total Matches": total_matches,
        "Goals Scored": goals_scored,
        "Goals Conceded": goals_conceded,
        "Average Goals": round(average_goals, 2),
        "Average Possession": round(average_possession, 2),
        "Wins": wins,
        "Draws": draws,
        "Losses": losses,
        "Win Percentage": round(win_percentage, 2)
    }


def compare_teams(team1, team2):

    df = load_matches()

    if df.empty:
        return None

    team1_data = df[
        df["Team"].str.lower() == team1.lower()
    ]

    team2_data = df[
        df["Team"].str.lower() == team2.lower()
    ]

    if team1_data.empty or team2_data.empty:
        return None

    team1_stats = {
        "Matches": len(team1_data),
        "Goals": team1_data["Goals_Scored"].sum(),
        "Average Goals": round(
            team1_data["Goals_Scored"].mean(), 2
        ),
        "Average Possession": round(
            team1_data["Possession"].mean(), 2
        )
    }

    team2_stats = {
        "Matches": len(team2_data),
        "Goals": team2_data["Goals_Scored"].sum(),
        "Average Goals": round(
            team2_data["Goals_Scored"].mean(), 2
        ),
        "Average Possession": round(
            team2_data["Possession"].mean(), 2
        )
    }

    return team1_stats, team2_stats