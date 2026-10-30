n = int(input("Enter a number (try 8 or 12): "))
input("Which bits drop until the first 1 appears.  Press Enter ")
temp = n
pos = 0
while temp > 0:
    print(f"  binary:{bin(temp)[2:]}  last bit:{temp & 1}")
    if temp & 1:
        break
    pos += 1
    temp >>= 1
print(f"  first set bit in {n} is at position {pos}")