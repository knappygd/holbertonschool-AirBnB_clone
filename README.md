# hbnb - AirBnB clone
## Description
hbnb is a replica of the popular vacation rental app. This project deals with the implementation of the console to handle data.

<br>

# Command Interpreter
A command intepreter is a way for the user to interact with a program. The user can input commands that the interpreter will execute, and subsequently print the output associated with the action performed.
## How to start it
First, it's necessary to clone the repo in order to access the interpreter. Use the following command to do so:
<br>

`git clone https://github.com/knappygd/holbertonschool-AirBnB_clone.git`
<br>

Grant execution permissions to the console file:
<br>

`chmod +x console.py`
<br>

And, finally, execute it:
<br>

`./console.py`
<br>

Once you have the `(hbnb)` prompt up and running, you can use the following built-in commands.

## How to use it
The console supports seven commands to interact with classes.

* `create`
    * Creates a new instance of a class, saves it to a JSON file and prints the `id`.
* `show`
    * Prints the string representation of an instance based on the class name and id.
* `destroy`
    * Deletes an instance based on a class name and the id and saves the changes into the JSON file.
* `all`
    * Prints a string representation of all instances base dor not on the class name.
* `update`
    * Updates an instance based on the class name and id by adding or updating attributes and saving the changes into a JSON file.

To quit the console, the `quit` command does just fine. Ctrl+D (`EOF`) is supported as well. Additionally, using the `help` command followed by the command name displays a short description of the command.

<br>

# Structure
This project makes use of three main files containing the code for implementing the console and its associated dependencies.
* console.py
    * This file contains the implementation of the command interpreter, as well as its built-in commands.
* base_model.py
    * This file contains the BaseModel class, a parent class from which other classes inherit from. It serves as a model establishing methods and attributes.
* file_storage.py
    * This file contains the FileStorage class, responsible of handling the serialization and deserialization process between Python objects and JSON data structures between JSON and Python files.
