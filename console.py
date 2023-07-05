#!/usr/bin/python3
""" The console for hbnb. """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Definition of the hbnb console. """

    prompt = "(hbnb) "

    def empty(self):
        pass

    def on_quit(self):
        return True

    def on_EOF(self):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
