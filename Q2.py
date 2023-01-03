def swap_case(s):
    newStr = ""
    for letter in s:
        if letter.isupper():
            newStr += letter.lower()
        else:
            newStr += letter.upper()
    return newStr

result = swap_case("Www.HackerRank.com")

print(result)
