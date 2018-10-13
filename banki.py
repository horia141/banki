#!/usr/local/bin/python3

import argparse


DEFAULT_TECHFILE_PATH = "techfile.yaml"


def main():
    parser = argparse.ArgumentParser(
        prog="banki",
        description="Banki is a tool for managing your local development environment")
    parser.add_argument(
        "-f", "--techfile",
        action="store", default=DEFAULT_TECHFILE_PATH,
        help="The path to the banki techfile to use")

    subparsers = parser.add_subparsers(help="Sub-commands help")

    begin_subparser = subparsers.add_parser("begin", help="Activate a banki environment")
    end_subparser = subparsers.add_parser("end", help="Deactivate the banki environment")
    install_subparser = subparsers.add_parser("install", help="Install the tech stack for the current environment")
    run_subparser = subparsers.add_parser("run", help="Run a program in the current environment")

    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    main()
