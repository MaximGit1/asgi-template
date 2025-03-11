from app.application.common.request_models import PaginationParams, SortOrder


def test_pagination_params_initialization() -> None:
    offset, limit = 1, 10
    pagination_params = PaginationParams(
        offset=offset,
        limit=limit,
    )
    assert pagination_params.offset == offset
    assert pagination_params.limit == limit


def test_sort_order_params_initialization() -> None:
    assert SortOrder.ASC.name == "ASC"
    assert SortOrder.DESC.name == "DESC"
