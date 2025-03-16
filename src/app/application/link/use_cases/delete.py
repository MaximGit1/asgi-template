from app.application.link.protocols import LinkDeleterProtocol
from app.domain.link.value_objects import LinkID


class LinkUpdater:
    def __init__(self, repository: LinkDeleterProtocol) -> None:
        self._rep = repository

    async def update(self, link_id: LinkID) -> None:
        return await self._rep.delete(link_id=link_id)
