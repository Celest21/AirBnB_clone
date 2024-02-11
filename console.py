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
        """Function to handle end of file character (Ctrl+D)."""
        print()
        return True

    def do_quit(self, line):
        """Function that exits the shell in interactive mode."""
        return True

    def emptyline(self):
        """Function that does nothing on ENTER."""
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not line:
            print("** class name missing **")
            return

        try:
            class_name = line.split()[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return

            new_instance = globals()[class_name]()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print(e)

    def do_show(self, line):
        """Prints the string representation of an instance."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = class_name + "." + instance_id
            if key not in models.storage.all():
                print("** no instance found **")
                return

            print(models.storage.all()[key])
        except Exception as e:
            print(e)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = class_name + "." + instance_id
            if key not in models.storage.all():
                print("** no instance found **")
                return

            del models.storage.all()[key]
            models.storage.save()
        except Exception as e:
            print(e)

    def do_all(self, line):
        """Prints all string representation of all instances."""
        try:
            if not line:
                instances = models.storage.all().values()
            else:
                class_name = line.split()[0]
                if class_name not in globals():
                    print("** class doesn't exist **")
                    return
                instances = [inst for key, inst in models.storage.all().items() if key.startswith(class_name + ".")]

            print([str(inst) for inst in instances])
        except Exception as e:
            print(e)

    def do_update(self, line):
        """Updates an instance based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = class_name + "." + instance_id
            if key not in models.storage.all():
                print("** no instance found **")
                return

            if len(args) < 3:
                print("** attribute name missing **")
                return

            attr_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return

            # Handle string arguments with spaces between double quotes
            attr_value_str = ' '.join(args[3:])
            if attr_value_str[0] == '"' and attr_value_str[-1] == '"':
                attr_value_str = attr_value_str[1:-1]

            instance = models.storage.all()[key]
            attr_value = None

            # Attempt to cast the attribute value to its original type
            if hasattr(instance, attr_name):
                attr_type = type(getattr(instance, attr_name))
                try:
                    attr_value = attr_type(attr_value_str)
                except ValueError:
                    print(f"Invalid value for {attr_name} (expected {attr_type.__name__})")
                    return
            else:
                print(f"Attribute {attr_name} does not exist for {class_name}")
                return

            setattr(instance, attr_name, attr_value)
            instance.save()

        except Exception as e:
            print(e)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
