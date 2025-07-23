def caesar_cipher(text, key):
    result = ""
    # Loop through each character in the input string
    for char in text:
        # Check if the character is an alphabet
        if char.isalpha():
            # Get the ASCII code of the character
            ascii_code = ord(char)
            # Get the position of the character in the alphabet
            position = ascii_code - ord('a')
            # Shift the position by the key value
            new_position = (position + key) % 26
            # Get the ASCII code of the new character
            new_ascii_code = new_position + ord('a')
            # Append the new character to the result
            result += chr(new_ascii_code)
        else:
            # Append non-alphabetic characters as is
            result += char
    return result

# Get the input text and key from the user
text = input("Enter the text to encrypt: ")
key = int(input("Enter the key value: "))

# Encrypt the input text using the Caesar cipher
encrypted_text = caesar_cipher(text, key)

# Print the encrypted text
print("Encrypted text:", encrypted_text)
