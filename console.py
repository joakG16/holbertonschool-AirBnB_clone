#!/usr/bin/python3
""" Console """

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Console """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program'
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        """
        errorHappened = False
        inputArgs = arg.split()

        # ERRORS
        if len(inputArgs) <= 0:
            print("** class name missing **")
            errorHappened = True
        else:
            try:
                eval(inputArgs[0])
            except Exception:
                print("** class doesn't exist **")
                errorHappened = True

        # NO ERRORS
        if errorHappened is False:
            newInstance = eval(inputArgs[0])()
            storage.save()
            print(newInstance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name
        and id
        """
        inputArgs = arg.split()
        errorHappened = False

        # if the class name is missing
        if len(inputArgs) <= 0:
            print("** class name missing **")
            errorHappened = True

        # checks if the class name exists
        elif errorHappened is False:
            try:
                eval(inputArgs[0])
            except Exception:
                print("** class doesn't exist **")
                errorHappened = True
        # if the instance id is missing
        if len(inputArgs) < 2 and errorHappened is False:
            print("** instance id missing **")
            errorHappened = True

        if errorHappened is False:
            try:
                objKey = f"{inputArgs[0]}.{inputArgs[1]}"
                objDict = storage.all()  # bringing the dict. of stored objects
                print(objDict[objKey])  # find & print desired object using key
            except Exception:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
