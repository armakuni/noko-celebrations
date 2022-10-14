from typing import Dict, List

from models import NokoEntry, NokoUser


def calculate_time_worked(entries: List[NokoEntry]) -> Dict[str, int]:
    users: Dict[int, NokoUser] = {}
    time_worked: Dict[int, int] = {}
    for entry in entries:
        users[entry.user.id] = entry.user
        current_time = time_worked.get(entry.user.id, 0)
        time_worked[entry.user.id] = current_time + entry.minutes

    time_worked_by_name = {
        f"{users[user].first_name} {users[user].last_name}": time
        for user, time in time_worked.items()
    }
    return time_worked_by_name


def time_worked_in_hours(time_worked_in_minutes: Dict[str, int]) -> Dict[str, float]:
    return {user: time / 60 for user, time in time_worked_in_minutes.items()}
