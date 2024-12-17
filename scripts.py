import json

def add(num1: str, num2: str) -> str:
    add = int(num1) + int(num2)
    return f"{add}"

def user(username:str, password: str): 
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
    else:
        return "Username has been taken."

    data["users"].append(new_user)

    with open("personal_website/data/users.json", "w") as write:
        json.dump(data, write, indent=4)
        
    return "Written to file"