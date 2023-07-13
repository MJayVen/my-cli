import fileinput
# This script strips out lines from a file that begin '##'
def main():
    for line in fileinput.input():
        if fileinput.isfirstline():
            print("<start of file '{0}'>".format(fileinput.filename()))
        if not line.startswith('##'):
            print(line, end="")
            if not line.endswith('\n'):
                print("\n")
main()


