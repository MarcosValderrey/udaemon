# Udaemon
**Udaemon** is a light command line tool to help you run a Python application as a background service.

Its purpose is to have a simplified way to deploy a Python script as a service. If you need more flexibility use [systemd](https://wiki.archlinux.org/title/systemd) itself.
## Author
Marcos Valderrey - Software Developer - [LinkedIn](https://ar.linkedin.com/in/marcosvalderrey)
## Requirements
Linux installation with `systemd` and `python`.
## Installation
Clone this repository and you are ready to go!
## Usage
Create a service definition like the one from the [example](example/example.service) somewhere. Visit [systemd documentation](https://wiki.archlinux.org/title/systemd) to know more about different ways of setting up the service file according to your needs.
## Creating a new service
Add the new service to **udaemon** running:

```console
python udaemon.py add <service-name> /path/to/your/service/<service-name>.service;
```

The path to your service could be relative to your working directory also, like:

```console
python udaemon.py add <service-name> ./example/example.service;
```

You could also run **udaemon** for another location in this way:

```console
python /home/someone/code/udaemon/udaemon.py add <service-name> /path/to/your/service/<service-name>.service;
```
## Removing a service
To remove an added service you must run:

```console
python udaemon.py remove <service-name>;
```

or

```console
python /home/someone/code/udaemon/udaemon.py remove <service-name>;
```
## Checking service state
You could check the state of the service and the latest logs running:

```console
python udaemon.py status <service-name>;
```
## Listing added services
Quick way to check which services you already deployed to **udaemon**:

```console
python udaemon.py list;
```

## Alias
You could use some of the common verbs on `systemctl` through **udaemon**, but it is not recommendend nor necessary since this wrapper takes care of everything. The aliased commands are:

1. Start a service (you should use `add` instead):

```console
python udaemon.py start <service-name>;
```

2. Stop a service (you should use `remove` instead):

```console
python udaemon.py stop <service-name>;
```

3. Enable a service (you should use `add` instead):

```console
python udaemon.py enable <service-name>;
```

4. Disable a service (you should use `remove` instead):

```console
python udaemon.py disable <service-name>;
```

5. Check the status of a service (this is still useful):

```console
python udaemon.py status <service-name>;
```

## Example
Inside example folder there's a heartbeat logger.

Modify the `WorkingDirectory` parameter on the [example service definition](example/example.service) such that it points to the root of this project.

If you want to test **udaemon** go ahead and run:

```console
python udaemon.py add example.service example/example.service;
```

To see the heartbeat in action try:

```console
python udaemon.py status example.service;
```

Also log entries should be written in `example/example.log` showing the service is deployed.

To stop and remove the service run:

```console
python udaemon.py remove example.service;
```
