import yaml
import json

with open('order.json') as f:
    templates = yaml.safe_load(f)
    print(templates)
    print(f"Order number: {templates['invoice']}")
    print(f"Delivery address: {templates['ship-to']['address']['lines']}")
    print(f"Package 1: {templates['product'][0]}")
    print(f"Package 2: {templates['product'][1]}")


def create_json():
    with open('order.json', 'r') as file:
        templates1 = yaml.safe_load(file)

    with open('order.json', 'w') as json_file:
        print(json.dump(templates1, json_file))


def create_yaml():
    reg_yaml = """
    first_name: 'Yaroslav'
    last_name : 'Lukashevich'
    email     : 'Hello_World@gmail.com'
    country   : 'Belarus'
    """
    templates2 = yaml.safe_load(reg_yaml)
    with open('reg.yaml', 'w') as file:
        yaml.dump(templates2, file)
