import whirl.commands

class Ring:
    def __init__(self, operations, position = 0, direction = 1, value = 0):
        self.operations = operations
        self.position = position
        self.direction = direction
        self.value = value

    def get_operation(self):
        return self.operations[self.position % len(self.operations)]

    def rotate(self):
        self.position += self.direction

    def get_direction(self):
        return self.direction

    def change_direction(self):
        self.direction = -self.direction

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def dump(self):
        print("Operation ({}):".format(self.position))
        print(self.get_operation().get_name())
        print("Direction:")
        print(self.direction)
        print("Value:")
        print(self.value)

def create_operations_ring():
    return Ring([
        whirl.commands.CommandNoop(),
        whirl.commands.CommandExit(),
        whirl.commands.CommandOne(),
        whirl.commands.CommandZero(),
        whirl.commands.CommandLoad(),
        whirl.commands.CommandStore(),
        whirl.commands.CommandPAdd(),
        whirl.commands.CommandDAdd(),
        whirl.commands.CommandLogic(),
        whirl.commands.CommandIf(),
        whirl.commands.CommandIntIO(),
        whirl.commands.CommandAscIO(),
    ])

def create_math_ring():
    return Ring([
        whirl.commands.CommandNoop(),
        whirl.commands.CommandLoad(),
        whirl.commands.CommandStore(),
        whirl.commands.CommandAdd(),
        whirl.commands.CommandMult(),
        whirl.commands.CommandDiv(),
        whirl.commands.CommandZero(),
        whirl.commands.CommandLess(),
        whirl.commands.CommandGreater(),
        whirl.commands.CommandEqual(),
        whirl.commands.CommandNot(),
        whirl.commands.CommandNeg(),
    ])

