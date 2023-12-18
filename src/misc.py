from .database import r, a

def u(m=0, d=None, id=None):
    if m==0:
        return list(r()["users_track"].keys())
    a({"users_track": {str(m.user_id): {"online_status": m.online_status, "channel_message": d["users_track"][str(m.user_id)]["channel_message"] if d else [id]}}})
    return r()