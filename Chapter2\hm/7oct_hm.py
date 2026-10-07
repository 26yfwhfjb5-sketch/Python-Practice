# 2-3 message
name = 'Arial'
print(f'Hello {name}, How are you?')

# 2-4 Cases
name1 = 'arial emi'
print(name1.lower())
print(name1.upper())
print(name1.title())

# 2-5 quotes
print('Someone once said,"Big money never comes clean."')

#2-6 quotes
famous_person = "Annoymous"
message = f'{famous_person} once said, "Big money never comes clean."'
print(message)

#2-7 stripping names
name2 = '\tArial Emi\n'
print(name2)
print(name2.lstrip())
print(name2.rstrip())
print(name2.strip())

# 2-8 File Extentions
file_name = "python_notes.txt"
print(file_name.removesuffix(".txt"))

#2-9 Number '8'
print(5+3)
print(10-2)
print(4*2)
print(16/2)

#2-10 Favourite Number
favourite_number = 11
message = f"My favourite number is {favourite_number}."
print(message)