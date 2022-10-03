def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

A1 = '9f970f4e 932330e4'
A2 = '6068f0b1 b645c008'
A3 = '5f67abaf 5210722b'
A4 = 'bbe033c0 0bc9330e'
A5 = '7c2822eb fdc48bfb'
A6 = '325032a9 c5e2364b'
A7 = '7b50baab 07640c3d'
A8 = 'ac343a22 cea46d60'
print(strxor(A1,A2))
# print(strxor(A3,A4))
# print(strxor(A5,A6))
# print(strxor(A7,A8))
# print(strxor('5','9'))