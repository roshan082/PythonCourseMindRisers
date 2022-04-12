# break 
# --> to stop iteration 
x = 5
while x == 5:
    print(x)
    break

i = 0
while i <= 30:
    if i%2 == 0 and i == 10:
        break
    i += 1
    print(i)

# continue
# --> to continue iteration

i = 0
while i <= 50:
    if i // 2 == 3:
        print(i)
        continue
    if i // 2 == 7:
        print(i)
        break
    i += 1
    print(i)
# pass
# --> ignore the statement

i = 0
while i <= 20:
    if i == 10:
        pass
    else:
        print(i)
    i += 1