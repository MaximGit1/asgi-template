from dataclasses import dataclass


@dataclass(slots=True, kw_only=True, frozen=True)
class LinkCreateRequest:
    full_path: str
    expiration: int


@dataclass(slots=True, kw_only=True, frozen=True)
class LinkUpdateRequest:
    full_path: str | None = None
    short_path: str | None = None
    expiration: int | None = None
