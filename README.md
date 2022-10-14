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

<h2>The Console</h2>

<div>

* creates a data model
* store and persist objects to a JSON file
* manage (create, update, destroy, etc) objects via a console/command interpreter

</div>

<p>The first part consists in creating a storage engine. This storage engine will be use to differentiate "My Object" and "How it is stored and persisted". This abstraction will allow us to chage the type of stoarge easily without updating all of our codebase.</p>

<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20221014%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221014T151247Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6207f4e486b413646cb36c177371e67614cf0d26e1118399a107a0b0c3788e77">

#

<h2>What is a console?</h2>

<p>This will work as a <a href="https://github.com/ismael-soler/holbertonschool-simple_shell">Shell</a>. It's exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project.</p>

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
