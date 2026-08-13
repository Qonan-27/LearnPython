# Di sini kita belajar fungsi

def jerry(func):
    def qonan(*a,**b):
        print("==========")
        print(f"Input: {a[1]}")
        print("==========")
        if func(*a) % 2 :
            n = func(*a) + 2
            return n
        else:
            return func(*a , **b)
    return qonan 
def jr():
    pass
@jerry
def jk(c,d):
    return c + d

y = jk(int(input("Input: ")),5)
print(f"Hasilnya adalah: {y}")