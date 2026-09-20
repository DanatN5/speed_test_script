import argparse


class Parser:

    def parse(self):
        parser = argparse.ArgumentParser()

        parser.add_argument("url")
        parser.add_argument(
            "-n",
            "--requests",
            type=int,
            default=10,
        )

        return parser.parse_args()