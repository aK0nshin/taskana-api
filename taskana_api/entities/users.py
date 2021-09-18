# from datetime import datetime
# from typing import Optional
#
# from fastapi_users import models
# from sqlmodel import SQLModel
#
#
# class UserBase(models.BaseUser, SQLModel):
#     first_name: str
#     birthdate: Optional[datetime.date]
#
#
# class UserCreate(models.BaseUserCreate, SQLModel):
#     first_name: str
#     birthdate: Optional[datetime.date]
#
#
# class UserUpdate(models.BaseUserUpdate, SQLModel):
#     first_name: Optional[str]
#     birthdate: Optional[datetime.date]
#
