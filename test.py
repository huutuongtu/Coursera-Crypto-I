def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

# A1 = '9f970f4e 932330e4'
# A2 = '6068f0b1 b645c008'
# A3 = '7c2822eb fdc48bfb'
# A4 = '325032a9 c5e2364b'
# A5 = '4af53267 1351e2e1'
# A6 = '87a40cfa 8dd39154'
# A7 = '2d1cfa42 c0b1d266'
# A8 = 'eea6e3dd b2146dd0'
# print("A:" + strxor(A1,A2))
# print("B:" + strxor(A3,A4))
# print("C:" + strxor(A5,A6))
# print("D:" + strxor(A7,A8))
print(strxor('5','9'))