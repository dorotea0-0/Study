class IPAddress:
    def __init__(self, ipaddress):
        if isinstance(ipaddress, str):
            parts = list(map(int, ipaddress.split('.')))
        else:
            parts = list(ipaddress)
        self.__ip = tuple(parts)

    def __str__(self):
        return '.'.join(map(str, self.__ip))

    def __repr__(self):
        return f"IPAddress('{self}')"


# Пример использования
ip1 = IPAddress('192.168.1.1')
ip2 = IPAddress([1, 2, 3, 4])

print(ip1)
print(repr(ip1))
print(ip2)
print(repr(ip2))