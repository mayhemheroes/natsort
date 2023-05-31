#!/usr/bin/env python3
import atheris
import sys
import fuzz_helpers


with atheris.instrument_imports():
    from natsort import natsorted
def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    natsorted(fuzz_helpers.build_fuzz_list(fdp, [str]))


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
