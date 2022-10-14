import pytest
from models import NokoEntry, NokoUser


@pytest.fixture
def entries_page_1():
    return [
        {
            "id": 1,
            "date": "2022-10-14",
            "minutes": 40,
            "billable": True,
            "user": {
                "id": 1,
                "email": "user1@email.com",
                "first_name": "user",
                "last_name": "1",
            },
        }
    ]


@pytest.fixture
def entries_page_2():
    return [
        {
            "id": 2,
            "date": "2022-10-14",
            "minutes": 60,
            "billable": True,
            "user": {
                "id": 2,
                "email": "user2@email.com",
                "first_name": "user",
                "last_name": "2",
            },
        }
    ]


@pytest.fixture
def entries():
    return [
        NokoEntry(
            id=1,
            date="2022-10-14",
            minutes=40,
            billable=True,
            user=NokoUser(
                id=1,
                email="user1@email.com",
                first_name="user",
                last_name="1",
            ),
        ),
        NokoEntry(
            id=2,
            date="2022-10-14",
            minutes=30,
            billable=True,
            user=NokoUser(
                id=1,
                email="user1@email.com",
                first_name="user",
                last_name="1",
            ),
        ),
        NokoEntry(
            id=3,
            date="2022-10-14",
            minutes=30,
            billable=True,
            user=NokoUser(
                id=2,
                email="user2@email.com",
                first_name="user",
                last_name="2",
            ),
        ),
    ]
