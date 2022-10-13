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


        # ERRORS
        errorHappened = self.checkArgs(arg, 2)

        # NO ERRORS
        if errorHappened is False:
            inputArgs = arg.split()
            newInstance = eval(inputArgs[0])()
            storage.save()
            print(newInstance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name
        and id
        """

        # calls the custom argument condition checker
        errorHappened = self.checkArgs(arg, 4)

        # if no error happened proceed with the program
        if errorHappened is False:
            inputArgs = arg.split()
            objKey = f"{inputArgs[0]}.{inputArgs[1]}"
            objDict = storage.all()

            print(objDict[objKey])

    def do_destroy(self, arg):
        """
        It checks if the arguments
        are valid, if they are, it deletes the object from the dictionary and saves the
        dictionary to the file
        """

        # calls the custom argument condition checker
        errorHappened = self.checkArgs(arg, 4)

        # if no error happened proceed with the program
        if errorHappened is False:
            inputArgs = arg.split()
            objKey = f"{inputArgs[0]}.{inputArgs[1]}"
            objDict = storage.all()

            objDict.pop(objKey)
            storage.save()

    def checkArgs(self, newArgs, numberFlag):
        """
        It checks if the
        arguments passed to the command are valid.

        Returns True on error, false otherwise
        """

        argsList = newArgs.split()


        if numberFlag >= 1:
        # CHECKS CLASS NAME CONDITIONS
            # if the class name is missing
            if len(argsList) <= 0:
                print("** class name missing **")
                return True
        if numberFlag >= 2:
            # checks if the class name exists
            try:
                eval(argsList[0])
            except Exception:
                print("** class doesn't exist **")
                return True

        # CHECKS ID CONDITONS
        if numberFlag >= 3:
            # if the instance id is missing
            if len(argsList) < 2:
                print("** instance id missing **")
                return True
        if numberFlag >= 4:
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
