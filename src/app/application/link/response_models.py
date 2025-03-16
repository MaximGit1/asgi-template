from dataclasses import dataclass


@dataclass(slots=True, kw_only=True, frozen=True)
class LinkResponse:
    id: int
    full_path: str
    short_path: str
    expiration: int


@dataclass(slots=True, kw_only=True, frozen=True)
class LinkIDResponse:
    link_id: int
