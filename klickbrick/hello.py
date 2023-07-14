import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="name of the person to greet")
    args = parser.parse_args()
    print(f'Hello{" " + args.name if args.name else ""}!')


if __name__ == "__main__":
    main()
