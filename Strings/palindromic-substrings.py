def extractandcount(i, j, s):
    length = len(s)
    count = 0

    while i >= 0 and j < length and s[i] == s[j]:
        i -= 1
        j += 1
        count += 1

    return count


s = input("Enter string : ")

print(sum(extractandcount(i, i, s) + extractandcount(i, i + 1, s) for i in range(len(s))))
