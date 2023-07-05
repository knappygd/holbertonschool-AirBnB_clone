#!/usr/bin/python3
""" The console for hbnb. """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Definition of the hbnb console. """

    prompt = "(hbnb) "

    def empty(self):
        pass

    def do_quit(self, line):
        """Quit the console."""
        return True

    def do_EOF(self, line):
        """Quit console at EOF."""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
