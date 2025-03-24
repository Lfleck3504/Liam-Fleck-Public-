class PhoneBook:
   def __init__(self):
       self.contacts = {}


   def add_contact(self, name, number):
       self.contacts[name] = number
       print(f"Contact {name} added successfully.")


   def search_contact(self, name):
       return self.contacts.get(name, "Contact not found.")


   def delete_contact(self, name):
       if name in self.contacts:
           del self.contacts[name]
           print(f"Contact {name} deleted successfully.")
       else:
           print("Contact not found.")


   def display_contacts(self):
       if self.contacts:
           for name, number in self.contacts.items():
               print(f"{name}: {number}")
       else:
           print("Phonebook is empty.")


phonebook = PhoneBook()
phonebook.add_contact("abby", "123-456-7890")
phonebook.add_contact("allan", "987-654-3210")
print(phonebook.search_contact("abby"))  # Output: 123-456-7890
phonebook.display_contacts()
phonebook.delete_contact("abby")
phonebook.display_contacts()


