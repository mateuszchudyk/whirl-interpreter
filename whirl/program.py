import whirl.rings

class Program:
    def __init__(self, program):
        self.program = program
        self.memory = {}
        self.program_position = 0
        self.memory_position = 0

        self.rings = [
            whirl.rings.create_operations_ring(),
            whirl.rings.create_math_ring(),
        ]
        self.active_ring = 0

    def get_value(self):
        return self.rings[self.active_ring].get_value()

    def set_value(self, value):
        self.rings[self.active_ring].set_value(value)

    def get_memory_value(self):
        return self.memory.get(self.memory_position, 0)

    def set_memval(self, value):
        self.memory[self.memory_position] = value

    def get_program_position(self):
        return self.program_position

    def set_program_position(self, position):
        self.program_position = position

    def get_memory_position(self):
        return self.memory_position

    def set_memory_position(self, position):
        self.memory_position = position

    def __ring_name(self, ring):
        return "Operations" if ring == 0 else "Mathematics"

    def __ring_direction_name(self, direction):
        return "clockwise" if direction == 1 else "counter-clockwise"

    def run(self, debug_dump = False, debug_verbose = False):
        if not self.program:
            return

        previous_zeros = 0
        while self.program_position >= 0 and self.program_position < len(self.program):
            command = self.program[self.program_position]
            self.program_position += 1
            if command == '1':
                if debug_verbose:
                    print("Ring '{}' rotate {}: {} -> ".format(
                        self.__ring_name(self.active_ring),
                        self.__ring_direction_name(self.rings[self.active_ring].get_direction()),
                        self.rings[self.active_ring].get_operation().get_name()),
                        end = '')

                self.rings[self.active_ring].rotate()

                if debug_verbose:
                    print(self.rings[self.active_ring].get_operation().get_name())

                previous_zeros = 0
            else:
                if debug_verbose:
                    print("Ring '{}' change direction: {} -> ".format(
                        self.__ring_name(self.active_ring),
                        self.__ring_direction_name(self.rings[self.active_ring].get_direction())),
                        end = '')

                self.rings[self.active_ring].change_direction()

                if debug_verbose:
                    print(self.__ring_direction_name(self.rings[self.active_ring].get_direction()))

                if previous_zeros % 2 == 1:
                    if debug_verbose:
                        print("Execute ", end = '')
                    self.rings[self.active_ring].get_operation().execute(self, debug_verbose)

                    if debug_verbose:
                        print("Change active ring: {} -> ".format(self.__ring_name(self.active_ring)), end = '')

                    self.active_ring = (self.active_ring + 1) % len(self.rings)

                    if debug_verbose:
                        print(self.__ring_name(self.active_ring))

                previous_zeros += 1

            if debug_dump:
                self.dump()

    def dump(self):
        if not self.program:
            return

        print("================================================================================")
        print("Whirl Program Dump")
        print("================================================================================")
        print("Program ({}):".format(self.program_position))
        if self.program_position < 0 or self.program_position >= len(self.program):
            print("Done!")
        else:
            print("{}[{}]{}".format(self.program[:self.program_position], self.program[self.program_position], self.program[self.program_position+1:] if self.program_position < len(self.program) - 1 else ""))
        print("--------------------------------------------------------------------------------")
        print("Memory ({}):".format(self.memory_position))
        print(self.memory)
        print("--------------------------------------------------------------------------------")
        print("Active ring:", self.active_ring)
        print("--------------------------------------------------------------------------------")
        self.rings[0].dump()
        print("--------------------------------------------------------------------------------")
        self.rings[1].dump()
        print("================================================================================")
        print("")

