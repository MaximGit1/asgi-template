from .create import LinkCreatorProtocol
from .delete import LinkDeleterProtocol
from .get import LinkGetterProtocol
from .update import LinkUpdaterProtocol

__all__ = (
    "LinkCreatorProtocol",
    "LinkGetterProtocol",
    "LinkUpdaterProtocol",
    "LinkDeleterProtocol",
)
