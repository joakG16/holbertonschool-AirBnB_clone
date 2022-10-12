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
        if errorHappened == False:
            try:
                eval(inputArgs[0])
            except:
                print("** class doesn't exist **")
                errorHappened = True

        # NO ERRORS
        if errorHappened == False:
            newInstance = eval(inputArgs[0])()
            storage.save()
            print(newInstance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name
        and id
        """
        inputArgs = arg.split()
        objKey = f"{inputArgs[0]}.{inputArgs[1]}"
        objDict = storage.all()
        print(objDict[objKey])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
