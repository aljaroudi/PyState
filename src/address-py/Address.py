from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class USAddress:
    addressee: str
    street_num: str
    street_name: str
    apt_num: str

    city: str
    region: str
    country: str

    @classmethod
    def parse(cls, address: str):
        return cls('', '', '', '', '', '', '')

    @classmethod
    def parse_google_maps(cls, address: str, api_key: str):
        pass
