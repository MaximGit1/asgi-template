from app.application.common.exceptions import ApplicationError


def test_entity_error_initialization() -> None:
    error_msg = "Test error message"
    error = ApplicationError(error_msg)

    assert error.message == error_msg
    assert str(error) == error_msg
