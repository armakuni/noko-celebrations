from typing import Dict
import operator

ONE_DAY = 8 * 60
ONE_WEEK = ONE_DAY * 5


def partial_completions(time_worked_in_minutes: Dict[str, int]) -> Dict[str, int]:
    return __filter_time_worked(time_worked_in_minutes, operator.lt, ONE_DAY)


def full_completions(time_worked_in_minutes: Dict[str, int]) -> Dict[str, int]:
    return __filter_time_worked(time_worked_in_minutes, operator.ge, ONE_DAY)


def partial_completions_week(time_worked_in_minutes: Dict[str, int]) -> Dict[str, int]:
    return __filter_time_worked(time_worked_in_minutes, operator.lt, ONE_WEEK)


def full_completions_week(time_worked_in_minutes: Dict[str, int]) -> Dict[str, int]:
    return __filter_time_worked(time_worked_in_minutes, operator.ge, ONE_WEEK)


def __filter_time_worked(
    time_worked: Dict[str, int], op: operator, limit: int
) -> Dict[str, int]:
    return {user: time for user, time in time_worked.items() if op(time, limit)}
