#!/usr/bin/python3
""" Console """
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ Console """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program'
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop(intro="holiwis")
