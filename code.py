def encode(decoded_password):
    global encoded_password
    encoded_password = ''
    for character in decoded_password:
        encoded_character = int(character)
        encoded_character += 3
        encoded_character = encoded_character % 10 # remove 10 if value greater than 9
        encoded_password += str(encoded_character)
    return encoded_password

def decode(encoded):
    decoded = ""
    for x in str(encoded):
        decoded_char = (int(x) - 3)
        if decoded_char < 0:
            decoded_char += 10
        decoded += str(decoded_char)
    return decoded


if __name__ == '__main__':
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        user_input = input('Please enter an option: ')
        if user_input == '1':
            decoded_password = input('Please enter your password to encode: ')
            encoded_password = encode(decoded_password)
            print('Your password has been encoded and stored!\n')
        elif user_input == '2':
            print(f'The encoded password is {encoded_password}, '
                  f'and the original password is {decode(encoded_password)}.\n')
        elif user_input == '3':
            break
        else:
            break
