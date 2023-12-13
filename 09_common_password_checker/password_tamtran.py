

with open('passwords.text','r') as f:
    data = f.readlines()

passwords = [i.strip() for i in data]

password = input('Please enter a password >> ')
common = False

for i in passwords:
    if password == i:
        common = True
        break

if common == True:
    print(f'The password {password} is too common!')
else:
    print(f'The password {password} is good!')