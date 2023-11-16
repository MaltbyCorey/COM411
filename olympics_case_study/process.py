import tui

COL_MEDAL = 14
COL_TEAM = 6
COL_YEAR = 9


def list_years(data):
    tui.started("Listing years")
    years = set()
    for year in data:
        year = year[COL_YEAR]
        years.add(year)

    tui.display_years(years)
    tui.completed()


def tally_medals(data):
    tui.started("Tally medals")
    count = {"Gold": 0, "Silver": 0, "Bronze": 0}
    for record in data:
        medal = record[COL_MEDAL]
        if medal == "Gold":
            count["Gold"] += 1
        elif medal == "Silver":
            count["Silver"] += 1
        elif medal == "Bronze":
            count["Bronze"] += 1

    tui.display_medal_tally(count)
    tui.completed()


def tally_team_medals(data):
    tui.started("Tallying medals for each team")
    medal_tally = {}
    for record in data:
        team = record[COL_TEAM]
        medal = record[COL_MEDAL]

        if medal in ("Gold", "Silver", "Bronze"):
            if team in medal_tally:
                medal_tally[team][medal] += 1
            else:
                medal_tally[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
                medal_tally[team][medal] += 1

    tui.display_team_medal_tally(medal_tally)
    tui.completed()
