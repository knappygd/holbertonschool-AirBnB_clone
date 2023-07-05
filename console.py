#!/usr/bin/python3
""" The console for hbnb. """
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, line):
        """Creates a new instance of BaseModel and saves it."""
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")

            kwargs = {}
            for i in range(1, len(my_list)):
                key, value = tuple(my_list[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
