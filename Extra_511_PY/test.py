def print_string():
    a = input("Insert a string: ")
    print(a)

print_string()

def sum_of_nums():
    a = input("First number: ")
    b = input("Second number: ")
    print(int(a)+int(b))

sum_of_nums()

def open_and_read_file():
    a = input("Filename: ")
    f = open(a, 'r')
    print(f.read())

open_and_read_file()

def pipe_open():
    a = input("Filename: ")
    f = open(a, 'r')
    for line in f:
        b = line.split("|")
        for x in b:
            print(x)

pipe_open()
