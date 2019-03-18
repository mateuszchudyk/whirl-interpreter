def load_source_from_file(filename):
    """
    Load source code, remove comments and whitespaces and check if the code
    contains only 0 and 1.
    """

    with open(filename, 'r') as file:
        result = ""
        for line in file.readlines():
            line = "".join(line.split())
            if line.find("//") >= 0:
                result += line[:line.find("//")]
            else:
                result += line
    
    for i in range(len(result)):
        if result[i] != "0" and result[i] != "1":
            return None

    return result
