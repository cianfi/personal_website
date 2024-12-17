import json

username = 'cian@gmail.com'
password = 'test'

try:
    with open("personal_website/users.json", "r") as read:
        data = json.load(read)

except FileNotFoundError:
    data = {'users': []}
except json.JSONDecodeError:
    data = {'users': []}

if username not in [user['username'] for user in data['users']]:
    new_user = {
        "username": f"{username}",
        "password": f"{password}"
        }   
    print("USERNAME HASNT BEEN TAKEN") 
else:
    print("Username has been taken.")