import sqlite3
import csv
import os

# Function to get list of people aged 50 or older
def get_old_people():
    """Query database for people aged 50 or older."""
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    cur.execute("SELECT name, age FROM people WHERE age >= 50")
    old_people = cur.fetchall()
    con.close()
    return old_people

# Function to print names and ages of old people
def print_name_and_age(old_people_list):
    """Print names and ages of old people."""
    for person in old_people_list:
        print(f"{person[0]} is {person[1]} years old.")

# Function to save names and ages of old people to a CSV file
def save_name_and_age_to_csv(old_people_list, file_path):
    """Save names and ages of old people to a CSV file."""
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])
        writer.writerows(old_people_list)

# Main function to coordinate the data retrieval, display, and saving
def main():
    old_people_list = get_old_people()
    print_name_and_age(old_people_list)
    
    # Determine the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the path for the CSV file
    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    
    # Save the old people data to CSV
    save_name_and_age_to_csv(old_people_list, old_people_csv)

# Ensure the script runs the main function if executed directly
if __name__ == "__main__":
    main()
