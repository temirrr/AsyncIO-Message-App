from datetime import datetime
import aiopg

class Message():
	def __init__(self, **kwargs):
		#self.db_str = 'dbname=postgres user=postgres password=timkabro7 host=127.0.0.1 port=5002'
		self.db_str = 'dbname=postgres user=temirlanmyrzakhmetov password=timkabro7 host=127.0.0.1 port=5432'

	async def get_messages(self, table_name):
	    pool = await aiopg.create_pool(self.db_str)
	    async with pool.acquire() as conn:
	        async with conn.cursor() as cur:
	            await cur.execute(f"SELECT messages FROM {table_name};")
	            ret = {'messages': []}
	            async for row in cur:
	                ret['messages'].append(row[0])
	            return ret
	            


	'''loop = asyncio.get_event_loop()
	loop.run_until_complete(go())'''

	async def send_message(self, table_name, message):
		pool = await aiopg.create_pool(self.db_str)
		async with pool.acquire() as conn:
			async with conn.cursor() as cur:
				await cur.execute(f"INSERT INTO {table_name} (messages) VALUES ('{message}');")




