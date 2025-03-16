from abc import abstractmethod
from typing import Protocol

from app.application.link.request_models import LinkUpdateRequest


class LinkUpdaterProtocol(Protocol):
    @abstractmethod
    async def path(self, link_data: LinkUpdateRequest) -> None: ...
