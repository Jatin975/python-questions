if __name__ == '__main__':
    s = input()
    alpha_num = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for letter in s:
        if letter.isalpha():
            alpha = True
        if letter.isalnum():
            alpha_num = True
        if letter.isdigit():
            digit = True
        if letter.islower():
            lower = True
        if letter.isupper():
            upper = True
    
    print(alpha_num)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
