# extracreditesep

# In-Memory Database with Transaction Support

A Python implementation of an in-memory key-value database that supports atomic transactions.

## Setup & Requirements

- Python 3.6 or higher required
- No additional packages needed - the implementation uses only Python standard library

## How to Run

1. Clone this repo:
```bash
git clone https://github.com/alanzhangithub/extracreditesep.git
cd extracreditesep
```

2. Run the tests:
```bash
python3 tester.py
```

3. if u wanna use in your own code:
```python
from dataprocessandstore_az import InMemoryDB


# Create database instance
db = InMemoryDB()

# Start a transaction
db.begin_transaction()

# Add some data
db.put("A", 5)

# Commit changes
db.commit()

# Retrieve data
value = db.get("A")  # Returns 5
```

## Assignment Improvement Suggestions

for future version of this assignment, I recommends:

1. Add requirements for concurrent transaction support, which would better reflect real-world database systems and teach students about transaction isolation levels.

2. Include performance requirements and testing with large datasets to help students understand scalability considerations - this could involve timing measurements for operations and memory usage limits. Something like 1M transactions or something.

3. Add some type of suspicious transaction monitoring like fraud or attacks. It would be weird if out of a few transactions, there were some that were either SQL injection, or an absurd value or not allowed value or transactions.