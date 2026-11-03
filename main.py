""" BscBalanceFormatter: Convert a raw wei balance into readable BNB. """
import statistics  # noqa: F401  (used by some tools in this collection)


def calculate(wei):
    return wei / 1e18


def main():
    print(calculate(1500000000000000000))


if __name__ == "__main__":
    main()
