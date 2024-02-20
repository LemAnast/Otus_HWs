import csv
import json


from HW_4 import BOOKS_CSV
from HW_4 import USERS_JSON
from HW_4 import RESULT_JSON_W


with open(USERS_JSON, 'r') as f:
    users = json.load(f)
    result = []
    for user in users:
        person = {}
        person["name"] = user["name"]
        person["gender"] = user["gender"]
        person["address"] = user["address"]
        person["age"] = user["age"]
        result.append(person)


books = []
with open(BOOKS_CSV, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        books.append(row)


num_users = len(users)
num_books = len(books)
books_per_user = num_books // num_users
remaining_books = num_books % num_users


for i, user in enumerate(result):
    user["books"] = books[i * books_per_user:(i + 1) * books_per_user]
    if i < remaining_books:
        user["books"].append(books[num_users * books_per_user + i])


with open(RESULT_JSON_W, 'w') as f:
    s = json.dumps(result, indent=4)
    f.write(s)
