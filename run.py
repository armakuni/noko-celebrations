import os

from noko_client import NokoClient
from utils.calculations import calculate_time_worked, time_worked_in_hours
from utils.dates import last_week, this_week, yesterday
from utils.filters import (
    full_completions,
    full_completions_week,
    partial_completions,
    partial_completions_week,
)

token = os.getenv("NOKO_TOKEN")


if token is None:
    print("Must provide a NokoToken")
    exit(1)

client = NokoClient(token)
entries = client.get_entries(yesterday())
time_worked = calculate_time_worked(entries)

print("Yesterday")
print("  Partial completions")
for user, time in time_worked_in_hours(partial_completions(time_worked)).items():
    print(f"    {user}: {time} hours")

print("  Full completions")
for user, time in time_worked_in_hours(full_completions(time_worked)).items():
    print(f"    {user}: {time} hours")

week_entries = client.get_entries(*this_week())

week_time_worked = calculate_time_worked(week_entries)
print("\nThis week")
print("  Partial completions")
for user, time in time_worked_in_hours(
    partial_completions_week(week_time_worked)
).items():
    print(f"    {user}: {time} hours")

print("  Full completions")
for user, time in time_worked_in_hours(full_completions_week(week_time_worked)).items():
    print(f"    {user}: {time} hours")

last_week_entries = client.get_entries(*last_week())

last_week_time_worked = calculate_time_worked(last_week_entries)
print("\nLast week")
print("  Partial completions")
for user, time in time_worked_in_hours(
    partial_completions_week(last_week_time_worked)
).items():
    print(f"    {user}: {time} hours")

print("  Full completions")
for user, time in time_worked_in_hours(
    full_completions_week(last_week_time_worked)
).items():
    print(f"    {user}: {time} hours")
