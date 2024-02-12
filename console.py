#!/usr/bin/python3
"""The Command Line Interpreter."""

from models.base_model import BaseModel
import json
import cmd
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


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
        """Create a new instance of a specified class, save it, and print its id."""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        
        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Print the string representation of an instance based on the class name and id."""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in FileStorage._FileStorage__objects:
            print("** no instance found **")
        else:
            print(FileStorage._FileStorage__objects[key])

    def do_all(self, line):
        """Print all string representations of instances for a specified class."""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return

        instances = []
        for key, obj in FileStorage._FileStorage__objects.items():
            if key.startswith(class_name + "."):
                instances.append(str(obj))
        print(instances)

    def do_destroy(self, line):
        """Delete an instance based on the class name and id."""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in FileStorage._FileStorage__objects:
            print("** no instance found **")
        else:
            del FileStorage._FileStorage__objects[key]

            file_storage_instance = FileStorage()
            file_storage_instance.save()

    def do_update(self, line):
        """Update an instance based on the class name and id."""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in FileStorage._FileStorage__objects:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            attribute_name = args[2]
            value = args[3]
            instance = FileStorage._FileStorage__objects[key]
            setattr(instance, attribute_name, value)
            instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
