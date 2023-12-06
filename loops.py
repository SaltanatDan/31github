x=6
while x<7:
    print(f"x= {x}")
    x +=1
else: print(f"x={x}. rabota zikla zavershena")
print("Rabota zavershena")

message = "I Love you"
for c in message:
    print(c)

n=0
while n<10:
    n += 1
    if n==6:
        break
    print(f"n={n}")

n=0
while n<10:
    n += 1
    if n==4:
        continue
    print(f"n={n}")