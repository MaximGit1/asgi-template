from app.application.link.mapper import LinkMapper
from app.application.link.protocols import LinkGetterProtocol
from app.application.link.response_models import LinkResponse
from app.domain.link.value_objects import LinkID, ShortPath


class LinkGetter:
    def __init__(
        self,
        repository: LinkGetterProtocol,
        mapper: LinkMapper,
    ) -> None:
        self._rep = repository
        self._mapper = mapper

    async def get_link_by_short_url(self, url: str) -> LinkResponse:
        return self._mapper.to_link_response(
            link=await self._rep.get_link_by_short_url(ShortPath(url)),
        )

    async def get_link_by_id(self, link_id: int) -> LinkResponse:
        return self._mapper.to_link_response(
            link=await self._rep.get_link_by_id(LinkID(link_id)),
        )
