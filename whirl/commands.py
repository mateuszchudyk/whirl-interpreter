class CommandNoop:
    """ Do nothing. """

    def get_name(self):
        return "Noop"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("Noop")

class CommandExit:
    """ Terminates the program. """

    def get_name(self):
        return "Exit"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("Exit")
        program_state.set_program_position(-1)

class CommandOne:
    """ Set value to 1. """

    def get_name(self):
        return "One"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("{}: {} -> ".format(self.get_name(), program_state.get_value()), end = '')

        program_state.set_value(1)

        if verbose:
            print(program_state.get_value())

class CommandZero:
    """ Set value to 0. """

    def get_name(self):
        return "Zero"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("{}: {} -> ".format(self.get_name(), program_state.get_value()), end = '')

        program_state.set_value(0)

        if verbose:
            print(program_state.get_value())

class CommandLoad:
    """ Set value to memval. """

    def get_name(self):
        return "Load"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("{}: {} -> ".format(self.get_name(), program_state.get_value()), end = '')

        program_state.set_value(program_state.get_memval())

        if verbose:
            print(program_state.get_value())

class CommandStore:
    """ Sets memval to value. """

    def get_name(self):
        return "Store"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("{}: {} -> ".format(self.get_name(), program_state.get_memval()), end = '')

        program_state.set_memval(program_state.get_value())

        if verbose:
            print(program_state.get_memval())

class CommandPAdd:
    """ Adds value to the current program position pointer (a jump). """

    def get_name(self):
        return "PAdd"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("{}: p={} + v={} -> p=".format(self.get_name(), program_state.get_program_position(), program_state.get_value()), end = '')

        program_state.set_program_position(program_state.get_program_position() + program_state.get_value())

        if verbose:
            print(program_state.get_program_position())

class CommandDAdd:
    """ Adds value to the current memory position pointer (change memory location). """

    def get_name(self):
        return "DAdd"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("{}: m={} + v={} -> m=".format(self.get_name(), program_state.get_memory_position(), program_state.get_value()), end = '')

        program_state.set_memory_position(program_state.get_memory_position() + program_state.get_value())

        if verbose:
            print(program_state.get_memory_position())

class CommandLogic:
    """ If memval is 0, then value is set to 0. Otherwise, value is set to value AND 1. This is a logical AND. """

    def get_name(self):
        return "Logic"

    def execute(self, program_state, verbose = False):
        value = 1 if program_state.get_value() != 0 else 0
        memval = 1 if program_state.get_memval() != 0 else 0

        if verbose:
            print("{}: v={} and m={} -> v=".format(self.get_name(), value, memval), end = '')

        program_state.set_value(value * memval)

        if verbose:
            print(program_state.get_value())

class CommandIf:
    """ If memval is not 0, then add value to program position pointer (see PAdd). """

    def get_name(self):
        return "If"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("{}: m={}, p={} -> p=".format(self.get_name(), program_state.get_memval(), program_state.get_program_position()), end = '')

        if program_state.get_memval() != 0:
            program_state.set_program_position(program_state.get_program_position() + program_state.get_value())

        if verbose:
            print(program_state.get_program_position())

class CommandIntIO:
    """ If value is 0, set memval to integer number read from stdin. Otherwise print memval to stdout as an integer. """

    def get_name(self):
        return "IntIO"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("{}: v={}, m={} -> ".format(self.get_name(), program_state.get_value(), program_state.get_memval()), end = '')

        if program_state.get_value() == 0:
            program_state.set_memval(int(input("")))
            if verbose:
                print("m={}".format(program_state.get_memval()))
        else:
            if verbose:
                print("Print")
            print(int(program_state.get_memval()))

class CommandAscIO:
    """ If value is 0, set memval to ASCII character read from stdin. Otherwise print memval to stdout as an ASCII character. """

    def get_name(self):
        return "AscIO"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("{}: v={}, m={} -> ".format(self.get_name(), program_state.get_value(), program_state.get_memval()), end = '')

        if program_state.get_value() == 0:
            program_state.set_memval(ord(input("")))
            if verbose:
                print("m={}".format(program_state.get_memval()))
        else:
            if verbose:
                print("Print")
            print(chr(program_state.get_memval()))

class CommandAdd:
    """ Sets value to value plus memval. """

    def get_name(self):
        return "Add"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("{}: v={} + m={} -> v=".format(self.get_name(), program_state.get_value(), program_state.get_memval()), end = '')

        program_state.set_value(program_state.get_value() + program_state.get_memval())

        if verbose:
            print(program_state.get_value())

class CommandMult:
    """ Sets value to value multiplied by memval. """

    def get_name(self):
        return "Mult"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("{}: v={} + m={} -> v=".format(self.get_name(), program_state.get_value(), program_state.get_memval()), end = '')

        program_state.set_value(program_state.get_value() * program_state.get_memval())

        if verbose:
            print(program_state.get_value())

class CommandDiv:
    """ Sets value to value divided by memval. """

    def get_name(self):
        return "Div"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("{}: v={} + m={} -> v=".format(self.get_name(), program_state.get_value(), program_state.get_memval()), end = '')

        program_state.set_value(program_state.get_value() // program_state.get_memval())

        if verbose:
            print(program_state.get_value())

class CommandLess:
    """ If value is less than memval, then sets value to 1. Otherwise sets value to 0. """

    def get_name(self):
        return "Less"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("{}: v={}, m={} -> v=".format(self.get_name(), program_state.get_value(), program_state.get_memval()), end = '')

        program_state.set_value(1 if program_state.get_value() < program_state.get_memval() else 0)

        if verbose:
            print(program_state.get_value())

class CommandGreater:
    """ If value is greater than memval, then sets value to 1. Otherwise sets value to 0. """

    def get_name(self):
        return "Greater"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("{}: v={}, m={} -> {}".format(self.get_name(), program_state.get_value(), program_state.get_memval()), end = '')

        program_state.set_value(1 if program_state.get_value() > program_state.get_memval() else 0)

        if verbose:
            print(program_state.get_value())

class CommandEqual:
    """ If value is equal to memval, then sets value to 1. Otherwise sets value to 0. """

    def get_name(self):
        return "Equal"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("{}: v={}, m={} -> {}".format(self.get_name(), program_state.get_value(), program_state.get_memval()), end = '')

        program_state.set_value(1 if program_state.get_value() == program_state.get_memval() else 0)

        if verbose:
            print(program_state.get_value())

class CommandNot:
    """ If value is not 0, then sets value to 0. Otherwise sets value to 1. """

    def get_name(self):
        return "Not"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("{}: {} -> ".format(self.get_name(), program_state.get_value()), end = '')

        program_state.set_value(0 if program_state.get_value() != 0 else 1)

        if verbose:
            print(program_state.get_value())

class CommandNeg:
    """ Sets value to value multiplied by -1 (inverse). """

    def get_name(self):
        return "Neg"

    def execute(self, program_state, verbose = False):
        if verbose:
            print("{}: {} -> ".format(self.get_name(), program_state.get_value()))

        program_state.set_value(-program_state.get_value())

        if verbose:
            print(program_state.get_value())

