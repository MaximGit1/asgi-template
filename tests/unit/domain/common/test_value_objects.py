from typing import TypeVar

import pytest

from app.domain.common.exceptions import DomainEntityError
from app.domain.common.value_objects import ValueObject

ValueT = TypeVar("ValueT")
StorageT = TypeVar("StorageT", bound=list | tuple | set | dict)  # type: ignore
NumT = TypeVar("NumT", bound=int | float)

ERROR_MESSAGE = "Test error"
MIN_VALUE = 3


class InvalidVO(ValueObject[ValueT]):
    """validate() is not implemented"""


@pytest.mark.parametrize(
    "value",
    [
        "test",
        "t",
        "lal",
        123,
        None,
        13133,
        -12,
        ["123", 13213, None],
        True,
        False,
        {"test": None},
    ],
)
def test_invalid_vo(value: ValueT) -> None:
    with pytest.raises(NotImplementedError) as exp:
        InvalidVO(value)

    assert str(exp.value) == "Method 'validate' is not implemented"


class ValidVO(ValueObject[ValueT]):
    def validate(self) -> None:
        value = self.value

        if type(value) is str:
            self._validate_str(value=value)
        elif (
            ((type(value) in (int, float)) and (value < MIN_VALUE)) # type: ignore
            or ((type(value) in (list, tuple, set, dict))  # type: ignore
                and (len(value) < MIN_VALUE))  # type: ignore
            or ((type(value) is bool) and (not value))
        ):
            raise DomainEntityError(ERROR_MESSAGE)

    @staticmethod
    def _validate_str(value: str) -> None:
        if len(value) < MIN_VALUE:
            raise DomainEntityError(ERROR_MESSAGE)


@pytest.mark.parametrize(
    "value",
    ["test", "t", "lal", "lorem lorem lorem"],
)
def test_valid_vo_string(value: str) -> None:
    if len(value) < MIN_VALUE:
        with pytest.raises(DomainEntityError) as exp:
            ValidVO(value)
            assert str(exp.value) == ERROR_MESSAGE
    else:
        ValidVO(value)


@pytest.mark.parametrize(
    "value",
    [
        -13,
        1,
        0,
        2,
        3,
        15,
        1_000,
        13.543,
        0.000001,
        3.1,
        2.9,
        -0.4,
    ],
)
def test_valid_vo_numbers(value: NumT) -> None:
    if value < MIN_VALUE:
        with pytest.raises(DomainEntityError) as exp:
            ValidVO(value)
            assert str(exp.value) == ERROR_MESSAGE
    else:
        ValidVO(value)


@pytest.mark.parametrize(
    "value",
    [
        [None] * 3,
        [None] * 2,
        [None] * 100,
        [None],
        (None,),
        (None, None),
        (None, None, None),
        (None, None, None, None),
        {None},
        {None, 1, 2},
        {1, 2, 3, 6},
        {
            "one": 1,
        },
        {"one": 1, "two": 2, "next": False},
    ],
)
def test_valid_vo_storages(value: StorageT) -> None:
    if len(value) < MIN_VALUE:
        with pytest.raises(DomainEntityError) as exp:
            ValidVO(value)
            assert str(exp.value) == ERROR_MESSAGE
    else:
        ValidVO(value)


@pytest.mark.parametrize("value", [True, False])
def test_valid_vo_boolean(*, value: bool) -> None:
    if not value:
        with pytest.raises(DomainEntityError) as exp:
            ValidVO(value)
            assert str(exp.value) == ERROR_MESSAGE
    else:
        ValidVO(value)


def test_repr() -> None:
    vo = ValidVO("test")
    assert repr(vo) == "ValidVO('test')"
