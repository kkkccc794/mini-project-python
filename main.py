import tkinter as tk
from tkinter import messagebox

from database import add_match, search_matches
from analysis import calculate_statistics, compare_teams
from visualization import show_goals_chart, show_trend_chart


# =========================================================
# ADD MATCH RECORD
# =========================================================

def add_match_record():

    try:
        team = team_entry.get().strip()
        opponent = opponent_entry.get().strip()
        date = date_entry.get().strip()

        goals_scored = int(goals_scored_entry.get())
        goals_conceded = int(goals_conceded_entry.get())
        shots = int(shots_entry.get())
        possession = float(possession_entry.get())

        if not team or not opponent or not date:
            raise ValueError("Please fill all text fields.")

        if goals_scored < 0:
            raise ValueError("Goals scored cannot be negative.")

        if goals_conceded < 0:
            raise ValueError("Goals conceded cannot be negative.")

        if shots < 0:
            raise ValueError("Shots cannot be negative.")

        if possession < 0 or possession > 100:
            raise ValueError(
                "Possession must be between 0 and 100."
            )

        add_match(
            team,
            opponent,
            date,
            goals_scored,
            goals_conceded,
            shots,
            possession
        )

        messagebox.showinfo(
            "Success",
            "Match record added successfully!"
        )

        clear_fields()

    except ValueError as error:
        messagebox.showerror(
            "Invalid Input",
            str(error)
        )

    except Exception as error:
        messagebox.showerror(
            "Error",
            str(error)
        )


# =========================================================
# CLEAR INPUT FIELDS
# =========================================================

def clear_fields():

    team_entry.delete(0, tk.END)
    opponent_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    goals_scored_entry.delete(0, tk.END)
    goals_conceded_entry.delete(0, tk.END)
    shots_entry.delete(0, tk.END)
    possession_entry.delete(0, tk.END)


# =========================================================
# SEARCH MATCHES
# =========================================================

def search_records():

    team = search_team_entry.get().strip()
    opponent = search_opponent_entry.get().strip()

    try:

        df = search_matches(team, opponent)

        search_result.delete("1.0", tk.END)

        if df.empty:

            search_result.insert(
                tk.END,
                "No matching records found."
            )

            return

        search_result.insert(
            tk.END,
            df.to_string(index=False)
        )

    except Exception as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# =========================================================
# SHOW PERFORMANCE STATISTICS
# =========================================================

def show_statistics():

    stats = calculate_statistics()

    if stats is None:

        messagebox.showinfo(
            "Statistics",
            "No match records available."
        )

        return

    result = ""

    for key, value in stats.items():
        result += f"{key}: {value}\n"

    messagebox.showinfo(
        "Performance Statistics",
        result
    )


# =========================================================
# TEAM COMPARISON
# =========================================================

def compare_teams_gui():

    team1 = compare_team1_entry.get().strip()
    team2 = compare_team2_entry.get().strip()

    if not team1 or not team2:

        messagebox.showerror(
            "Input Error",
            "Please enter both team names."
        )

        return

    try:

        result = compare_teams(team1, team2)

        if result is None:

            messagebox.showinfo(
                "Comparison",
                "One or both teams were not found."
            )

            return

        team1_stats, team2_stats = result

        comparison = (
            f"{team1}\n"
            f"Matches: {team1_stats['Matches']}\n"
            f"Goals: {team1_stats['Goals']}\n"
            f"Average Goals: {team1_stats['Average Goals']}\n"
            f"Average Possession: "
            f"{team1_stats['Average Possession']}%\n\n"

            f"{team2}\n"
            f"Matches: {team2_stats['Matches']}\n"
            f"Goals: {team2_stats['Goals']}\n"
            f"Average Goals: {team2_stats['Average Goals']}\n"
            f"Average Possession: "
            f"{team2_stats['Average Possession']}%"
        )

        messagebox.showinfo(
            "Team Comparison",
            comparison
        )

    except Exception as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title(
    "Football Performance Analysis System"
)

root.geometry("900x750")


# =========================================================
# SCROLLABLE WINDOW
# =========================================================

canvas = tk.Canvas(root)

scrollbar = tk.Scrollbar(
    root,
    orient="vertical",
    command=canvas.yview
)

scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window(
    (0, 0),
    window=scrollable_frame,
    anchor="nw"
)

canvas.configure(
    yscrollcommand=scrollbar.set
)

canvas.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)


# =========================================================
# TITLE
# =========================================================

title = tk.Label(
    scrollable_frame,
    text="Football Performance Analysis System",
    font=("Arial", 20, "bold")
)

title.pack(pady=15)


# =========================================================
# MATCH ENTRY SECTION
# =========================================================

entry_frame = tk.Frame(scrollable_frame)

entry_frame.pack()


# Team Name

tk.Label(
    entry_frame,
    text="Team Name"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=5
)

team_entry = tk.Entry(
    entry_frame,
    width=25
)

team_entry.grid(
    row=0,
    column=1,
    pady=5
)


