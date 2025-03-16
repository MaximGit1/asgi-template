from app.application.link.mapper import LinkMapper
from app.application.link.protocols import LinkCreatorProtocol
from app.application.link.request_models import LinkCreateRequest
from app.application.link.response_models import LinkIDResponse


class LinkCreator:
    def __init__(
        self,
        repository: LinkCreatorProtocol,
        mapper: LinkMapper,
    ) -> None:
        self._rep = repository
        self._mapper = mapper

    async def create(self, link_data: LinkCreateRequest) -> LinkIDResponse:
        return self._mapper.to_id_response(
            link_id=await self._rep.create(link_data=link_data),
        )
