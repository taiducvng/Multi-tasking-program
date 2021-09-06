from Tools.secret import*

def checkDB_Login(a):
    file = open("src/Documents/log_sign.txt","r", encoding= "utf-8")
    for line in file:
        s = line.split("; ")
        if a[0] == str(s[1]) and a[1] == str(s[2].strip("\n")):
            file.close()
            return True
    return False

def checkDB_Sign(a):
    file = open("src/Documents/log_sign.txt","r", encoding= "utf-8")
    for line in file:
        s = line.split("; ")
        if a[1] == str(s[2].strip("\n")):
            file.close()
            return True
    return False



def encode(secret):
    key = "!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[]^_`abcdefghijklmnopqrstuvwxyz~"
    rotate_const = 13
    encoded = ""
    for c in secret:
        index = key.find(c)
        original_index = (index + rotate_const) % len(key)
        encoded = encoded + key[original_index]
    
    return str(hashDB(encoded))




