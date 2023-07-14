import argparse


def hello(name):
    return f"Hello { name }!"


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subcommand", title="subcommands")

    hello_parser = subparsers.add_parser("hello", help="say hello")
    hello_parser.add_argument(
        "--name", default="World", help="name of the person to greet"
    )

    args = parser.parse_args()
    if args.subcommand == "hello":
        print(hello(args.name))


if __name__ == "__main__":
    main()
