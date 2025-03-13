from dataclasses import dataclass

from app.domain.common import BaseEntity
from app.domain.link.enums import LinkExpiration
from app.domain.link.value_objects import FullPath, LinkID, ShortPath


@dataclass(slots=True, kw_only=True)
class LinkEntity(BaseEntity[LinkID]):
    full_path: FullPath
    short_path: ShortPath
    expiration: LinkExpiration
