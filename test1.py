import instagrapi
import os
b = instagrapi.Client()
login =b.login("wreck._.it._.ralph", "watersaintgood@1")
pics = os.listdir()
id = b.user_id_from_username("maheen_lakhvera")
for pic in pics:
    if login is True:
        if "png" not in pic:
            b.direct_send_file(pic, [id])
            print(f"{pic} Sent !!")
        else:
            pass
    else:
        login =b.login("wreck._.it._.ralph", "watersaintgood@1")
