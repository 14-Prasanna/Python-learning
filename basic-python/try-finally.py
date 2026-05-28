try:
    fh = open("text.bin", "w")
    try:
        fh.write("This is my test file for exception handling")
    finally:
        print("going to close the file")
        fh.close()
except IOError:
    print("Error: cannot find file write data")
else:
    print("I will execute when no exception")
finally:
    print("I am always executing")