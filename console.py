#!/usr/bin/python3
"""
This is a simple Python3 code snippet
"""


import cmd


class HbnbConsole(cmd.Cmd):
    """
    This class handles the command line instance for our HBNB clone
    """
    prompt = '(hbnb) '

    def do_exit(self, line):
        """
        This function handles exit
        """
        return True


if __name__ == "__main__":
    HbnbConsole().cmdloop()
