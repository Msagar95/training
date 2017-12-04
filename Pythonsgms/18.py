n=int(input("Enter the decimal number: "))

def decimalConvert(n,base):
    s = ""
    if base < 10:
        while int(n) > 0:
            s = s + str(n % base)
            n /= base
            n = int(n)
    else:
        while int(n) > 0:
            t=n
            t %= 16
            if t<10:
                x=t
            else:
                x=t+55              #remainder needs to be converted to hexadecimal ASCII but subtracted by 5
                x=chr(x)
            s = s + str(x)     #ASCII value of A = 65
            n /= 16
            n = int(n)
    s = s[::-1]
    return s

print(n, "in binary: ", decimalConvert(n,2))
print(n, "in octal: ", decimalConvert(n,8))
print(n, "in hexadecimal: ", decimalConvert(n,16))