def add_contact(contacts, name, phone, email):
    contact = {"name": name, "phone": phone, "email": email,"favorite": False}
    contacts.append(contact)
    print(f"Contact {name} added successfully")
    return

def show_contacts(contacts):
    print("\nContacts list:")
    for index, contact in enumerate(contacts, 1):
        favorite = ""
        if contact["favorite"] == True:
            favorite = "☆"
        print(f"{index}. Name: {contact['name']} | Phone: {contact['phone']} | E-mail: {contact['email']} | Favorite: [{favorite}]")
    return

def update_contacts(contacts, index, new_name, new_phone, new_email):
    if new_name != "":
        contacts[index - 1]["name"] = new_name
    if new_phone != "":
        contacts[index - 1]["phone"] = new_phone
    if new_email != "":
        contacts[index - 1]["email"] = new_email
    print(f"Task {index}, updated to {new_name}")

def fav_unfav_contacts(contacts, index):
    if contacts[index - 1]["favorite"] == False:
        contacts[index - 1]["favorite"] = True
        message = "favorited"
    else:
        contacts[index - 1]["favorite"] = False
        message = "unfavorited"
    print(f"Contact {index} {message}")

def show_contacts_favorited(contacts):
    print("\nContacts list:")
    for index, contact in enumerate(contacts, 1):
        favorite = ""
        if contact["favorite"] == True:
            favorite = "☆"
            print(f"{index}. Name: {contact['name']} | Phone: {contact['phone']} | E-mail: {contact['email']} | Favorite: [{favorite}]")
    return

def delete_contact(contacts, index):
    contacts.remove(contacts[index - 1])


contacts = []
while True:
    print("\nContact book manager menu:")
    print("1. Add contact;")
    print("2. Show contacts;")
    print("3. Update contact;")
    print("4. Fav/unfav contact;")
    print("5. Show fav's contacts;")
    print("6. Delete contact;")
    print("7. Leave;")

    option = int(input("Choose your option: "))

    if option == 1:
        name = input("Type the contact name: ")
        phone = input("Type the contact phone: ")
        email = input("Type the contact email: ")
        add_contact(contacts, name, phone, email)

    elif option == 2:
        show_contacts(contacts)

    elif option == 3:
        show_contacts(contacts)
        index = int(input("Wich contact you want to update? "))
        new_name = input("What is the name you want this contact to have now? Enter to skip ")
        new_phone = input("What is the phone you want this contact to have now? Enter to skip ")
        new_email = input("What is the e-mail you want this contact to have now? Enter to skip ")
        update_contacts(contacts, index, new_name, new_phone, new_email)
        show_contacts(contacts)

    elif option == 4:
        show_contacts(contacts)
        index = int(input("Wich contact you want to favorite/unfavorite? "))
        fav_unfav_contacts(contacts, index)

    elif option == 5:
        show_contacts_favorited(contacts)

    elif option == 6:
        show_contacts(contacts)
        index = int(input("Wich contact you want to delete? "))
        delete_contact(contacts, index)

    elif option == 7:
        break
