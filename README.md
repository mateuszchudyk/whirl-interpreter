# Whirl Interpreter

[![Release](https://img.shields.io/github/release/mateuszchudyk/whirl-interpreter.svg?colorB=blue&style=for-the-badge)](https://github.com/mateuszchudyk/whirl-interpreter/releases)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?colorB=blue&style=for-the-badge)](./LICENSE)

## Overview

Simple interpreter of `Whirl` programming language written in Python. To execute program, use script `whirl-interpreter.py`.

```
>> python3 whirl-interpreter.py --help
Usage: whirl-interpreter.py [--help] [--verbose] sourcefile

Options:
  --help     - show this message
  --verbose  - execute program in verbose mode (display information about every step)
```

Following rules define comments in source code:
  - all lines starts with `//`
  - all characters that are not `0` or `1`

You can find more details about `Whirl` language at http://bigzaphod.github.io/Whirl/.

## License

All files except examples are under [MIT] license. Each example have specify its license and author in a comment at the beginning of the file.

[MIT]: LICENSE
