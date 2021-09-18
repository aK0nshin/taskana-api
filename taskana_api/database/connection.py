from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from taskana_api.config import settings

# def get_url():
#     return DatabaseURL(settings.DB_URL)
#
#
# def get_pool():
#     database = MyDatabase(get_url())
#     return database
#
#
# async def connect_db(app):
#     await db.connect()
#
#
# async def disconnect_db(app):
#     await db.disconnect()

engine = create_async_engine(settings.DB_URL, echo=True, future=True)


async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session

# db = databases.Database(settings.DB_URL)
#
# engine = sqlalchemy.create_engine(
#     settings.DB_URL, connect_args={"check_same_thread": False}
# )
#
# Base.metadata.create_all(engine)
#
# users = UserTable.__table__
# user_db = SQLAlchemyUserDatabase(UserDB, database, users)