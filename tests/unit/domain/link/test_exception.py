from app.domain.link.exceptions import LinkEntityValidationError


def test_entity_error_initialization() -> None:
    error_msg = "Test error message"
    error = LinkEntityValidationError(error_msg)

    assert error.message == error_msg
    assert str(error) == error_msg
