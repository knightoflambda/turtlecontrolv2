# IT011FP - turtlecontrolv2

Controlling Python's turtle using msvcrt and network programming

## Author
* **Katherine Mega Lopez**

## How to Setup
On a Windows laptop, open the command prompt and type **ipconfig** look for the field **Wireless LAN adapter Wi-Fi**, under it should be the IPv4 Address you will use for the **localhost** variable in both *server.py* and *client.py*.

## Getting Started
The application is about controlling a turtle using the console on a network in object-oriented code.

The application uses classes and functions to make debugging easier and to make the process easily understandable.

As seen on the script, *server.py* is broken down into only three processes:
* create screen
* create server
* start server

While *client.py* is a very simple script that only uses a *while loop* on **msvcrt** to wait for keyboard presses on the console. It waits for the appropriate keypresses and if detected, it will send the keycode to the server. The server will then decode the keycode and apply the appropriate commands on the turtle.
