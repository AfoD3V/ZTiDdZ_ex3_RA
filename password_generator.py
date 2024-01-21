import random

def pass_gen() -> str:
    pass_length = random.randint(8, 16)
    random_char = ["!", "#", "$", "%", "&", "?"]
    password = ""
    for char in range(pass_length):
        if char < int(pass_length * 0.25):
            password += chr(random.randint(48, 57))
        elif char < int(pass_length * 0.5):
            password += chr(random.randint(65, 90))
        elif int(pass_length * 0.5) < char < int(pass_length * 0.75):
            password += chr(random.randint(97, 122))
        else:
            password += random_char[random.randint(0, 5)]

    password = [x for x in password]
    random.shuffle(password)

    return "".join(password)


print(pass_gen())
