This project is a clone of AirBnB website which is a web application that replicate the features of a popular website that offer booking and reservation services.

This project is goning to use a command intepreter(Console) for the frontend and the backend initially till we get to other following projects where we will make use of: HTML/CSS, database storage, API, front-end integration...

Command Interpreter:

The command interpreter is exactly as a shell interpreter but limited to a specific use-case, we want to be able to manage object of our projects:

*. Create a new object (ex: a new User or a new Place)
*. Retrieve an object from a file, a database etc…
*. Do operations on objects (count, compute stats, etc…)
*. Update attributes of an object
*. Destroy an object




Execution
Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$


All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
