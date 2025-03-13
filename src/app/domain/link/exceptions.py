from app.domain.common import DomainEntityError


class LinkEntityValidationError(DomainEntityError):
    def __init__(self, message: str) -> None:
        super().__init__(message=message)
