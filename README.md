![AsyncIO Message App](https://github.com/temirrr/AsyncIO-Message-App/tree/master/static/img/msgapp_logo.png)
This is simple messaging app with common chatting groups.

It is based on **aiohttp** framework, which makes it easy to use **asyncio** within the app. **Websockets** were used for the purpose of exchanging multiple messages between client and server. Other core libraries are **aioredis** and **aiopg**.

TODO: record GIFs and add them to GitHib repo.

Go and see DEMO in _Demo_ section below.

If you want to try using it:
- Clone the repository to your machine.
- Follow instructions in _Installation Instructions_ section.
- Then, to run the app, follow instructions in _App Using_ section.

# DEMO

- GIF1
- GIF2
- ETC

# Installation Instructions

## Redis Setup (for MacOS)
- You will need to have brew installed on your machine.
- Run `brew install redis` to install Redis on your MacOS. 
- Run `brew services start redis` to start redis server.

Respective instructions for Windows can be found on the Internet.

- Later on, if you want to shut the Redis server down, use `redis-cli shutdown` command.
- In case you want to check whether the server is running, use "redis-cli ping" command and you will get "PONG" in response in case server is running.

## PostgreSQL Setup

- Install postgresql on your machine. If you want, you can do it using docker.
- Run postgresql.
- You will need to do `CREATE TABLE group_general (messages json NOT NULL);` and `CREATE TABLE group_interns (messages json NOT NULL);` for two of my hard-coded chat-groups. Sorry for not taking care of this within the code, since my main purpose was to learn asyncio and aiohttp.
- You can change `db_str` variable in "chat/models.py" file's `Message` class to fit your postgresql instance's username, dbname, password, port, etc.

## Package Installation
- Firstly, create virtual environment inside the repository. One way of doing it is by using _pyenv_.
- Then, install all the packages by running the command `pip install -U -r requirements.txt`.

# App Using

## Server Start
- Run `python ./app.py` from the root folder. NOTE: it will occupy one of terminal windows.

## Connection to the Server as a Client
- Open your web-browser. NOTE: the app is mostly adapted for PC and not for mobile devices.
- Go to "localhost:8080" and the chat will work in case everything is fine with the server. If the server is running on someone-else's machine, then go to "server_machine_ip_address:8080" to connect to the chat. NOTE: you have to be on the same Wi-Fi network.

# Credits

- Thanks to [@achimnol](https://github.com/achimnol) for assigning doing this app during "Lablup Bootcamp" (Internship@Lablup Inc., Summer 2019).
- Thanks to all [@lablup](https://github.com/lablup) members for supporting and helping me.
- Thanks to all the tutorials and docs our there on the Internet. I got most of the ideas and used the following repo as my template: https://github.com/Crandel/aiohttp ([@Crandel](https://github.com/Crandel)).