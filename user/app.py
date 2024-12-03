import re
def get_username():
    
    username = input("enter username: ")
    
    if username[0].isdigit():
        print("username must not starts with digit")
    if not (5 <= len(username) <= 10):
        print("Invalid username: Length must be between 5 and 10 characters.")
        
    if not re.match("^[a-zA-Z0-9]+$", username):
        return "Valid Username"
    else:
        print (f"username accepted : {username}")
        
    
print(get_username())