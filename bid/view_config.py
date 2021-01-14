import sqlite3

DB_location="/srv1/process/tender.db"

conn = sqlite3.connect(DB_location,check_same_thread=False)
cur = conn.cursor()

find_tender = "select * from tender where Category like \"%{0}%\""
monitering_tender = "SELECT * FROM tender where InputTime like \"%{0}%\""
detail_tender = "select * from tender where InputTime like \"%{0}%\""

cats_analogue={"TRANSFORMER":["converter","transformer"],
         "SWITCH GEARS":["switch"],
         "OLBS":["olbs","oil Immersed Loadbreak Switch","Switch","Loadbreak","Load break","breaker"],
         "CABLE":["cable", "conductors", "insulating", "wire", "cables"],
         "INSULATOR":["insulator", "electrical insulator","Ceramic insulator"],
         "ARRESTOR":["arrester","Surge","lightning","surge diverter", "diverter", "protect", "protector", "Lightning rod"],
         "FUSES":["fuse", "fusing", "fuse-base", "fuse-link", "drop-out", "fuse-carrier", "fuse-element", "melt", "cos", "cut", "cutout", "holder"],
         "OCR":["ocr", "protective", "relay", "power", "Power","current", "overcurrent", "digital", "protection", "microprocessor"],
         "UPS":["ups", "load"],
         "CONSTRUCTION":["construction"],
         "Boundary wall":["wall"],
         "CIRCUIT":["circuit"],
         "FILLIMG":["filling"],
         "FLOORING":["flooring"],
         "BUILDING":["building"],
         "STATION":["station"],
         "TIRE":["tire","tires","tire","tires"],
         "TUBE":["tube"],
         "SERVICE":["service"],
         "PLANT":["plant"],
         "RECORD":["record"],
         "SCANNING":["scanning"],
         "METER":["meter"],
         "EQUIPMENT":["equipment"],
         "BRACKET":["bracket"],
         "DISPLAY":["display", "moniter"],
         "DISTRIBUTION LINE":["distribution line"],
         "RECLOSER":["recloser"],
         "PARTS":["parts"],
         "SHOCKS":["shock"],
         "DETAILING":["detailing"],
         "ENGINE":["engine"],
         "TANK":["tank"],
         "CAMERA":["camera"],
         "TONER CARTRIDGE":["toner","cartridge"],
         "TELEPHONE":["telephone"],
         "OUTLET":["outlet","extention"],
         "STEEL":["steel"],
         "POLE":["pole"],
         "GAUGE":["gauge"],
         "PAD":["pad"],
         "STICKER":["sticker"],
         "PEN":["pen"],
         "PAPER":["paper"],
         "STAMP":["stamp"],
         "BRUSH":["brush"],
         "APPLIANCES":["appliances"],
         "AIRCONDITION":["aircondition"],
         "HIGHLIGHTER":["highlighter"],
         "GENERATOR":["generator"," generating","dynamo"],
         "BATTERIES":["Batteries", "battery", "Charger", "Chargers"]
         }  