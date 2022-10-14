from datetime import datetime
from typing import Dict, List, Optional, Union

import requests
from pydantic import parse_obj_as

from models import NokoEntry


class NokoClient:
    def __init__(self, token: str) -> None:
        self.token = token

    def get_entries_by_page(
        self, date_from: datetime, date_to: Optional[datetime] = None, page: int = 1
    ) -> List[NokoEntry]:
        if date_to is None:
            date_to = date_from

        params: Dict[str, Union[int, str]] = {
            "from": date_from.strftime("%Y-%m-%d"),
            "to": date_to.strftime("%Y-%m-%d"),
            "page": page,
        }

        response = requests.get(
            "https://api.nokotime.com/v2/entries",
            headers={"X-NokoToken": self.token},
            params=params,
        )
        return parse_obj_as(List[NokoEntry], response.json())

    def get_entries(
        self, date_from: datetime, date_to: Optional[datetime] = None
    ) -> List[NokoEntry]:
        all_entries = []
        page = 1
        while True:
            entries = self.get_entries_by_page(date_from, date_to, page)
            if len(entries) == 0:
                break
            page += 1
            all_entries.extend(entries)
        return all_entries
