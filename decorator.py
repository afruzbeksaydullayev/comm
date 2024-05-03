#Decorators
import time
# @timer
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#
#     return n * factorial(n - 1)
#
#
# print(factorial(5))


#Project match_password

import bcrypt


def hash_password(raw_password):
    encoded_password = raw_password.encode('utf-8')
    salt = bcrypt.gensalt(4)
    return bcrypt.hashpw(encoded_password, salt)


def check_password(raw_password, hashed_password):
    encoded_password = raw_password.encode('utf-8')
    return bcrypt.checkpw(encoded_password, hashed_password)

