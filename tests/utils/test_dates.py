import freezegun

from utils.dates import this_week, yesterday, last_week


@freezegun.freeze_time("2022-10-13")
def test_yesterday():
    assert yesterday().strftime("%Y-%m-%d") == "2022-10-12"


@freezegun.freeze_time("2022-10-13")
def test_this_week():
    start_of_week, end_of_week = this_week()
    assert start_of_week.strftime("%Y-%m-%d") == "2022-10-10"
    assert end_of_week.strftime("%Y-%m-%d") == "2022-10-14"


@freezegun.freeze_time("2022-10-13")
def test_last_week():
    start_of_week, end_of_week = last_week()
    assert start_of_week.strftime("%Y-%m-%d") == "2022-10-03"
    assert end_of_week.strftime("%Y-%m-%d") == "2022-10-07"
