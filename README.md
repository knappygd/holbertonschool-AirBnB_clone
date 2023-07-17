# hbnb - AirBnB clone
## Description
hbnb is a replica of the popular vacation rental app. This project deals with the implementation of the console to handle data.

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

# Structure
This project makes use of three main files containing the code for implementing the console and its associated dependencies.
* console.py
    * This file contains the implementation of the command interpreter, as well as its built-in commands.
* base_model.py
    * This file contains the BaseModel class, a parent class from which other classes inherit from. It serves as a model establishing methods and attributes.
* file_storage.py
    * This file contains the FileStorage class, responsible of handling the serialization and deserialization process between Python objects and JSON data structures between JSON and Python files.

# Examples
Some console commands can be used with arguments or not, depending on their use case.

Here we are creating a BaseModel instance, returning the id of the new instance, which was saved into our JSON file.

```
(hbnb) create BaseModel
256394cf-78d4-49b8-99cd-66f509fc97b9
```
We can see the information associated with this instance using the `show` command.
```
(hbnb) show BaseModel 256394cf-78d4-49b8-99cd-66f509fc97b9
[BaseModel] (256394cf-78d4-49b8-99cd-66f509fc97b9) {'id': '256394cf-78d4-49b8-99cd-66f509fc97b9', 'created_at': datetime.datetime(2023, 7, 9, 17, 35, 45, 447233), 'updated_at': datetime.datetime(2023, 7, 9, 17, 35, 45, 447251)}
```
Here are some new classes instantiated, such as another BaseModel, a new User, and a new City.
```
(hbnb) create BaseModel
7dfb7857-a6d4-45ae-82b2-a0a401ed74e1
(hbnb) create User
5ebd47e0-bc6c-4988-bafa-8053c27f45ea
(hbnb) create City
183740ec-9866-48b3-a6e7-ff61b24d3250
```
We can see the information of them all using the `all` command.
```
(hbnb) all
["[BaseModel] (7dfb7857-a6d4-45ae-82b2-a0a401ed74e1) {'id': '7dfb7857-a6d4-45ae-82b2-a0a401ed74e1', 'created_at': datetime.datetime(2023, 7, 9, 17, 35, 5, 436529), 'updated_at': datetime.datetime(2023, 7, 9, 17, 35, 5, 436548)}", "[User] (5ebd47e0-bc6c-4988-bafa-8053c27f45ea) {'id': '5ebd47e0-bc6c-4988-bafa-8053c27f45ea', 'created_at': datetime.datetime(2023, 7, 9, 17, 35, 8, 439918), 'updated_at': datetime.datetime(2023, 7, 9, 17, 35, 8, 439948)}", "[City] (183740ec-9866-48b3-a6e7-ff61b24d3250) {'id': '183740ec-9866-48b3-a6e7-ff61b24d3250', 'created_at': datetime.datetime(2023, 7, 9, 17, 35, 11, 956214), 'updated_at': datetime.datetime(2023, 7, 9, 17, 35, 11, 956239)}", "[BaseModel] (256394cf-78d4-49b8-99cd-66f509fc97b9) {'id': '256394cf-78d4-49b8-99cd-66f509fc97b9', 'created_at': datetime.datetime(2023, 7, 9, 17, 35, 45, 447233), 'updated_at': datetime.datetime(2023, 7, 9, 17, 35, 45, 447251)}"]
```
Now we have:
* 2 BaseModel instances
* 1 User instance
* 1 City instance

What if we want to see all instances of a specific class, like BaseModel? Then we have to use `all` followed by the name of the class.
```
(hbnb) all BaseModel
["[BaseModel] (7dfb7857-a6d4-45ae-82b2-a0a401ed74e1) {'id': '7dfb7857-a6d4-45ae-82b2-a0a401ed74e1', 'created_at': datetime.datetime(2023, 7, 9, 17, 35, 5, 436529), 'updated_at': datetime.datetime(2023, 7, 9, 17, 35, 5, 436548)}", "[BaseModel] (256394cf-78d4-49b8-99cd-66f509fc97b9) {'id': '256394cf-78d4-49b8-99cd-66f509fc97b9', 'created_at': datetime.datetime(2023, 7, 9, 17, 35, 45, 447233), 'updated_at': datetime.datetime(2023, 7, 9, 17, 35, 45, 447251)}"]
```

Let's destroy a BaseModel class with a specific `id`.
```
(hbnb) destroy BaseModel 7dfb7857-a6d4-45ae-82b2-a0a401ed74e1
(hbnb) all
["[User] (5ebd47e0-bc6c-4988-bafa-8053c27f45ea) {'id': '5ebd47e0-bc6c-4988-bafa-8053c27f45ea', 'created_at': datetime.datetime(2023, 7, 9, 17, 35, 8, 439918), 'updated_at': datetime.datetime(2023, 7, 9, 17, 35, 8, 439948)}", "[City] (183740ec-9866-48b3-a6e7-ff61b24d3250) {'id': '183740ec-9866-48b3-a6e7-ff61b24d3250', 'created_at': datetime.datetime(2023, 7, 9, 17, 35, 11, 956214), 'updated_at': datetime.datetime(2023, 7, 9, 17, 35, 11, 956239)}", "[BaseModel] (256394cf-78d4-49b8-99cd-66f509fc97b9) {'id': '256394cf-78d4-49b8-99cd-66f509fc97b9', 'created_at': datetime.datetime(2023, 7, 9, 17, 35, 45, 447233), 'updated_at': datetime.datetime(2023, 7, 9, 17, 35, 45, 447251)}"]
```
Now we might want to update a class, for example City, and add a new field called "city_name", with the value "Montevideo".
```
(hbnb) update City 183740ec-9866-48b3-a6e7-ff61b24d3250 city_name "Montevideo"
(hbnb) show City 183740ec-9866-48b3-a6e7-ff61b24d3250
[City] (183740ec-9866-48b3-a6e7-ff61b24d3250) {'id': '183740ec-9866-48b3-a6e7-ff61b24d3250', 'created_at': datetime.datetime(2023, 7, 9, 17, 35, 11, 956214), 'updated_at': datetime.datetime(2023, 7, 9, 17, 42, 2, 497588), 'city_name': 'Montevideo'}
```