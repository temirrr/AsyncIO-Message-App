# Messaging App
This is simple messaging app, in which users can communicate in chatting groups.

If you want to try using it:
- Clone the repository to your machine.
- Follow instructions in _Installation Instructions_ section.
- Then, to run the app, follow instructions in _App Using_ section.

## Installation Instructions

### Redis Setup (for MacOS)
- You will need to have brew installed on your machine.
- Run `brew install redis` to install Redis on your MacOS. 
- Run `brew services start redis` to start redis server.

Respective instructions for Windows can be found on the Internet.

- Later on, if you want to shut the Redis server down, use `redis-cli shutdown` command.
- In case you want to check whether the server is running, use "redis-cli ping" command and you will get "PONG" in response in case server is running.

### PostgreSQL Setup

- Install postgresql on your machine. If you want, you can do it using docker.
- Run postgresql.
- You can change `db_str` variable in "chat/models.py" file's `Message` class to fit your postgresql instance's username, dbname, password, port, etc.

## Package Installation
- Firstly, create virtual environment inside the repository. One way of doing it is by using _pyenv_.
- Then, install all the packages by running the command `pip install -U -r requirements.txt`.

## App Using

### Server Start
- Run "python ./app.py" from the root folder. NOTE: it will occupy one of terminal windows.

### Connection to the Server as a Client
- Open your web-browser. NOTE: the app is mostly adapted for PC and not for mobile devices.
- Go to "localhost:8080" and the chat will work in case everything is fine with the server. If the server is running on someone-else's machine, then go to "server_machine_ip_address:8080" to connect to the chat. NOTE: you have to be on the same Wi-Fi network.