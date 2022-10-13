#!/usr/bin/python3
""" Console """

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


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
            argsList = arg.split()
            newInstance = eval(argsList[0])()
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
            argsList = arg.split()
            objKey = f"{argsList[0]}.{argsList[1]}"
            objDict = storage.all()

            print(objDict[objKey])

    def do_destroy(self, arg):
        """
        It checks if the arguments
        are valid, if they are, it deletes the object from
        the dictionary and saves the
        dictionary to the file
        """

        # calls the custom argument condition checker
        errorHappened = self.checkArgs(arg, 4)

        # if no error happened proceed with the program
        if errorHappened is False:
            argsList = arg.split()
            objKey = f"{argsList[0]}.{argsList[1]}"
            objDict = storage.all()

            objDict.pop(objKey)
            storage.save()

    def do_all(self, arg):
        """
        It prints all the objects
        in the storage file if no parameter is given.
        Otherwise only prints the list of objects of the given class
        """

        argsList = arg.split()
        errorHappened = False

        # We only check the argument if it was given by the user
        if len(argsList) >= 1:
            errorHappened = self.checkArgs(arg, -1)
        if errorHappened is False:
            objDict = storage.all()

            objList = []
            # iterate through the objects (represented as the value
            # in the dictionary from storage.all())
            for currentObject in objDict.values():
                # if we have an argument, then we need to filter what
                # goes into the list. We use 'isinstance' for that.
                if len(argsList) >= 1:
                    if isinstance(currentObject, eval(argsList[0])) is False:
                        continue
                objList.append(str(currentObject))
            print(objList)

    def do_update(self, arg):
        """
        Takes the arguments from the command line and updates the
        attribute of the object with
        the new value.

        :param arg: <class name> <id> <attribute name> "<attribute value>"
        """
        # update <class name> <id> <attribute name> "<attribute value>"
        #          ARG[0]   ARG[1]    ARG[2]          ARG[3]]

        errorHappened = self.checkArgs(arg, 6)

        if errorHappened is False:
            argsList = arg.split()
            objAttName = argsList[2]
            objAttValue = eval(argsList[3])  # casts the actual object type
            objDict = storage.all()
            objKey = f"{argsList[0]}.{argsList[1]}"

            objDict[objKey].__dict__[objAttName] = objAttValue
            storage.save()

    def checkArgs(self, newArgs, numberFlag):
        """
        It checks if the
        arguments passed to the command are valid.

        NumberFlag: This flag is used based on the
        number passed, and executes the needed "rules/
        conditions"

        each number adds a function + all of the above:
        1: if the class name is missing
        2: if the class exists
        3: if the instance id is missing
        4: if the instance exists
        5: if the attribute name is missing
        6: if the value is missing
        Returns True on error, false otherwise
        """

        argsList = newArgs.split()
        # CHECKS CLASS NAME CONDITIONS
        # if the class name is missing
        if numberFlag >= 1:
            # REMEMBER len() STARTS FROM 1
            if len(argsList) <= 0:
                print("** class name missing **")
                return True
        # if the class exists
        if numberFlag >= 2 or numberFlag == -1:
            try:
                eval(argsList[0])
            except Exception:
                print("** class doesn't exist **")
                return True

        # CHECKS ID CONDITONS
        # if the instance id is missing
        if numberFlag >= 3:
            if len(argsList) < 2:
                print("** instance id missing **")
                return True
        # if the instance exists
        if numberFlag >= 4:
            # tries to find the object in the dictionary of stored objects
            # using the key. If it is not found, it will print an error message
            objKey = f"{argsList[0]}.{argsList[1]}"
            objDict = storage.all()  # loads the dict. of stored objects
            # if key specified is not found
            if objDict.get(objKey) is None:
                print("** no instance found **")
                return True

        # if the attribute name is missing
        if numberFlag >= 5:
            if len(argsList) <= 2:
                print("** attribute name missing **")
                return True
        # if the value is missing
        if numberFlag >= 6:
            if len(argsList) <= 3:
                print("** value missing **")
                return True

        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
