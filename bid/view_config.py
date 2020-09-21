import sqlite3

DB_location="tender.db"

conn = sqlite3.connect(DB_location,check_same_thread=False)
cur = conn.cursor()

find_tenders = "select * from tenders where bid_descriptions like \"%{0}%\""

cats_analogue={"TRANSFORMER":["converter","transformer"],
         "SWITCH GEARS":["switch"],
         "OLBS":["olbs","oil Immersed Loadbreak Switch","Switch","Loadbreak","Load break","breaker"],
         "CABLE":["cable", "conductors", "insulating", "wire", "cables"],
         "INSULATOR":["insulator", "electrical insulator","Ceramic insulator"],
         "ARRESTOR":["arrester","Surge","lightning","surge diverter", "diverter", "protect", "protector", "Lightning rod"],
         "FUSES":["fuse", "fusing", "fuse-base", "fuse-link", "drop-out", "fuse-carrier", "fuse-element", "melt", "cos", "cut", "cutout", "circuit", "holder"],
         "OCR":["ocr", "protective", "relay", "power", "current", "overcurrent", "digital", "protection", "microprocessor"],
         "UPS":["ups", "load"],
         "BATTERIES":["Batteries", "battery", "Charger", "Chargers"]
         }