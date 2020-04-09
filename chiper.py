def encrypt(st, cn=1):
    '''
    encrypt this code using consecutive cn's
    st: str to be encrypted
    cn (default = 1): first congruent loop counter to be added to ord(st) to encrypt
    '''
    chip = ''
    for char in st:
        char = ord(char)
        char = char + cn
        cn = cn + 1
        e_key = (chr(char))
        chip += e_key
    print(chip)
    return chip
def decrypt(enk,cu = 1):
    '''
This program decrypts the encrypted text.
Note: provide an encrypted key only.
    '''
    code = ""
    for i in enk:
        st = ord(i)
        st = st - cu
        string = chr(st)
        cu = cu + 1
        code += string
    print(code)
    return code
print("Completed Loading Chiper Module Successfully!!!")

