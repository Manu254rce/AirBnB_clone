#!/usr/bin/python3
"""
This is a simple Python3 code snippet
"""


import cmd
import importlib
from models.base_model import BaseModel

classes = {"BaseModel"}


class HBNBCommand(cmd.Cmd):
    """
    This class handles the command line instance for our HBNB clone
    """
    prompt = '(hbnb) '

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
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            from models import storage
            class_instance = eval(args[0])()
            class_instance.save()
            print(class_instance.id)
            storage.save()

    def do_show(self, line):
        """
        Function that shows the string reprsentation of an instance
        """
        from models import storage
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_instance = eval(args[0])
        except KeyError:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj = storage.all()
        key = f"{args[0], args[1]}"
        if key in obj:
            print(obj[key])
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Function that prints all string representations of the instance
        """
        from models import storage
        if line:
            try:
                class_instance = eval(line)
            except KeyError:
                print("** class doesn't exist **")
                return
        else:
            obj = storage.all()
        if len(obj) == 0:
            print("[]")
        for ob in obj.values():
            print(ob)

    def do_update(self):
        pass

    def do_destroy(self):
        """
        Function that destroys or deletes an instance based on
        a cli argument from the shell
        """



if __name__ == "__main__":
    HBNBCommand().cmdloop()
