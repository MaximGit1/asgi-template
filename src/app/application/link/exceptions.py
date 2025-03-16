from app.application.common import ApplicationError


class LinkNotFoundError(ApplicationError):
    def __init__(self, url: str) -> None:
        msg = f"Link not found, url: {url}"
        super().__init__(msg)
