from Sign_up import decrypt, database


def signin():
        username = input("Enter a username: ")
        password =  input("Enter a password: ")

        if username not in database:
                print("Username not found \n")
                return False
        
        stored_encrypted = database[username]["password"]
        stored_key = database[username]["key"]

        decrypted_pass = decrypt(stored_encrypted, stored_key)
        if password == decrypted_pass:
                print(f"Welcome {username} \n")
                return True
        else:
                print("Incorrect password \n")
                return False
