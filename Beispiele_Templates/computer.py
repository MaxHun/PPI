"""
Example code for object oriented programming.
Lecture: Einfuehrung in das wissenschaftliche Rechnen
Authors: Franz Bethke, Hella Rabus (2018)
"""

class Computer(object):
    """ This class is used to manage computers with different operating systems in a building.

    Attributes:
        sys (string): The operating system, that is currently run on the computer.
                      Should be one of the values `MAC`, `WINDOWS` or `LINUX`
        room (int): The room in which the computer is currently located.
        state (bool): The state of the computer.
                      False = The computer is turned off.
                      True = The computer is turned on.

        static all_computers (list of computers): A collection of all created computers.
    """

    all_computers = []

    def __init__(self, operating_system, room):
        """ Constructs a new computer.

        New computer will be turned off, i.e. state = False.

        Input:
            operating_system (string): The system, that the computer will be launched with.
                                       Should be one of the values `MAC`, `WINDOWS` or `LINUX`
            room (int): The room the computer will be set up in.
        """

        self.sys = operating_system
        self.room = room
        self.state = False

        Computer.all_computers.append(self)

    def change_room(self, new_room):
        """ Change the location of this computer to a new room.

        Input:
            new_room (int): the room this computer will be moved to

        Returns: None
        """

        self.room = new_room

    def toggle_state(self):
        """ Toggles the state of this computer.

        Input: -
        Returns: None
        """

        self.state = not self.state

    def __str__(self):
        """ Gives a string representation of this computer,
        that can be printed with `print()`.

        Input: -
        Returns: 
             (string) a representation of the object for the use with print()
        """

        result = "Der Computer\n"

        result += "\t- steht im Raum " + str(self.room) + ".\n"

        result += "\t- läuft mit "
        if self.sys == "MAC":
            result += "MAC-OS.\n"
        elif self.sys == "WINDOWS":
            result += "Windows.\n"
        elif self.sys == "LINUX":
            result += "Linux.\n"
        else:
            result += "einem unbekannten Betriebssystem.\n"

        result += "\t- ist derzeit "
        if self.state:
            result += "eingeschaltet."
        else:
            result += "ausgeschaltet."

        return result

    @staticmethod
    def get_computers_in(room):
        """ Collects all computers in a given room.

        Input:
            room (int): The room number.

        Returns:
            (list of computers): All computers in room `room`.

        """
        result = []
        for computer in Computer.all_computers:
            if computer.room == room:
                result.append(computer)
        return result

def main():
    """ Main function to test the Computer class.
    """

    cmp1 = Computer("LINUX", 1115)
    print(cmp1)
    cmp1.toggle_state()
    cmp1.change_room(2407)
    print(cmp1)

    print("\n==================\n")

    Computer("MAC", 2407)
    Computer("LINUX", 1115)

    my_computers = Computer.get_computers_in(2407)
    for computer in my_computers:
        print(computer)

if __name__ == "__main__":
    main()
