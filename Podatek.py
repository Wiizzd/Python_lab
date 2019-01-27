def percentage(percent, whole):
    return (percent * whole) / 100.0

print("Obliczanie podatku dochodowego")

umowa = (input("Wprowadź rodzaj umowy.\n p - umowa o pracę, z - umowa zlecenie\n Rodzaj umowy: "))
a = int(input("Wprowadź wynagrodzenie brutto: "))
q = percentage(9.76,a)
w = percentage(1.5,a)
r = percentage(2.45,a)
b = q + w + r
c = a - b
d = percentage(9,c)
e = percentage(7.75,c)
f = 111.25
g = round(a - f - b,0)
h = round(percentage(18,g) - 46.33 - e,0)
i = a - b - d - h
print("q: ", q)
print("w: ", w)
print("r: ", r)
print("b: ", b)
print("c: ", c)
print("d: ", d)
print("e: ", e)
print("f: ", f)
print("g: ", g)
print("h: ", h)

print(round(i,2))
