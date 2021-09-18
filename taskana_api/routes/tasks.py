from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from taskana_api.database.connection import get_session
from taskana_api.database.tables import Task
from taskana_api.entities.tasks import TaskCreate

tasks_router = APIRouter()


@tasks_router.get('/{model_id}')
async def get_single_task(model_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Task).filter(Task.id == model_id))
    models = result.scalars().first()
    return [Task(title=model.title, description=model.description, id=model.id) for model in models]


@tasks_router.get('/')
async def get_tasks(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Task))
    models = result.scalars().all()
    return models


@tasks_router.post('/')
async def add_task(model: TaskCreate, session: AsyncSession = Depends(get_session)):
    model = Task(title=model.title, description=model.description)
    session.add(model)
    await session.commit()
    await session.refresh(model)
    return model
