import asyncio
import aiosqlite


async def async_fetch_users():
  async with aiosqlite.connect("users.db") as db:
      async with db.execute("SELECT * FROM users;") as cursor:
          rows = await cursor.fetchall()
          return rows

async def async_fetch_older_users():
  async with aiosqlite.connect("users.db") as db:
      async with db.execute("SELECT * FROM users WHERE age > 40;") as cursor:
          rows = await cursor.fetchall()
          return rows



async def fetch_concurrently():
  users, old_users = await asyncio.gather(
    async_fetch_users(),
    async_fetch_older_users(),
  )
  
  return (users, old_users)

