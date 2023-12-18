from .database import r, w

def u(m=0, d=None, id=None):
    if m==0:
        return list(r()["users_track"].keys())
    if d and not str(m.user_id) in d:
        d["users_track"].update({str(m.user_id): {}})
    print(d)
    d["users_track"][str(m.user_id)] = {"online_status": m.online_status, "channel_message": d["users_track"][str(m.user_id)]["channel_message"] if not id else [id]}
    w(d)
    return r()