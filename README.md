# Whirl Interpreter

[![Release](https://img.shields.io/github/release/mateuszchudyk/whirl-interpreter.svg?colorB=blue&style=for-the-badge)](https://github.com/mateuszchudyk/whirl-interpreter/releases)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?colorB=blue&style=for-the-badge)](./LICENSE)

## Overview

Simple `Whirl` programming language interpreter written in Python. To execute program, use script `whirl-interpreter.py`.

```
>> python3 whirl-interpreter.py --help
Usage: whirl-interpreter.py [--help] [--verbose] sourcefile

Options:
  --help     - show this message
  --verbose  - execute program in verbose mode (display information about every step)
```

During loading source code:
  - all lines starts with `//` are removed
  - all characters that are not `0` or `1` are removed

You can find more details about `Whirl` language at http://bigzaphod.github.io/Whirl/.

## License

All files except examples are under [MIT] license. Examples have specify its license and author in a comment at the beginning of file.

[MIT]: LICENSE
