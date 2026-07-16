from socket import socket, AddressFamily, SocketKind

from config import config


class NetworkBackend:
    def __init__(self) -> None:
        self.socket = socket(AddressFamily.AF_INET, SocketKind.SOCK_DGRAM)

    def send(self, message: str) -> None:
        self.socket.sendto(message.encode("utf8"), ("127.0.0.1", config.port))
