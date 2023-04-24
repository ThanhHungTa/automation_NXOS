import hashlib

# Open the file in read mode
with open('password.txt', 'r') as file:
    # Read the entire contents of the file into a string
    password_read = file.read()
    #print(password)

def encode_password(password, shift):
    """
    Encodes a password using a Caesar cipher with a given shift value.
    
    Args:
        password (str): The password to be encoded.
        shift (int): The number of positions by which each letter is shifted in the alphabet.
        
    Returns:
        str: The encoded password.
    """
    encoded_password = ""
    for char in password:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encoded_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encoded_password += encoded_char
        else:
            encoded_password += char
    return encoded_password


def decode_password(password, shift):
    """
    Decodes a password using a Caesar cipher with a given shift value.
    
    Args:
        password (str): The password to be decoded.
        shift (int): The number of positions by which each letter is shifted in the alphabet.
        
    Returns:
        str: The decoded password.
    """
    decoded_password = ""
    for char in password:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decoded_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decoded_password += decoded_char
        else:
            decoded_password += char
    return decoded_password


# Example usage:
original_password = password_read
shift = 5

# Encode the password
encoded_password = encode_password(original_password, shift)
#print("Original password:", original_password)
#print("Encoded password:", encoded_password)

# Decode the password
decoded_password = decode_password(encoded_password, shift)
#print("Decoded password:", decoded_password)
