from datetime import datetime, timedelta
from typing import Tuple


def yesterday() -> datetime:
    return datetime.now() - timedelta(days=1)


def this_week() -> Tuple[datetime, datetime]:
    now = datetime.now()
    start = now - timedelta(days=now.weekday())
    end = start + timedelta(days=4)
    return start, end


def last_week() -> Tuple[datetime, datetime]:
    now = datetime.now()
    start = now - timedelta(days=now.weekday())
    last_week = start - timedelta(days=7)
    end = last_week + timedelta(days=4)
    return last_week, end
