from dataclasses import dataclass

from app.domain.common import ValueObject
from app.domain.link.exceptions import LinkEntityValidationError


@dataclass(frozen=True)
class LinkID(ValueObject[int]):
    pass


@dataclass(frozen=True)
class FullPath(ValueObject[str]):
    def validate(self) -> None:
        value = self.value

        if not value.startswith(("http://", "https://")):
            msg = "This is not a link"
            raise LinkEntityValidationError(message=msg)

        min_length = 10
        max_length = 225


        value_length = len(value)

        if value_length < min_length or value_length > max_length:
            msg = ("The link length exceeds or falls short "
                   "of the required range")
            raise LinkEntityValidationError(message=msg)


@dataclass(frozen=True)
class ShortPath(ValueObject[str]):
    pass
