import sqlite3

DB_location="tender.db"

conn = sqlite3.connect(DB_location,check_same_thread=False)
cur = conn.cursor()

find_tenders = "select * from tenders where bid_descriptions like \"%{0}%\""
monitering_tenders = "SELECT COUNT(DB_table_name) as cnt, DB_table_name, input_time FROM 'tenders' where input_time like \"%2020-09-12%\"  GROUP BY DB_table_name"
total_qty = "SELECT COUNT(DB_table_name) from 'tenders' where input_time like \"%2020-09-12%\" "
all_tenders = "SELECT COUNT(DB_table_name), DB_table_name, max(input_time) from 'tenders' GROUP BY DB_table_name"
all_total = "select count(*) as cnt from 'tenders'"
detail_tenders = "select * from tenders where input_time like \"%{0}%\""

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