from sqlmodel import Field

from taskana_api.entities.tasks import TaskBase


class Task(TaskBase, table=True):
    id: int = Field(primary_key=True)
