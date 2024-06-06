from message import Message


class User:

    def __init__(self, nickname: str, password: str, age: int or None, silent: bool = False):
        self.nickname = nickname
        self.password = hash(password)
        if age:
            self.age = age
            self.msg = Message(silent)

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return self.nickname

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password
