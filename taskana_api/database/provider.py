from databases import Database


# class MyDatabase(Database):
#     async def fetch_all(self, query, values: dict = None):
#         return [dict(x) for x in await super(MyDatabase, self).fetch_all(query=query, values=values)]
#
#     async def fetch_one(self, query, values: dict = None):
#         result = await super(MyDatabase, self).fetch_one(query=query, values=values)
#         if result:
#             return dict(result)
#         return result
