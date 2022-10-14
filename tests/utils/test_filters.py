from utils.filters import (
    full_completions,
    partial_completions,
    partial_completions_week,
    full_completions_week,
)


def test_partial_completions():
    time_worked_in_minutes = {"foo": 480, "bar": 300, "baz": 1000}
    assert partial_completions(time_worked_in_minutes) == {"bar": 300}


def test_full_completions():
    time_worked_in_minutes = {"foo": 480, "bar": 300, "baz": 1000}
    assert full_completions(time_worked_in_minutes) == {"foo": 480, "baz": 1000}


def test_partial_completions_week():
    time_worked_in_minutes = {"foo": 2400, "bar": 300, "baz": 5000}
    assert partial_completions_week(time_worked_in_minutes) == {"bar": 300}


def test_full_completions_week():
    time_worked_in_minutes = {"foo": 2400, "bar": 300, "baz": 5000}
    assert full_completions_week(time_worked_in_minutes) == {"foo": 2400, "baz": 5000}
