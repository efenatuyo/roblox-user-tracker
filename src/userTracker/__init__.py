from .track import tracker_ss

class track_Ids:
    userPresenceType = [['Offline', 0x808080], ['Online', 0x00FF00], ['In Game', 0xFFFF00], ['In Studio', 0xFFA500], ['Invisible', 0x000000]]
    
    def __init__(self, cookie, token, user_ids=[], proxies=[None]): # proxy format: proxy_type://host:port
        self.cookie = cookie
        self.user_ids = user_ids
        self.proxies = proxies
        self.token = token
    
    async def track(self):
        await tracker_ss(self)
    