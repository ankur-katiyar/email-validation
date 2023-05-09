import csv
from faker import Faker

# Set up Faker to generate email addresses
fake = Faker()

# Set up the CSV file
filename = "email_addresses.csv"
headers = ["email"]
num_addresses = 1000

# Generate random email addresses and write to CSV file
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for _ in range(num_addresses):
        email_address = fake.email()
        writer.writerow([email_address])
