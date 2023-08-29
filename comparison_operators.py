from typing import Generic, TypeVar

import strawberry

T = TypeVar("T")

@strawberry.input
class ComparisonOperators(Generic[T]):
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
        if isinstance(value, ComparisonOperators):
            params |= generate_orm_comparison_operators(field, value)
        else:
            params[field] = value

    return params


def generate_orm_comparison_operators(field: str, comparison_operators: ComparisonOperators):
    generated_fields = {}
    for comparison_operator, value in comparison_operators.__dict__.items():
        if value is strawberry.UNSET:
            continue

        if comparison_operator == "in_list":
            comparison_operator = "in"
        elif comparison_operator == "not_in_list":
            comparison_operator = "nin"

        generated_fields[f"{field}__{comparison_operator}"] = value

    return generated_fields
