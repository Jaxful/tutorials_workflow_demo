"""
z = float(input("Input risk percentage: "))
x = int(input("Input maximum units of risk earned: "))
print()
tp = 0

for i in range(1, (x + 1)):
    if i == 4:
        p = z * i
        tp += p
        z = z - z
        print("Current units of risk earned:", i)
        print("Profit taken:", str(p) + "%")
        print("Total profit earned:", str(tp) + "%\n")
        print(z)
        break
    ta = z / 2
    z /= 2
    p = ta * i
    tp += p
    print("Current units of risk earned:", i)
    print("Profit taken:", str(p) + "%")
    print("Total profit earned:", str(tp) + "%\n")
    print(z)

print("Final profit earned:", str(tp) + "%")
end = input("Enter any input to end program: ")
"""
z = float(input("Input risk percentage: "))
x = int(input("Input maximum units of risk earned: "))
print()
tp = 0
y = 1/4*z

for i in range(1, (x + 1)):
    if i == 4:
        p = y * i
        tp += p
        print("Current units of risk earned:", i)
        print("Profit taken:", str(p) + "%")
        print("Total profit earned:", str(tp) + "%\n")
        break
    p = y * i
    tp += p
    print("Current units of risk earned:", i)
    print("Profit taken:", str(p) + "%")
    print("Total profit earned:", str(tp) + "%\n")

print("Final profit earned:", str(tp) + "%")
end = input("Enter any input to end program: ")
