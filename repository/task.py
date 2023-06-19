from models.task import Task

class TaskRepository:

    @classmethod
    def create(cls, task: dict) -> Task:
        task_document = Task(**task)
        task_document.save()
        return task_document

    @classmethod
    def get_many(cls, query: dict) -> list:
        return list(Task.objects.filter(**query))