# Opponent

tk.Label(
    entry_frame,
    text="Opponent"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)

opponent_entry = tk.Entry(
    entry_frame,
    width=25
)

opponent_entry.grid(
    row=1,
    column=1,
    pady=5
)


# Date

tk.Label(
    entry_frame,
    text="Date"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=5
)

date_entry = tk.Entry(
    entry_frame,
    width=25
)

date_entry.grid(
    row=2,
    column=1,
    pady=5
)


# Goals Scored

tk.Label(
    entry_frame,
    text="Goals Scored"
).grid(
    row=3,
    column=0,
    padx=10,
    pady=5
)

goals_scored_entry = tk.Entry(
    entry_frame,
    width=25
)

goals_scored_entry.grid(
    row=3,
    column=1,
    pady=5
)


# Goals Conceded

tk.Label(
    entry_frame,
    text="Goals Conceded"
).grid(
    row=4,
    column=0,
    padx=10,
    pady=5
)

goals_conceded_entry = tk.Entry(
    entry_frame,
    width=25
)

goals_conceded_entry.grid(
    row=4,
    column=1,
    pady=5
)


# Shots

tk.Label(
    entry_frame,
    text="Shots"
).grid(
    row=5,
    column=0,
    padx=10,
    pady=5
)

shots_entry = tk.Entry(
    entry_frame,
    width=25
)

shots_entry.grid(
    row=5,
    column=1,
    pady=5
)


# Possession

tk.Label(
    entry_frame,
    text="Possession (%)"
).grid(
    row=6,
    column=0,
    padx=10,
    pady=5
)

possession_entry = tk.Entry(
    entry_frame,
    width=25
)

possession_entry.grid(
    row=6,
    column=1,
    pady=5
)


# =========================================================
# ADD BUTTON
# =========================================================

tk.Button(
    scrollable_frame,
    text="Add Match Record",
    command=add_match_record,
    width=30
).pack(pady=8)


# =========================================================
# SEARCH SECTION
# =========================================================

tk.Label(
    scrollable_frame,
    text="Search / Filter Matches",
    font=("Arial", 14, "bold")
).pack(pady=8)


search_frame = tk.Frame(scrollable_frame)

search_frame.pack()


# Search Team

tk.Label(
    search_frame,
    text="Team:"
).grid(
    row=0,
    column=0,
    padx=5
)

search_team_entry = tk.Entry(
    search_frame,
    width=15
)

search_team_entry.grid(
    row=0,
    column=1,
    padx=5
)


# Search Opponent

tk.Label(
    search_frame,
    text="Opponent:"
).grid(
    row=0,
    column=2,
    padx=5
)

search_opponent_entry = tk.Entry(
    search_frame,
    width=15
)

search_opponent_entry.grid(
    row=0,
    column=3,
    padx=5
)


# Search Button

tk.Button(
    scrollable_frame,
    text="Search Matches",
    command=search_records,
    width=30
).pack(pady=5)


# Search Result

search_result = tk.Text(
    scrollable_frame,
    height=3,
    width=95
)

search_result.pack(pady=3)


# =========================================================
# TEAM COMPARISON
# =========================================================

tk.Label(
    scrollable_frame,
    text="Compare Two Teams",
    font=("Arial", 14, "bold")
).pack(pady=8)


comparison_frame = tk.Frame(scrollable_frame)

comparison_frame.pack()


# Team 1

tk.Label(
    comparison_frame,
    text="Team 1:"
).grid(
    row=0,
    column=0,
    padx=5
)

compare_team1_entry = tk.Entry(
    comparison_frame,
    width=15
)

compare_team1_entry.grid(
    row=0,
    column=1,
    padx=5
)


# Team 2

tk.Label(
    comparison_frame,
    text="Team 2:"
).grid(
    row=0,
    column=2,
    padx=5
)

compare_team2_entry = tk.Entry(
    comparison_frame,
    width=15
)

compare_team2_entry.grid(
    row=0,
    column=3,
    padx=5
)


# Compare Button

tk.Button(
    scrollable_frame,
    text="Compare Teams",
    command=compare_teams_gui,
    width=30
).pack(pady=5)


# =========================================================
# STATISTICS BUTTON
# =========================================================

tk.Button(
    scrollable_frame,
    text="Show Performance Statistics",
    command=show_statistics,
    width=30
).pack(pady=5)


# =========================================================
# GRAPH BUTTONS
# =========================================================

tk.Button(
    scrollable_frame,
    text="Goals Comparison Chart",
    command=show_goals_chart,
    width=30
).pack(pady=5)


tk.Button(
    scrollable_frame,
    text="Performance Trend Chart",
    command=show_trend_chart,
    width=30
).pack(pady=5)


# =========================================================
# EXIT BUTTON
# =========================================================

tk.Button(
    scrollable_frame,
    text="Exit",
    command=root.destroy,
    width=30
).pack(pady=8)


# =========================================================
# START APPLICATION
# =========================================================

root.mainloop()