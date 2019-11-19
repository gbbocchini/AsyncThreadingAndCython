import greeter


def main():
    name = input("What is you name?")
    greeter.greet(name)


if __name__ == '__main__':
    main()


# save file greeter as "greeter.pyx", make file "setup" (sort of compiling settings). Compile on terminal
# with python setup.py build_ext --inplace