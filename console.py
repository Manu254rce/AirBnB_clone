#!/usr/bin/python3
"""
This is a simple Python3 code snippet
"""


import cmd
import importlib
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    This class handles the command line instance for our HBNB clone
    """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel}

    def do_EOF(self, line):
        """
        Function that handles EOF conditions
        within the console i.e user sends a SIGINT
        signal (Ctrl D)
        """
        print()
        return True

    def do_quit(self, line):
        """
        Quit comand to exit the program
        """
        return True

    def emptyline(self):
        """
        This function ensures that pressing Enter doesn't execute anything
        """
        pass

    def do_create(self, line):
        """
        Function that creates a new instance of our BaseModel, saves it to JSON
        & prints the id
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            from models import storage
            class_instance = eval(args[0])()
            class_instance.save()
            print(class_instance.id)
            storage.save()

    def do_show(self, line):
        """
        Function that shows the string representation of an instance
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        from models import storage
        obj = storage.all(self.classes[class_name])
        key = "{}.{}".format(class_name, instance_id)
        if key in obj:
            print(obj[key])
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Function that prints all string representations of the instance
        """
        from models import storage
        class_instance = None
        if line:
            try:
                class_instance = eval(line)
            except KeyError:
                print("** class doesn't exist **")
                return
        else:
            obj = storage.all(class_instance)
        if len(obj) == 0:
            print("[]")
        for ob in obj.values():
            print(ob)

    def do_update(self, line):
        """
        Function that updates an instance by changing its attribute
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 3:
            print("** instance id and attribute name missing **")
            return

        instance_id = args[1]
        attribute_name = args[2]
        value = args[3] if len(args) > 3 else None

        from models import storage
        # Retrieve the instance
        instances = storage.all(self.classes[class_name])
        key = "{}.{}".format(class_name, instance_id)

        if key not in instances:
            print("** no instance found **")
            return

        # Update the instance
        instance = instances[key]
        if value is not None:
            setattr(instance, attribute_name, value)
            instance.save()
            print("** instance updated **")
        else:
            print("** value missing **")

    def do_destroy(self, line):
        """
        Function that destroys or deletes an instance based on
        a cli argument from the shell
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        from models import storage
        instances = storage.all(self.classes[class_name])
        key = "{}.{}".format(class_name, instance_id)
        if key not in instances:
            print("** no instance found **")
            return
        del instances[key]
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
