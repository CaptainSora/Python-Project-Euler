f = open('p059_cipher.txt', 'r')

encrypted = f.read().split(',') # something something change to string
f.close()
msg_len = len(encrypted)

for key1 in range(97, 123):
    for key2 in range(97, 123):
        for key3 in range(97, 123):
            key = [key1, key2, key3]
            decrypted = ""
            for index in range(msg_len):
                decrypted += chr(int(encrypted[index]) ^ key[index % 3])
            if " the " in decrypted and " and " in decrypted:
                print("Probable key: ", chr(key1), chr(key2), chr(key3))
                print("Decrypted message: ", decrypted)
                print("Sum: ", sum([ord(x) for x in decrypted]))