from datetime import datetime

import strawberry

from comparison_operators import ComparisonOperators

@strawberry.type
class TaskRead:
    id: str
    content: str
    created_at: datetime
    updated_at: datetime


@strawberry.input
class TaskCreate:
    content: str

@strawberry.input
class TaskQuery:
    id: str | None = strawberry.UNSET
    created_at: ComparisonOperators[datetime] | None = strawberry.UNSET

