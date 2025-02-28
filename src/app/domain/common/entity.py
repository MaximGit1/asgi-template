from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from app.domain.common.value_objects import ValueObject

ValueT = TypeVar("ValueT")
EntityId = TypeVar("EntityId", bound=ValueObject[Any])


@dataclass
class BaseEntity(Generic[EntityId]):
    id: EntityId
