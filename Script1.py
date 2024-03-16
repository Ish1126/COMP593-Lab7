import sqlite3
from faker import Faker
from datetime import datetime

# Create faker object for generating fake data
fake = Faker()

# Function to generate fake data for a person
def generate_fake_person():
    return (
        fake.name(),
        fake.email(),
        fake.street_address(),
        fake.city(),
        fake.administrative_unit(),
        fake.text(),
        fake.random_int(min=1, max=100),  # Random age between 1 and 100
        datetime.now(),  # Current date and time for created_at
        datetime.now()   # Current date and time for updated_at
    )

# Function to create SQLite database and populate people table
def create_and_populate_database():
    # Connect to SQLite database (creates if not exists)
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    
    # Create people table if not exists
    create_ppl_tbl_query = """
    CREATE TABLE IF NOT EXISTS people
    (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    province TEXT NOT NULL,
    bio TEXT,
    age INTEGER,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
    );
    """
    cur.execute(create_ppl_tbl_query)

    # Generate and insert fake data for 200 people
    for _ in range(200):
        person_data = generate_fake_person()
        cur.execute("INSERT INTO people (name, email, address, city, province, bio, age, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", person_data)

    # Commit changes and close connection
    con.commit()
    con.close()

# Call the function to create and populate the database
create_and_populate_database()
