from sqlmodel import SQLModel


class TaskBase(SQLModel):
    title: str
    description: str


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass
