from fastapi import APIRouter

from taskana_api.routes.actions import actions_router
from taskana_api.routes.statistics import statistics_router
from taskana_api.routes.tasks import tasks_router
from taskana_api.routes.users import users_router

v1_router = APIRouter()

v1_router.include_router(actions_router)
v1_router.include_router(users_router, prefix='/users')
v1_router.include_router(tasks_router, prefix='/tasks')
v1_router.include_router(statistics_router, prefix='/statistics')
"""
ресурсы

register
auth
user
user/addTag
task
Statistics
"""