import json

def main():
    data_json = """
    [
    {"id":5,"name": "Nguyen", "age": 28, "address": "Da Nang"},
    {"id":6,"name": "Phuc", "age": 31, "address": "Quang Nam"}
    ]
    """

    data_array = json.loads(data_json)
    for item in data_array:
        print(item)


if __name__ == '__main__':
    main()



