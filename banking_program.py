
#modules for password encryption
import random
import string

#db of users
database = {}


#signup
username = input("Enter username: ")
password = input("Enter password: ")

def encrypt():
        global key
        global encrypted_pass
        global characters
        #encryption characters
        characters = list(string.punctuation + string.digits + string.ascii_letters + " ")
        #create a key to shuffle
        key = characters.copy()
        random.shuffle(key)
        
        encrypted_pass = ""
        #encrypt
        for letter in password:#goes through each letter in the password
                index = characters.index(letter) #finds that letter in the characters list
                encrypted_pass += key[index] #returns the same position from the key list

        return encrypted_pass


#storing the funciton into a variable so i can call it without printing it
password = encrypt()
database[username] = {
    "password": encrypted_pass,
    "key": key
}

def decrypt():
        #decrypt
        for letter in encrypted_pass:
                index = key.index(letter)
                password += characters[index]
        return password

decrypting = decrypt()

stored_pass = database[username][password]#accesses the database with the username key
stored_key = database[username][key]#accesses the encryption key of that password

