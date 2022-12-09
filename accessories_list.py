import sqlite3

accessories = [
  "helmet",
  "bottle cage",
  "bike light",
  "lock",
  "mittens",
  "bike saddle",
  "hand pump",
  "mudguard",
  "seat post clamp",
  "Bike pannier",
  "horn",
  "stand",
  "water pouch",
  "onion",
  "Short-sleeve jersey",
  "floor pump",
  "padded cycling shorts",
  "seatpost",
  "smartphone bracket",
  "frame bag",
  "luggage rack",
  "saddle bag",
  "saddle cover",
  "turbo trainer",
  "backpack",
  "bike computer",
  "bike stabiliser",
  "carry case",
  "handlebar bag",
  "pedal",
  "noodles",
  "lentils",
  "rearview mirror",
  "sensor",
  "water bag nozzle",
  "watertight pocket",
  "wheel axle",
  "wheel riser block",
  "doodad straps"
  
]

accessories = sorted(accessories)

connection = sqlite3.connect("accessory_list.db")
cursor = connection.cursor()

cursor.execute("create table accessories (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
for i in range(len(accessories)):
  cursor.execute("insert into accessories (name) values (?)",[accessories[i]])
  print("added ", accessories[i])

connection.commit()
connection.close()