
def computepay(h, r):
    fh = float(h)
    fr = float(r)
    if fh > 40:
        p = (fh - 40) * 1.5 * fr + 40 * fr
    else:
        p = fh * fr
    return p

h = input("Enter Hours:")
r = input("Enter Rate:")
p = computepay(h, r)
print("Pay", p)