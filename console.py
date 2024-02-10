#!/usr/bin/python3
"""The Command Line Interpreter."""

from models import *
import json
import cmd
import re

class HBNBCommand(cmd.Cmd):
    """Class that defines Airbnb clone public class instances."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Function handle end of file character (Ctrl+D)."""

        print()
        return (True)

    def do_quit(self, line):
        """Function that exits the shell in interactive mode."""

        return (True)

    def emptyline(self):
        """Function that does nothing on ENTER."""

        pass

    def do_create(self, line):
        """Create a new instance of a specified class."""

        args = re.split(r'[()]', line)
        args = [arg.strip() for arg in args if arg.strip()]

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in models.storage.CLASSES:
            print("** class doesn't exist **")
            return

        new_instance = eval(f"{class_name}()")
        models.storage.save()
        print(new_instance.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
