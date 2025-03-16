from abc import abstractmethod
from typing import Protocol

from app.application.link.request_models import LinkCreateRequest
from app.domain.link.value_objects import LinkID


class LinkCreatorProtocol(Protocol):
    @abstractmethod
    async def create(self, link_data: LinkCreateRequest) -> LinkID: ...
