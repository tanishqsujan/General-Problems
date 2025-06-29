def substr(s1, s2):
    if s1 in s2:
        return s2.index(s1)
    return -1

if __name__ == "__main__":
    s1= "to"
    s2= "Welcome to Codingal"
    result= substr(s1, s2)
    if result == -1:
        print("Not Present")
    else:
        print("Present at index: " + str(result))