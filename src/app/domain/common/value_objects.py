from dataclasses import dataclass
from typing import Generic, TypeVar

ValueT = TypeVar("ValueT")


@dataclass(frozen=True)
class ValueObject(Generic[ValueT]):
    value: ValueT

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        """
        Must be implemented by subclasses.
        Raises a :class:`DomainValidationError` if the value is invalid.
        """

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value!r})"
