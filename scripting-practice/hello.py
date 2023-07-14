import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name")
    args = parser.parse_args()
    if args.name:
        print("Hello " + args.name)
    else:
        print("Hello")


main()
