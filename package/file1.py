# Di sini kita belajar fungsi

def jerry(func):
    def qonan(a,b):
        print("Input:",b)
        print("======")
        return func(a,b)
    return qonan

def jr():
    pass
@jerry
def jk(c,d):
    return c + d

y = jk(int(input("Input: ")),5)
print(f"Hasilnya adalah: {y}")