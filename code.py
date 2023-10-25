def encode(decoded_password):
    global encoded_password
    encoded_password = ''
    for character in (decoded_password):
        encoded_character = int(character)
        encoded_character += 3
        encoded_password + str(encoded_character)
    return encoded_password


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


        if user_input == '2':
            print(f'The encoded password is {encode(decoded_password)}, and the original password is {decoded_password}.\n3')

