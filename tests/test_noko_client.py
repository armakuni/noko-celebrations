from datetime import datetime, timedelta
from time import time
from typing import List
import responses
from models import NokoEntry
from noko_client import NokoClient
from pydantic import parse_obj_as
import freezegun


@freezegun.freeze_time("2022-10-14")
@responses.activate
def test_get_entries_by_page(entries_page_1):
    client = NokoClient("fake_token")
    responses.get(
        "https://api.nokotime.com/v2/entries",
        json=entries_page_1,
        match=[
            responses.matchers.query_param_matcher(
                {"from": "2022-10-14", "to": "2022-10-14", "page": 1}
            ),
            responses.matchers.header_matcher({"X-NokoToken": "fake_token"}),
        ],
    )
    assert client.get_entries_by_page(date_from=datetime.now(), page=1) == parse_obj_as(
        List[NokoEntry], entries_page_1
    )


@freezegun.freeze_time("2022-10-14")
@responses.activate
def test_get_entries_by_page_uses_data_ranges(entries_page_1):
    client = NokoClient("fake_token")
    responses.get(
        "https://api.nokotime.com/v2/entries",
        json=entries_page_1,
        match=[
            responses.matchers.query_param_matcher(
                {"from": "2022-10-11", "to": "2022-10-14", "page": 1}
            ),
            responses.matchers.header_matcher({"X-NokoToken": "fake_token"}),
        ],
    )
    assert client.get_entries_by_page(
        date_from=datetime.now() - timedelta(days=3), date_to=datetime.now(), page=1
    ) == parse_obj_as(List[NokoEntry], entries_page_1)


@freezegun.freeze_time("2022-10-13")
@responses.activate
def test_get_entries_single_page(entries_page_1):
    client = NokoClient("fake_token")
    responses.get(
        "https://api.nokotime.com/v2/entries",
        json=entries_page_1,
        match=[
            responses.matchers.query_param_matcher(
                {"from": "2022-10-13", "to": "2022-10-13", "page": 1}
            ),
            responses.matchers.header_matcher({"X-NokoToken": "fake_token"}),
        ],
    )
    responses.get(
        "https://api.nokotime.com/v2/entries",
        json=[],
    )
    assert client.get_entries(date_from=datetime.now()) == parse_obj_as(
        List[NokoEntry], entries_page_1
    )


@freezegun.freeze_time("2022-10-13")
@responses.activate
def test_get_entries_multi_page(entries_page_1, entries_page_2):
    client = NokoClient("fake_token")
    responses.get(
        "https://api.nokotime.com/v2/entries",
        json=entries_page_1,
        match=[
            responses.matchers.query_param_matcher(
                {"from": "2022-10-13", "to": "2022-10-13", "page": 1}
            ),
            responses.matchers.header_matcher({"X-NokoToken": "fake_token"}),
        ],
    )
    responses.get(
        "https://api.nokotime.com/v2/entries",
        json=entries_page_2,
        match=[
            responses.matchers.query_param_matcher(
                {"from": "2022-10-13", "to": "2022-10-13", "page": 2}
            ),
            responses.matchers.header_matcher({"X-NokoToken": "fake_token"}),
        ],
    )
    responses.get(
        "https://api.nokotime.com/v2/entries",
        json=[],
    )
    assert client.get_entries(date_from=datetime.now()) == parse_obj_as(
        List[NokoEntry], entries_page_1
    ) + parse_obj_as(List[NokoEntry], entries_page_2)
