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

        # calls the custom argument condition checker
        errorHappened = self.checkArgs(arg)

        # if no error happened proceed with the program
        if errorHappened is False:
            inputArgs = arg.split()
            objKey = f"{inputArgs[0]}.{inputArgs[1]}"
            objDict = storage.all()

            print(objDict[objKey])

    def checkArgs(self, newArgs):
        """
        It checks if the
        arguments passed to the command are valid.

        Returns True on error, false otherwise
        """

        argsList = newArgs.split()

    # CHECKS CLASS NAME CONDITIONS
        # if the class name is missing
        if len(argsList) <= 0:
            print("** class name missing **")
            return True
        # checks if the class name exists
        try:
            eval(argsList[0])
        except Exception:
            print("** class doesn't exist **")
            return True

    # CHECKS ID CONDITONS
        # if the instance id is missing
        if len(argsList) < 2:
            print("** instance id missing **")
            return True

        # tries to find the object in the dictionary of stored objects
        # using the key. If it is not found, it will print an error message.
        objKey = f"{argsList[0]}.{argsList[1]}"
        objDict = storage.all()  # loads the dict. of stored objects
        # if key specified is not found
        if objDict.get(objKey) == None:
            print("** no instance found **")
            return True

        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
