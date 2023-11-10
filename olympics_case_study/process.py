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
