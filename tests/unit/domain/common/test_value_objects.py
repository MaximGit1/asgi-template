from typing import TypeVar

import pytest

from app.domain.common.exceptions import DomainEntityError
from app.domain.common.value_objects import ValueObject

ValueT = TypeVar("ValueT")
ERROR_MESSAGE = "Test error"


class InvalidVO(ValueObject[ValueT]):
    """validate() is not implemented"""


class ValidVO(ValueObject[ValueT]):
    def validate(self) -> None:
        if not self.value:
            raise DomainEntityError(ERROR_MESSAGE)


@pytest.mark.parametrize(
    "value",
    ["test", "", 0, 1, [], [1], (1,), {1, 2}, True, False],
)
def test_empty_validation_vo(value: ValueT) -> None:
    assert InvalidVO(value)


@pytest.mark.parametrize(
    "value",
    ["test", "", 0, 1, [], [1], (1,), {1, 2}, True, False],
)
def test_valid_vo(value: str) -> None:
    if not value:
        with pytest.raises(DomainEntityError) as exp:
            ValidVO(value)
            assert str(exp.value) == ERROR_MESSAGE
    else:
        ValidVO(value)


def test_repr() -> None:
    vo = ValidVO("test")
    assert repr(vo) == "ValidVO('test')"
