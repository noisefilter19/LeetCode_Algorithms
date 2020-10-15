def dup():
    t=[]
    p = []
    n = int(input())
    for i in range(n):
        x = int(input())
        p.append(x)
    for j in range(len(p)):
        for k in range(j+1, len(p)):
            if p[j].__eq__(p[k]):
                t.append(p[j])
    print(len(list(set(t))))

dup()
