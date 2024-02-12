#!/usr/bin/python3
"""The Command Line Interpreter."""

from models.base_model import BaseModel
from models import storage
import json
import cmd
import re
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Class that defines Airbnb clone public class instances."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Function to handle end of file character (Ctrl+D)."""
        print()
        return True

    def do_quit(self, line):
        """Function that exits the shell in interactive mode."""
        return True

    def emptyline(self):
        """Function that does nothing on ENTER."""
        pass

    def do_create(self, arg):
        """
        Create a new instance of a specified class.
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        class_name = arg_list[0]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Show details of a specified instance.
        Usage: show <class_name> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        class_name = arg_list[0]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def do_all(self, arg):
        """
        Show details of all instances or all instances of a specified class.
        Usage: all [<class_name>]
        """
        arg_list = arg.split()
        if arg and arg_list[0] not in globals():
            print("** class doesn't exist **")
            return

        instances = []
        for key, value in storage.all().items():
            if not arg or value.__class__.__name__ == arg_list[0]:
                instances.append(str(value))

        print("[{}]".format(", ".join(instances)))

    def do_destroy(self, arg):
        """
        Destroy an instance specified by class name and id.
        Usage: destroy <class_name> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        class_name = arg_list[0]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_update(self, arg):
        """
        Update an instance with new attributes.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        class_name = arg_list[0]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return

        if len(arg_list) < 4:
            print("** value missing **")
            return

        attribute_name = arg_list[2]
        attribute_value = arg_list[3].strip('"')

        setattr(storage.all()[key], attribute_name, attribute_value)
        storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
