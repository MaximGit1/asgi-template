from app.application.link.response_models import LinkIDResponse, LinkResponse
from app.domain.link.entity import Link
from app.domain.link.value_objects import LinkID


class LinkMapper:
    @staticmethod
    def to_id_response(link_id: LinkID) -> LinkIDResponse:
        return LinkIDResponse(link_id=link_id.value)

    @staticmethod
    def to_link_response(link: Link) -> LinkResponse:
        return LinkResponse(
            id=link.id.value,
            full_path=link.full_path.value,
            short_path=link.short_path.value,
            expiration=link.expiration,
        )
