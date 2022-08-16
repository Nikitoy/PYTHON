import calendar
from pathlib import Path

month_year = list(calendar.month_name[1:])

day_week = list(calendar.day_name[0:])

for i, month in enumerate(month_year):
    for day in day_week:
        Path(f'2022/{i+1}.{month}/{day}').mkdir(parents=True, exist_ok=True)
