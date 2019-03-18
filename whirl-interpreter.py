#!/usr/bin/env python

import os
import sys
import whirl.program
import whirl.utils

def usage():
    print("Usage: {} [--help] [--verbose] sourcefile".format(os.path.basename(__file__)))
    print("")
    print("Options:")
    print("  --help     - show this message")
    print("  --verbose  - execute program in verbose mode (display information about every step)")
    exit(0)

def main():
    if len(sys.argv) <= 1:
        usage()

    sourcefile = ""
    verbose = False
    debug = False
    for arg in sys.argv[1:]:
        if arg == "--help":
            usage()
        elif arg == "--verbose":
            verbose = True
        elif sourcefile == "":
            sourcefile = arg
        else:
            print("Unexpected parameter '{}'!".format(arg))
            print("")
            usage()

    if not os.path.isfile(sourcefile):
        print("Cannot find source file '{}'!".format(sourcefile))
        exit(1)
    
    source = whirl.utils.load_source_from_file(sourcefile)
    program = whirl.program.Program(source)
    program.run(debug_verbose = verbose)

if __name__ == "__main__":
    main()
