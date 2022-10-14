from utils.calculations import calculate_time_worked, time_worked_in_hours


def test_calculate_time_worked(entries):
    assert calculate_time_worked(entries) == {"user 1": 70, "user 2": 30}


def test_time_worked_in_hours():
    time_worked_in_minutes = {"foo": 600, "bar": 450}
    assert time_worked_in_hours(time_worked_in_minutes) == {"foo": 10, "bar": 7.5}
