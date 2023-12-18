import aiohttp

from   dataclasses     import dataclass
from ..cookieRefresher import Bypass

@dataclass
class user_request():
    status_code: int = None
    online_status: int = None
    last_location: str = None
    place_id: int = None
    user_id: int = None
    last_online: str = None
    
class aioSession:
    def __init__(self, cookie):
        self.session = aiohttp.ClientSession(cookies={".ROBLOSECURITY": Bypass(cookie).start_process()})
    
    async def post(self, user_ids, proxy):
        try:
            async with self.session.post("https://presence.roblox.com/v1/presence/users", json={"userIds": user_ids}, proxy=proxy) as response:
                response_json = (await response.json())["userPresences"]
        
                data = []
                for user_data in response_json:
                    data.append(user_request(status_code=response.status, online_status=user_data.get("userPresenceType"), last_location=user_data.get("lastLocation") ,place_id=user_data.get("placeId"), user_id=user_data.get("userId"), last_online=user_data.get("lastOnline")))
        
                return data
        except:
            return []
    
    async def get(self, url):
        async with self.session.get(url) as response:
            return (await response.json())
        
    async def close(self):
        await self.session.close()