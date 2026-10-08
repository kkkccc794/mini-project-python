import matplotlib.pyplot as plt
from database import load_matches


def show_goals_chart():

    df = load_matches()

    if df.empty:
        print("No match records available.")
        return

    plt.figure(figsize=(8, 5))

    x = range(len(df))

    plt.bar(
        [i - 0.2 for i in x],
        df["Goals_Scored"],
        width=0.4,
        label="Goals Scored"
    )

    plt.bar(
        [i + 0.2 for i in x],
        df["Goals_Conceded"],
        width=0.4,
        label="Goals Conceded"
    )

    plt.xticks(
        list(x),
        df["Opponent"]
    )

    plt.xlabel("Opponent")
    plt.ylabel("Goals")
    plt.title("Goals Scored vs Goals Conceded")

    plt.legend()
    plt.tight_layout()
    plt.show()


def show_trend_chart():

    df = load_matches()

    if df.empty:
        print("No match records available.")
        return

    plt.figure(figsize=(8, 5))

    plt.plot(
        df["Date"],
        df["Goals_Scored"],
        marker="o",
        label="Goals Scored"
    )

    plt.plot(
        df["Date"],
        df["Goals_Conceded"],
        marker="o",
        label="Goals Conceded"
    )

    plt.xlabel("Match Date")
    plt.ylabel("Goals")
    plt.title("Team Performance Trend")

    plt.legend()
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()