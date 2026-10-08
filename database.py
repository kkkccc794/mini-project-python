import pandas as pd
import os

FILE_NAME = "football_data.csv"


def add_match(team, opponent, date, goals_scored,
              goals_conceded, shots, possession):

    data = {
        "Team": team,
        "Opponent": opponent,
        "Date": date,
        "Goals_Scored": goals_scored,
        "Goals_Conceded": goals_conceded,
        "Shots": shots,
        "Possession": possession
    }

    new_data = pd.DataFrame([data])

    if os.path.exists(FILE_NAME):
        new_data.to_csv(
            FILE_NAME,
            mode="a",
            header=False,
            index=False
        )
    else:
        new_data.to_csv(
            FILE_NAME,
            index=False
        )


def load_matches():
    try:
        return pd.read_csv(FILE_NAME)

    except FileNotFoundError:
        return pd.DataFrame()
def search_matches(team_name="", opponent=""):
    df = load_matches()

    if df.empty:
        return df

    if team_name:
        df = df[df["Team"].str.contains(team_name, case=False, na=False)]

    if opponent:
        df = df[df["Opponent"].str.contains(opponent, case=False, na=False)]

    return df