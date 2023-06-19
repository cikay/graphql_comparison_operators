from typing import Generic, TypeVar

import strawberry

T = TypeVar("T")

@strawberry.input
class QueryOperators(Generic[T]):
    exact: T | None = strawberry.UNSET
    iexact: T | None = strawberry.UNSET
    contains: T | None = strawberry.UNSET
    icontains: T | None = strawberry.UNSET
    # in_list is equivalent to operator `in` in Mongoengine as the word in
    # is not valid variable name in Python
    in_list: list[T] | None = strawberry.UNSET
    not_in_list: list[T] | None = strawberry.UNSET
    gt: T | None = strawberry.UNSET
    gte: T | None = strawberry.UNSET
    lt: T | None = strawberry.UNSET
    lte: T | None = strawberry.UNSET
    startswith: T | None = strawberry.UNSET
    istartswith: T | None = strawberry.UNSET
    endswith: T | None = strawberry.UNSET
    iendswith: T | None = strawberry.UNSET
    regex: T | None = strawberry.UNSET
    iregex: T | None = strawberry.UNSET


def build_query(query: dict):
    params = {}
    for field, value in query.items():
        if isinstance(value, QueryOperators):
            params |= generate_orm_query_operators(field, value)
        else:
            params[field] = value

    return params


def generate_orm_query_operators(field, filter_lookup):
    generated_fields = {}
    for lookup_field, value in filter_lookup.__dict__.items():
        if value is strawberry.UNSET:
            continue

        if lookup_field == "in_list":
            lookup_field = "in"
        elif lookup_field == "not_in_list":
            lookup_field = "nin"

        generated_fields[f"{field}__{lookup_field}"] = value

    return generated_fields
