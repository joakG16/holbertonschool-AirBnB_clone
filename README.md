<!--HEADER-->
<h1 align="center">
<img width=5.3% src="https://cdn-icons-png.flaticon.com/512/5977/5977574.png" alt="gif" />
  AirBnB Clone
</h1>

<p align="center">
    <img width=52% src="https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67" alt="hbnb" width=50% heigth=50% >
</p>

<p align="center">
The goal of this project is to deploy in our own server a simple copy of the AirBnB website. The project will be built in separates steps, each focusing on different aspects and technologies. This specific part consists in building the console.
</p>

#


<h2>The Console (Command Interpreter)</h2>

<div>

* creates a data model
* manage (create, update, destroy, etc) objects via a console/command interpreter
* store and persist objects to a JSON file

</div>

<p>The first part consists in creating a storage engine. This storage engine will be used to differentiate the actual object from how it's stored and persisted . This abstraction will allow us to chage the type of stoarge easily without updating all of our codebase.</p>

<img src="https://i.imgur.com/1jNvIGN.png">

<!-- REQUIREMENTS -->
<h2>Requirements</h2>

<div>

* Allowed editors: vi, vim, emacs
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* Our code uses the pycodestyle (version 2.7.*)
* All tests can be executed by using this command: python3 -m unittest discover tests

</div>
#

<!--THE CONSOLE-->
<h2>What is a console?</h2>

<p>This will work as a <a href="https://github.com/ismael-soler/holbertonschool-simple_shell">Shell</a>. It's exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project.</p>

<p></p>

<br>

__Interactive Mode__


```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
(hbnb)
(hbnb) quit
$
```

__Non-Interactive Mode__

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
```

#

- __console.py__ commands

	| Function | Description | Usage example |
	| -- | -- | -- |
	| `do_quit` | Exit the progrmm | `quit` |
	| `do_EOF` | Exit the program handling End of File (ctrl + D) | ctrl + D |
	| `emptyline` | Do nothing | empty line + enter |
	| `do_create` | Creates a new instance of a given class | `create BaseModel` |
	| `do_show` | Prints the string representation of an instance | `show User [ID]` |
	| `do_destroy` | Deletes an instance based on the class name and id | `destroy User [ID]` |
	| `do_all` | Prints all string representation of all instances | `all` or `all Review`|
	| `do_update` | Updates an instance based on the class name and id by adding or updating attribute | `update User [ID] email "aibnb@mail.com"`|