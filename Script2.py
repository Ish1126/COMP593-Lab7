import sqlite3
import csv

# Function to query database for people aged 50 or older
def query_old_people():
    # Connect to SQLite database
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()

    # Execute SQL query to select name and age of people aged 50 or older
    cur.execute("SELECT name, age FROM people WHERE age >= 50")

    # Fetch all query results
    old_people = cur.fetchall()

    # Print names and ages of old people
    for person in old_people:
        print(f"{person[0]} is {person[1]} years old.")

    # Save old people data to CSV file
    with open('old_people.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])
        writer.writerows(old_people)

    # Commit changes and close connection
    con.commit()
    con.close()

# Call the function to query old people and save them to a CSV file
query_old_people()
