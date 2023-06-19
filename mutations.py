import strawberry

from resolvers.task import create_task_resolver

@strawberry.type
class Mutations:
    create_task = strawberry.mutation(resolver=create_task_resolver)
