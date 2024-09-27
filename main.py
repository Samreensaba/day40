
nameCard = {"Name": "", "DOB": "", "Telephone": "", "Email": "", "Address": ""}

nameCard["Name"] = input("Name: ").strip().capitalize()
nameCard["DOB"] = input("Date of Birth: ").strip().capitalize()
nameCard["Telephone"] = input("Telephone: ").strip().capitalize()
nameCard["Email"] = input("Email: ").strip().capitalize()
nameCard["Address"] = input("Address: ").strip().capitalize()

print()
line = "--------------------------------------------------------"
print(f"{line}")
print(f"Here's your contact card")
print()
print(f"Name: {nameCard['Name']}")
print(f"DOB: {nameCard['DOB']}")
print(f"Telephone: {nameCard['Telephone']}")
print(f"Email: {nameCard['Email']}")
print(f"Address: {nameCard['Address']}")