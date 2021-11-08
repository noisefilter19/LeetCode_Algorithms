n = int(input("Nth term you want to find: "))
last=1
penultimate=1

if (n==1) or (n==2):
    print("1")
else:
    for count in range(2,n):
        term = last + penultimate
        penultimate = last
        last = term
        count += 1
    print(term)
