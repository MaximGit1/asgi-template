import pytest

from app.domain.link.exceptions import LinkEntityValidationError
from app.domain.link.value_objects import FullPath, LinkID


@pytest.mark.parametrize("link_id", [0, 1, 2, 3, 9999, -1])
def test_link_id(link_id: int) -> None:
    assert link_id == LinkID(link_id).value


@pytest.mark.parametrize(
    "url",
    [
        "https://www.google.com/",
        "http://www.google.com/",
        "www.google.com/",
        "www.google.com",
        "https://127.0.0.1/",
        "https://127.0.0.1/" * 100,
    ],
)
def test_full_path_len(url: str) -> None:
    min_length = 10
    max_length = 225

    value_length = len(url)

    if value_length < min_length or value_length > max_length:
        err_msg = ("The link length exceeds or falls short "
                   "of the required range")
        with pytest.raises(LinkEntityValidationError) as exp:
            FullPath(url)
        assert str(exp.value) == err_msg


@pytest.mark.parametrize(
    "url",
    [
        "",
        " ",
        "https://www.google.com/",
       "http://www.google.com/",
        "www.google.com/",
        "www.google.com",
        "https://127.0.0.1/",
    ],
)
def test_full_path_value(url: str) -> None:
    if url[:7] != "http://" and url[:8] != "https://":
        err_msg = "This is not a link"
        with pytest.raises(LinkEntityValidationError) as exp:
            FullPath(url)
        assert str(exp.value) == err_msg
