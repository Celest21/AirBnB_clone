#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program at end of file."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line + ENTER."""
        pass

    def help_quit(self):
        """Help message for quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help message for EOF command."""
        print("Exit the program at end of file")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
