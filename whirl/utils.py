import re

def load_source_from_file(filename):
    """
    Load source code, remove all lines starts with // and remove all characters
    that are not 0 or 1.
    """

    with open(filename, 'r') as file:
        code = file.read()
        code = re.sub(r"^//.*", "", code, flags=re.MULTILINE)
        code = re.sub("[^01]", "", code)

    return code
