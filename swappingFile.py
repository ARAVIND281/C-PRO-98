def swapFileData():
    file_1 = input("enter files name")
    file_2 = input("enter files name")


    with open(file_1, 'r') as a:
    a = a.read()

	with open(file_2, 'r') as b:
    b = b.read()

    with open(file_1, 'w') as a:
    a.write(b)

    with open(file_2, 'w') as b:
    b.write(a)

swapFileData()
