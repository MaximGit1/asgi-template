from abc import abstractmethod
from typing import Protocol

from app.domain.link.value_objects import LinkID


class LinkDeleterProtocol(Protocol):
    @abstractmethod
    async def delete(self, link_id: LinkID) -> None: ...
