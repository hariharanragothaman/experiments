#! /usr/bin/env python3
import argparse
import cmd
import pickle
import socket
import threading


def main():
    """Connect a chat client to a server and process incoming commands."""
    parser = argparse.ArgumentParser(description='Execute a chat client demo.')
    parser.add_argument('host', type=str, help='name of server on the network')
    parser.add_argument('port', type=int, help='location where server listens')
    arguments = parser.parse_args()
    client = User(socket.create_connection((arguments.host, arguments.port)))
    client.start()


class User(cmd.Cmd, threading.Thread):

    """Provide a command interface for internal and external instructions."""

    prompt = '>>> '

    def __init__(self, connection):
        """Initialize the user interface for communicating with the server."""
        cmd.Cmd.__init__(self)
        threading.Thread.__init__(self)
        self.connection = connection
        self.reader = connection.makefile('rb', -1)
        self.writer = connection.makefile('wb', 0)
        self.handlers = dict(print=print, ping=self.ping)

    def start(self):
        """Begin execution of processor thread and user command loop."""
        super().start()
        super().cmdloop()
        self.cleanup()

    def cleanup(self):
        """Close the connection and wait for the thread to terminate."""
        self.writer.flush()
        self.connection.shutdown(socket.SHUT_RDWR)
        self.connection.close()
        self.join()

    def run(self):
        """Execute an automated message pump for client communications."""
        try:
            while True:
                self.handle_server_command()
        except (BrokenPipeError, ConnectionResetError):
            pass

    def handle_server_command(self):
        """Get an instruction from the server and execute it."""
        source, (function, args, kwargs) = pickle.load(self.reader)
        print('Host: {} Port: {}'.format(*source))
        self.handlers[function](*args, **kwargs)

    def preloop(self):
        """Announce to other clients that we are connecting."""
        self.call('print', socket.gethostname(), 'just entered.')

    def call(self, function, *args, **kwargs):
        """Arrange for a handler to be executed on all other clients."""
        assert function in self.handlers, 'You must create a handler first!'
        pickle.dump((function, args, kwargs), self.writer)

    def do_say(self, arg):
        """Causes a message to appear to all other clients."""
        self.call('print', arg)

    def do_ping(self, arg):
        """Ask all clients to report their presence here."""
        self.call('ping')

    def ping(self):
        """Broadcast to all other clients that we are present."""
        self.call('print', socket.gethostname(), 'is here.')

    def do_exit(self, arg):
        """Disconnect from the server and close the client."""
        return True

    def postloop(self):
        """Make an announcement to other clients that we are leaving."""
        self.call('print', socket.gethostname(), 'just exited.')


if __name__ == '__main__':
    main()
