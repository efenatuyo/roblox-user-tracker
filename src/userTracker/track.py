from ..requestHandler       import aioSession
from ..database             import r, a
from ..discord.send_message import post
from ..misc                 import u
import asyncio

async def tracker_ss(self):
    session = aioSession(self.cookie)
    list_ids = split(self.user_ids)
    while True:
        current_proxy = 0
        tasks = []
        for user_ids in list_ids:
            tasks.append(tracker_tasks(self, session, user_ids, self.proxies[current_proxy]))
            if not len(current_proxy) > current_proxy:
                current_proxy = 0
            else:
                current_proxy += 1
        await asyncio.gather(*tasks)

        list_ids = split(self.user_ids)
        self.user_ids = u()
        await asyncio.sleep(1)

async def tracker_tasks(self, session, user_ids, proxy):
        response = await session.post(user_ids, proxy)
        for resp in response:
            if not resp.status_code == 200:
                if resp.status_code == 429:
                    await asyncio.sleep(5)
                continue
            
            data = r()
            if str(resp.user_id) not in data["users_track"]:
                data = u(resp)
                
            if resp.online_status != data["users_track"][str(resp.user_id)]["online_status"]:
                embed_data = {"embeds": [{
                    "title": "User Tracker",
                    "color": self.userPresenceType[resp.online_status][1],
                    "fields": [
                        {"name": "Online Status", "value": f"from **{str(self.userPresenceType[data['users_track'][str(resp.user_id)]['online_status']][0])}** to **{str(self.userPresenceType[resp.online_status][0])}**", "inline": False},
                        {"name": "Last Location", "value": resp.last_location, "inline": False},
                        {"name": "Place ID", "value": str(resp.place_id), "inline": False},
                        {"name": "User Profile", "value": f"[Profile](https://www.roblox.com/users/{str(resp.user_id)}/profile)", "inline": False},
                        {"name": "Last Online", "value": resp.last_online, "inline": False}
                    ]}
                ]}
                tasks = []
                for channel_ids in data["users_track"][str(resp.user_id)]["channel_message"]:
                    tasks.append(post(session, f"https://discord.com/api/v9/channels/{channel_ids}/messages", embed_data, self.token))
                await asyncio.gather(*tasks)
                data = u(resp, data)

def split(input_list: list, max_len: int = 200):
    if len(input_list) <= max_len:
        return [input_list]
        
    input_list *= -(-max_len // len(input_list))
    return [input_list[i:i+max_len] for i in range(0, len(input_list), max_len)]
