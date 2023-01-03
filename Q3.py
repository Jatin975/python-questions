def split_and_join(line):
    # write your code here
    myList = line.split()
    newStr = "-".join(myList)
    return newStr

result = split_and_join("this is a string")

print(result)
