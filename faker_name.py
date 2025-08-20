# Generate Faker Name
from faker import Faker
fake = Faker()

for _ in range(250):
    with open("faker_names.txt", "a") as f:
        f.write(f"{fake.name()}\n")
