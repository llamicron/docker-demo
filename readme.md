# 2 Containers
I just did this to figure out docker. It shows how two containers can communicate.

There are two containers:
  - `data-service`: provides some data through a webserver (Flask)
  - `website`: retrieves the data from the `data-service` and displays it through a webserver (also Flask)

There is a `Dockerfile` in each directory. They are both identical because both are running a Flask app. The `website` container's port `80` is mapped to port `5000` on the host machine.
