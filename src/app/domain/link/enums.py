from enum import IntEnum


class LinkExpiration(IntEnum):
    """Time is stored in hours"""

    HALF_AN_HOUR = 0.5
    HOUR = 1
    HALF_AN_DAY = 12
    DAY = 24
    WEEK = 7 * 24
