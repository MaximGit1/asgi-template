import pytest

from app.domain.link.entity import LinkEntity
from app.domain.link.enums import LinkExpiration
from app.domain.link.exceptions import LinkEntityValidationError
from app.domain.link.value_objects import FullPath, LinkID, ShortPath


@pytest.mark.parametrize(
    ("full_path", "short_path", "expiration"),
    [
        ("google-bugle.com", "", LinkExpiration.DAY),
        ("htpp://l.ru", "", LinkExpiration.HALF_AN_DAY),
    ],
)
def test_entity_error_initialization(
    full_path: str, short_path: str, expiration: LinkExpiration,
) -> None:
    with pytest.raises(LinkEntityValidationError):
        LinkEntity(
            id=LinkID(1),
            full_path=FullPath(full_path),
            short_path=ShortPath(short_path),
            expiration=expiration,
        )
