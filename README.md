#  Mini Database — Built from Scratch

A simple database engine built from scratch in Python —
no SQLite, no ORM, no external libraries whatsoever.
Stores data in JSON format on disk, just like a mini MongoDB.

##  Features
- CREATE and DROP tables
- INSERT rows with auto-incrementing IDs
- SELECT all rows from a table
- FILTER rows by any field (like WHERE in SQL)
- UPDATE rows by ID
- DELETE rows by ID
- COUNT rows in a table
- Persistent storage — data saved to disk as JSON
- Data survives restarts (loaded back on startup)

##  What I learned
- How databases store and retrieve data
- How indexing and row IDs work
- How data is persisted to disk
- Difference between SQL and NoSQL storage models
- How to design a clean Python API from scratch

##  How to run
python main.py

##  Tech
- Python 3
- Built-in json and os modules only
- Zero external libraries
