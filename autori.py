inp = input()
print(inp[0], end="")  

for i in range(len(inp)):
    if inp[i] == "-":
        print(inp[i+1], end="")
