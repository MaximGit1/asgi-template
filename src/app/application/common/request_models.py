from dataclasses import dataclass
from enum import StrEnum, auto


@dataclass(slots=True)
class PaginationParams:
    offset: int
    limit: int


class SortOrder(StrEnum):
    ASC = auto()
    DESC = auto()
