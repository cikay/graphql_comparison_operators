import strawberry

from resolvers.task import tasks_resolver

@strawberry.type
class Query:
    tasks = strawberry.field(resolver=tasks_resolver)
