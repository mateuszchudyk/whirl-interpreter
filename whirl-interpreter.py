#!/usr/bin/env python

import sys
import whirl.program
import whirl.utils

def usage():
    print("Usage: whirl-sim.py [--help] sourcefile")
    exit(0)

def main():
    if len(sys.argv) <= 1:
        usage()

    sourcefile = ""
    for arg in sys.argv[1:]:
        if arg == "--help":
            usage()
        elif sourcefile == "":
            sourcefile = arg
        else:
            print("Unexpected parameter '{}'!".format(arg))
            print("")
            usage()

    source = whirl.utils.load_source_from_file(sourcefile)
    program = whirl.program.Program(source)
    program.run()

if __name__ == "__main__":
    main()
