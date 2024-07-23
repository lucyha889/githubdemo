def encode_password(password):
    encode_password = ""
    for char in password:
        encode_char =  str((int(char) + 3) % 10)
        encode_password += encode_char
    return encode_password

def decode_password(password):
    decode_password = ""
    for char in password:
        decode_char = str((int(char) - 3) % 10)
        decode_password += decode_char
    return decode_password

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    option = input("\nPlease enter an option: ")

    if option == "1":
        password = input("Please enter your password to encode: ")
        encode_password = encode_password(password)
        print("Your password has been encoded and stored!\n")
    elif option == "2":
        if encode_password: 
            original_password = decode_password(encode_password)
            print(f"The encoded password is {encode_password}, and the original password is {original_password}.\n")
    elif option == "3":
        break