from datetime import datetime

from graphql_models.task import TaskCreate, TaskRead, TaskQuery
from repositories.task import TaskRepository
from query_operators import build_query
from utils import to_dict

def create_task_resolver(task: TaskCreate) -> TaskRead:
    current_time = datetime.now()
    task_fields = {
        "created_at": current_time,
        "updated_at": current_time,
        "content": task.content
    }
    return TaskRepository.create(task_fields)


def tasks_resolver(query: TaskQuery) -> list[TaskRead]:
    query_dict = to_dict(query)
    orm_query = build_query(query_dict)
    return TaskRepository.get_many(orm_query)
