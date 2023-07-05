#!/usr/bin/python3
""" The console for hbnb. """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Definition of the hbnb console. """

    prompt = "(hbnb) "

    def empty(self):
        pass

    def do_quit(self):
        """Quit the console."""
        return True

    def do_EOF(self):
        """Quit console at EOF."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
