import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

def add_contact():
    name = input("Введите имя и фамилию: ")
    phone = input("Введите номер(а) телефона: ")
    email = input("Введите email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    save_contacts(contacts)
    print("Контакт успешно добавлен!")

def view_contacts():
    for contact in contacts:
        print("Имя:", contact["name"])
        print("Телефон:", contact["phone"])
        print("Email:", contact["email"])
        print("--------------------")

def search_contact():
    keyword = input("Введите имя или фамилию для поиска: ")
    found_contacts = []
    for contact in contacts:
        if keyword.lower() in contact["name"].lower():
            found_contacts.append(contact)
    if found_contacts:
        print("Найденные контакты:")
        for contact in found_contacts:
            print("Имя:", contact["name"])
            print("Телефон:", contact["phone"])
            print("Email:", contact["email"])
            print("--------------------")
    else:
        print("Контакты с таким именем или фамилией не найдены.")

def update_contact():
    keyword = input("Введите имя или фамилию контакта для редактирования: ")
    found_contacts = []
    for contact in contacts:
        if keyword.lower() in contact["name"].lower():
            found_contacts.append(contact)
    if found_contacts:
        print("Найденные контакты:")
        for i, contact in enumerate(found_contacts):
            print(f"{i+1}. {contact['name']}")
        choice = int(input("Выберите номер контакта для редактирования: "))
        if choice in range(1, len(found_contacts)+1):
            contact = found_contacts[choice-1]
            print(f"Редактирование контакта: {contact['name']}")
            new_name = input("Введите новое имя: ")
            new_phone = input("Введите новый номер телефона: ")
            new_email = input("Введите новый email: ")
            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email
            save_contacts(contacts)
            print("Контакт успешно обновлен!")
        else:
            print("Некорректный выбор.")
    else:
        print("Контакты с таким именем или фамилией не найдены.")

def delete_contact():
    keyword = input("Введите имя или фамилию контакта для удаления: ")
    found_contacts = []
    for contact in contacts:
        if keyword.lower() in contact["name"].lower():
            found_contacts.append(contact)
    if found_contacts:
        print("Найденные контакты:")
        for i, contact in enumerate(found_contacts):
            print(f"{i+1}. {contact['name']}")
        choice = int(input("Выберите номер контакта для удаления: "))
        if choice in range(1, len(found_contacts)+1):
            contact = found_contacts[choice-1]
            contacts.remove(contact)
            save_contacts(contacts)
            print("Контакт успешно удален!")
        else:
            print("Некорректный выбор.")
    else:
        print("Контакты с таким именем или фамилией не найдены.")

def main():
    global contacts
    contacts = load_contacts()
    while True:
        print("Телефонный справочник")
        print("1. Просмотреть контакты")
        print("2. Добавить контакт")
        print("3. Поиск контакта")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            view_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break
        else:
            print("Некорректный выбор.")

if __name__ == "__main__":
    main()

