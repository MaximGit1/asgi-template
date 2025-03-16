from abc import abstractmethod
from typing import Protocol

from app.domain.link.entity import Link
from app.domain.link.value_objects import LinkID, ShortPath


class LinkGetterProtocol(Protocol):
    @abstractmethod
    async def get_link_by_id(self, link_id: LinkID) -> Link: ...

    @abstractmethod
    async def get_link_by_short_url(self, url: ShortPath) -> Link: ...
