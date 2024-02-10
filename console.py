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
        """Function that creates new instance of BaseModel."""

        if line == "" or line is None:
            print("** class name missing **")

        elif line not in storage.classes():
            print("** class doesn't exist **")

        else:
            instance = storage.classes()[line]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Function that prints the string representation of an instance."""

        if line == "" or line is None:
            print("** class name missing **")

        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")

            elif len(words) < 2:
                print("** instance id missing **")

            else:
                patt = "{}.{}".format(words[0], words[1])
                if patt not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[patt])

    def do_destroy(self, line):
        """Function that deletes an instance based on class name and id."""

        if line == "" or line is None:
            print("** class name missing **")

        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")

            elif len(words) < 2:
                print("** instance id missing **")

            else:
                patt = "{}.{}".format(words[0], words[1])
                if patt not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[patt]
                    storage.save()

    def do_all(self, line):
        """Function that prints all string representation of an instance."""

        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")

            else:
                new_list = [str(obj) for patt, obj in storage.all().items()
                            if type(obj).__name__ == words[0]]
                print(new_list)

        else:
            f_list = [str(obj) for patt, obj in storage.all().items()]
            print(f_list)

    def do_update(self, line):
        """Function that updates an instance based on name and id"""

        if line == "" or line is None:
            print("** class name missing **")
            return

        regex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(regex, line)
        cname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)

        if not match:
            print("** class name missing **")

        elif cname not in storage.classes():
            print("** class doesn't exist **")

        elif uid is None:
            print("** instance id missing **")

        else:
            patt = "{}.{}".format(cname, uid)
            if patt not in storage.all():
                print("** no instance found **")

            elif not attribute:
                print("** attribute name missing **")

            elif not value:
                print("** value missing **")

            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float

                    else:
                        cast = int

                else:
                    value = value.replace('"', '')

                attributes = storage.attributes()[cname]
                if attribute in attributes:
                    value = attributes[attribute](value)

                elif cast:
                    try:
                        value = cast(value)

                    except ValueError:
                        pass

                setattr(storage.all()[patt], attribute, value)
                storage.all()[patt].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
