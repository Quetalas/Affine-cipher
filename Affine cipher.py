alphabet = {chr(i): i-65 for i in range(65, 91)}
numbers = {i-65: chr(i) for i in range(65, 91)}

def oppositenumber(num, mod):
    for i in range(2, mod):
        if num * i % mod == 1:
            return i


def isrightkey(key, mod):
    if oppositenumber(key, mod):
        return True
    return False


def encrypt(text, keya, keyb, alphabet=alphabet):
    mod = len(alphabet)
    #print('(x * {0} + {1}) % {2}'.format(keya, keyb, mod))
    res = []
    if not isrightkey(keya, mod):
        print('Error keya', keya)
        return 1
    for l in text:
        if not l.isalpha():
            res.append(l)
        elif l.islower():
            letter = l.upper()
            new_num = (alphabet[letter]*keya + keyb) % mod
            res.append(numbers[new_num].lower())
            #print(letter, '->', numbers[new_num].lower(),alphabet[letter], new_num)
        else:
            new_num = (alphabet[l] * keya + keyb) % mod
            res.append(numbers[new_num])
            #print(l, '->', numbers[new_num], alphabet[l], new_num)
    return ''.join(res)


def decrypt(text, keya, keyb, alphabet=alphabet):
    mod = len(alphabet)
    oppositekey = oppositenumber(keya, mod)
    if not oppositekey:
        print('Error keya', keya)
        return 1
    res = []
    for l in text:
        if not l.isalpha():
            res.append(l)
        elif l.islower():
            letter = l.upper()
            new_num = (oppositekey * (alphabet[letter] - keyb) ) % mod
            res.append(numbers[new_num].lower())
        else:
            new_num = (oppositekey * (alphabet[l] - keyb) ) % mod
            res.append(numbers[new_num])
    return ''.join(res)


if __name__ == '__main__':
    #print(alphabet)
    print(encrypt('Hello world',5,26))
    print(decrypt(encrypt('Hello world',5,26), 5, 26))