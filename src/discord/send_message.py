async def post(self, url, data, token):
    async with self.session.post(url, json=data, headers={"Authorization": "Bot " + token}) as response:
        try:
            return await response.json()
        except:
            return {}