def mutate_string(string, position, character):
    newStr = string[:position] +character+string[position+1:]
    return newStr

result = mutate_string("abracadabra", 5,"k")
print(result)