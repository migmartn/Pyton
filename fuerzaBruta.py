import itertools
import string

def brute_force(target_password):
    characters = string.ascii_lowercase + string.digits
    password_length = 4
    combinations = itertools.product(characters, repeat=password_length)
    for attempt in combinations:
        current_attempt = ''.join(attempt)
        if current_attempt == target_password:
            return current_attempt 
        return None

i = 0
while i == 0 :
    target_password = "abcd"
    result = brute_force(target_password)
    if result:
        i = 1
        print(f"Contrasena encontrada: {result}")
        
    else:
        print(result)
        print("Contrasena no encontrada")
        print(" ") 
        print(" ") 
        print(" ")