from datetime import datetime
import aiopg

class Message():
	def __init__(self, **kwargs):
		self.db_str = 'dbname=postgres user=temirlanmyrzakhmetov host=127.0.0.1 port=5432'

	async def get_messages(self, table_name):
	    pool = await aiopg.create_pool(self.db_str)
	    async with pool.acquire() as conn:
	        async with conn.cursor() as cur:
	            await cur.execute(f"SELECT messages FROM {table_name};")
	            ret = {'messages': []}
	            async for row in cur:
	                ret['messages'].append(row[0])
	            return ret

	async def send_message(self, table_name, json_message):
		pool = await aiopg.create_pool(self.db_str)
		async with pool.acquire() as conn:
			async with conn.cursor() as cur:
				await cur.execute("INSERT INTO {1} (messages) VALUES ('{0}');".format(json_message, table_name))




