import sqlite3

DB_location="/srv1/process/tender.db"

conn = sqlite3.connect(DB_location,check_same_thread=False)
cur = conn.cursor()

find_tender = "select * from tender where Category like \"%{0}%\""
monitering_tender = "SELECT * FROM tender order by id desc"
detail_tender = "select * from tender where InputTime like \"%{0}%\""

cats_analogue = {
    "TRANSFORMER":["converter","transformer"],
    "SWITCH":["switch"],
    "OLBS":["olbs","oil Immersed Loadbreak Switch","Switch","Loadbreak","Load break","breaker"],
    "CABLE":["cable", "conductors", "insulating", "wire", "cables"],
    "INSULATOR":["insulator", "electrical insulator","Ceramic insulator"],
    "ARRESTOR":["arrester","Surge","lightning","surge diverter", "diverter", "protect", "protector", "Lightning rod"],
    "FUSES":["fuse", "fusing", "fuse-base", "fuse-link", "drop-out", "fuse-carrier", "fuse-element", "melt", "cos", "cut", "cutout", "holder"],
    "UPS":["ups", "Uninterruptible Power Supply","Power Supply"],
    "METER":["meter","watt-hour meter","ectricity meter"],
    "GENERATOR":["generator"," generating","dynamo"],
    "BATTERIES":["Batteries", "battery", "Charger", "Chargers"],
    "MOTOR":["motor"],
    "BREAKER":["circuit breaker"],
    "DISTRIBUTING BOARD":["distributing board","plane", "switchboard", "panel board"],
     }