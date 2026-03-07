
#modules for password encryption
import random
import string

#db of users
database = {}
#db format: database = {username: {password: "password"}, 
#                                  key:{"scrambled key"}}



#encryption process
def encrypt(password):
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

        return encrypted_pass, key



#decryption process
def decrypt(encrypted_pass, key):
        #decrypt
        characters = list(string.punctuation + string.digits + string.ascii_letters + " ")
        decrypted_pass = ""
        for letter in encrypted_pass:
                index = key.index(letter)
                decrypted_pass += characters[index]
        return decrypted_pass


def signup():
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        encrypted_pass, key = encrypt(password)
        database[username] = {"password": encrypted_pass,
                                "key": key}
        
        print(f"Hello, {username}, you have successfully created your account!")


signup()
