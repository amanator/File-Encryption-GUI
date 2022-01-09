from pathlib import Path

# CODE OF FILE_ENCRYPTION
#   code to encrypt file

# f = open("C:/Users/HP/Desktop/PYTHON/d.txt", "rt")
# string = list(f.read())
# encrypt = ''
# print(string)
# for lines in string:
#     if lines == "\t":
#         lines = 'a'
#     ascii = ord(lines)
#     ascii -= 10
#     ascii = chr(ascii)
#     encrypt = encrypt + ascii
#
# print(encrypt)
# f.close()
#
# f = open("d.txt", "wt")
# f.write(encrypt)
# f.close

#  CODES TO DECRYPT FILE
# f = open("d.txt", "rt")
# string = list(f.read())
# encrypt = ''
# for lines in string:
#     if lines == "\t":
#         lines = 'a'
#     ascii = ord(lines)
#     ascii += 10
#     ascii = chr(ascii)
#     encrypt = encrypt + ascii
#
# f.close()
#
# f = open("d.txt", "wt")
# f.write(encrypt)
# f.close
#

#   CODE TO FIND THE NAME OF WHICH FILE IS STORED
#     CODE of ENCRYPTION_SAVER

# a =  ''
# f = open("grt.txt", "r")
# for idx, line in enumerate(f):
#     a += line
#     a = a.split()
#     if a[0] == "email":
#         break
#     a = ''
# f.close()
# print(a)
#
# b = ''
# for i in range(1, len(a)):
#     b = b + ' ' + a[i]
# print(b)
