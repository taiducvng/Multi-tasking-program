
def hashDB(s):
    sum = -2971215073
    for i in s:
        sum = sum*31 + int(ord(i))
    return sum % 87178291199
