a = "Hello, I am Multiplication Table printer Program."
print(a.title())
n = int(input("Enter your integer Please: "))
for i in range(0, n+1):
    for j in range(1, 11):
        print(str(i) + " X " + str(j) + " = " + str(i * j))

    print("\n")