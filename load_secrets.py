import json

def get_token():
    with open('./secrets.json', 'r') as file:
        json_data = json.load(file)

    file.close()
    return json_data['token']
