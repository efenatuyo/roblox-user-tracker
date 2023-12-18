from src.userTracker import track_Ids
from src.discord import bot
import asyncio

token = ".Gf_5bn."

cookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|"
async def run():
      tasks = [track_Ids(cookie, token).track(), # proxies arg list argument optimal but suggested after 200 ids
             bot.start(token)]
      
      await asyncio.gather(*tasks)

asyncio.run(run())
