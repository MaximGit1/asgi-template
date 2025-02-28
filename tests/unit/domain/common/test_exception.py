from app.domain.common.exceptions import DomainEntityError


def test_entity_error_initialization() -> None:
    error_msg = "Test error message"
    error = DomainEntityError(error_msg)

    assert error.message == error_msg
    assert str(error) == error_msg
