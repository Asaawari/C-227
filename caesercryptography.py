print("Welcme to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("Encryption has started")
    msg = input("Enter your message")
    key = int(input("Enter key(1-94):"))
    encryptedText = ""
    for i in range(len(msg)):
        temp = (ord(msg[i])+key)
        if (temp>126):
            temp = temp - 127 + 32
        encryptedText += chr(temp)
    print("The encrypted text is - "+encryptedText)

def decryption():
    print("Decryption has started")
    print("Message can only be lowercase or uppercase alphabet")
    encryption_message = input("Enter encrypted text: ")
    decryptedText = int(input("Enter key(1-94): "))
    decrypted_text = ""
    for i in range(len(encryption_message)):
        temp = (ord(encryption_message[i])-decryptedText)
        if (temp<32):
            temp = temp+127-32
        decrypted_text += chr(temp)
    print("The decrypted text is - "+decrypted_text)

        
if __name__ == "__main__":
    main()