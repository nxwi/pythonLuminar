# Pass the key value into dictionary

def order(**kwargs):
    li= list(kwargs)
    li.sort()
    d={}
    for i in li:
        d.update({i: kwargs.get(i)})
    print(d)


order (b=2, c=3, a=1)