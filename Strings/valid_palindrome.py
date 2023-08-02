def palindrome(st):
    res = ("".join(i for i in st if i.isalnum())).lower()
    return res == res[::-1]

palindrome("gadag)!@")