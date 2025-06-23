import json

class Student(object):
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f'{self.name} {self.age} {self.address}'

    def to_dict(self):
        return {'name': self.name, 'age': self.age, 'address': self.address}

def main():
    list_data = [
        {'name': 'Nguyen', 'age': 28, 'address': 'Da Nang'},
        {'name': 'Phuc', 'age': 31, 'address': 'Quang Nam'}
    ]

    new_data = {'name': 'Minh', 'age': 29, 'address': 'Da Nang'}

    with open('data.json', 'w') as file:
        json.dump(list_data, file, indent=4)
        print("✅ Ghi file lần 1 thành công")

    with open('data.json', 'r') as file:
        data = json.load(file)
        print("📖 Đọc file:")
        for s in data:
            print(s)

    data.append(new_data)

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
        print(" Ghi file lần 2 (có thêm dữ liệu) thành công")

    with open('data.json', 'r') as file:
        data = json.load(file)
        print(" Đọc lại file sau khi thêm dữ liệu:")
        for s in data:
            print(s)

if __name__ == '__main__':
    main()
