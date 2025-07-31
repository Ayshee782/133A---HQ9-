def output(p: str)->str:
    for char in p:
         if char in {'H', 'Q', '9'}:
            return "YES"
    return "NO"
p = input()
print(output(p))
