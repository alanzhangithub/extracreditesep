from dataprocessandstore_az import InMemoryDB
# test code stuff. uncomment to try urself.
db = InMemoryDB()

try:
    db.put("bread", 100)
except Exception as e:
    print(f"Caught these hands: {e}")

db.begin_transaction()
db.put("bread", 100) 
print(db.get("bread"))

db.commit()
print(db.get("bread"))  # now we got that bread (100)
