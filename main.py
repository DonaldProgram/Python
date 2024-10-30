import time

# Ask the user for the password
user_password = input("Enter your password: ")

print()  # Line break

# Calculate the time taken by the program to find the password
start_time = time.time()  # Record the time at the start of the program

def display_time():
    end_time = time.time()  # Record the time at the end of the program
    # Display the time taken by the program
    print(f"TIME: Program completed in '{end_time - start_time:.4f}' seconds.")

# Test passwords
passwords_tested = 0  # Track the number of passwords tested

with open('Dict/dict.txt', 'r', encoding='latin-1') as file:
    for line in file:
        passwords_tested += 1
        # Remove any special characters from the password
        line = line.strip()

        # If the password is found
        if line == user_password:
            print("SUCCESS: The password has been found!")
            print()  # Line break
            display_time()  # Display the time taken by the program
            print(f"INFO: Total passwords tested: '{passwords_tested:,}'".replace(',', '.'))
            exit()  # Exit the program

# If the password is not found
print("FAILURE: The password was not found!")
print()
display_time()
print(f"INFO: Total passwords tested: '{passwords_tested:,}'".replace(',', '.'))

# Ajouter le mdp au dict
with open('Dict/dict.txt', 'a', encoding='latin-1') as file:
    file.write(f"{user_password}\n")
    print("Mot de passe ajouté à la base de donné.")