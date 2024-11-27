class InMemoryDB:
    def __init__(self):
        self._storage = {}
        self._transaction = {}
        # Flag to check if we in the middle of something rn
        self._in_transaction = False
    
    def get(self, key):
        """
        checks the temp stuff first cuz that's the new 
        """
        if self._in_transaction and key in self._transaction:
            return self._transaction[key]
        return self._storage.get(key, None)
        # pretty sure this was like one of my interview/leetcode style questions
    
    def put(self, key, val):
        if not self._in_transaction:
            raise Exception("start a transaction first")
        
        self._transaction[key] = val
    
    def begin_transaction(self):
        if self._in_transaction:
            raise Exception("already a transaction ip!!!")
        
        self._in_transaction = True
        self._transaction = {}
    
    def commit(self):
        if not self._in_transaction:
            raise Exception("bruh no transaction")
        
        # Update the main storage with our new changes (real ones only)
        self._storage.update(self._transaction)
        
        # Reset everything cuz we done here
        self._transaction = {}
        self._in_transaction = False
    
    def rollback(self):
        if not self._in_transaction:
            raise Exception("no transaction to rollback")
        
        self._transaction = {}
        self._in_transaction = False

'''
test code stuff. uncomment to try urself.
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
'''