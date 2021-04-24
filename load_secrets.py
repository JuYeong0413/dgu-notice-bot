"""
This file defines function for loading token value from JSON file.
"""
import json

def get_token():
    """
    Load discord bot token from secrets.json.
    :return str: 'token' variable from secrets.json
    """
    with open('./secrets.json', 'r') as file:
        json_data = json.load(file)

    file.close()
    return json_data['token']
