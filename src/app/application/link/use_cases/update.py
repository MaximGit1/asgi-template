from app.application.link.protocols import LinkUpdaterProtocol
from app.application.link.request_models import LinkUpdateRequest


class LinkUpdater:
    def __init__(self, repository: LinkUpdaterProtocol) -> None:
        self._rep = repository

    async def update(self, link: LinkUpdateRequest) -> None:
        return await self._rep.path(link_data=link)
