#!/usr/bin/python3
""" Nameless module for Console class """
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """A HBNBCommand class.

    Args:
        cmd module's Cmd class it is inheriting from

    Returns:
        Nothing
    """
    intro = ''
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exits the console
        """
        return True

    def do_help(self, arg):
        """Prints out the help menu
        """
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit\n")

    def do_quit(self, arg):
        """Quits the console
        """
        return True

    def emptyline(self):
        """Handles empty or whitespace input and overwrites the parent class emptyline method """
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
