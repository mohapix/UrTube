from time import time
# from datetime import datetime


class Message:

    def __init__(self, silent=False):
        self.msg_log = self.msg_txt = 'Начало лога'
        self.silent = silent
        self.log = {}
        self.log_this()

    def log_this(self):
        key = len(self.log) + 1
        timestamp = time()
        self.log[key] = [timestamp, self.msg_log]

    def user(self, msg_id: int, *args):
        msg_args = [*args]
        msg_mandatory = False
        match msg_id:
            case 1:
                self.msg_txt = f'Пользователь {msg_args[0]} уже существует'
                self.msg_log = f'Попытка регистрации пользователя. Логин: {msg_args[0]}'
            case 2:
                self.msg_txt = f'Пользователь {msg_args[0]} успешно зарегистрирован'
                self.msg_log = f'Пользователь зарегистрирован: {msg_args[0]}'
            case 3:
                self.msg_txt = f'Неверное имя пользователя или пароль'
                self.msg_log = f'Попытка авторизации пользователя. Логин: {msg_args[0]}'
                msg_mandatory = True
            case 4:
                self.msg_txt = f'Привет, {msg_args[0]}'
                self.msg_log = f'Вход в систему {msg_args[0]}'
            case 5:
                self.msg_txt = f'До свидания, {msg_args[0]}'
                self.msg_log = f'Выход из системы {msg_args[0]}'
            case _:
                self.msg_txt = ''
                self.msg_log = f'Сообщение об ошибке!'
        self.log_this()

        if (not self.silent and self.msg_txt) or msg_mandatory:
            print(self.msg_txt)

    def watch_video(self, msg_id: int, *args):
        msg_args = [*args]
        msg_mandatory = True
        match msg_id:
            case 1:
                self.msg_txt = f'Видео не найдено'
                self.msg_log = f'Не найдено видео: {msg_args[0]}'
                msg_mandatory = False
            case 2:
                self.msg_txt = f'Войдите в аккаунт, чтобы смотреть видео'
                self.msg_log = f'Попытка просмотра видео без авторизации: {msg_args[0]}'
            case 3:
                self.msg_txt = f'Вам нет 18 лет, пожалуйста, покиньте страницу'
                self.msg_log = f'Попытка просмотра взрослого контента: {msg_args[0]}'
            case 4:
                self.msg_txt = f'Конец видео'
                self.msg_log = f'Завершение просмотра видео: {msg_args[0]}'
            case 5:
                self.msg_txt = f'Запуск видео: "{msg_args[0]}" с {msg_args[1]} секунды со скоростью х{msg_args[2]}'
                self.msg_log = self.msg_txt
            case _:
                self.msg_txt = ''
                self.msg_log = f'Сообщение об ошибке!'
                msg_mandatory = False
        self.log_this()

        if (not self.silent and self.msg_txt) or msg_mandatory:
            print(self.msg_txt)

    def video_adg(self, msg_id: int, *args):    # adg - add, delete, get
        msg_args = [*args]
        msg_mandatory = False
        match msg_id:
            case 1:
                self.msg_txt = f'Войдите в аккаунт, чтобы добавить видео'
                self.msg_log = f'Попытка добавить видео: {msg_args}'
            case 2:
                self.msg_txt = f'Добавление видео:\n{msg_args}'
                self.msg_log = f'Добавление видео: {msg_args}'
            case 3:
                self.msg_txt = f'Все видео успешно добавлены'
                self.msg_log = self.msg_txt
            case 4:
                self.msg_txt = f'Не удалось добавить видео:\n{msg_args}'
                self.msg_log = f'Не удалось добавить видео: {msg_args}'
            case 5:
                self.msg_txt = f'Войдите в аккаунт, чтобы удалить видео'
                self.msg_log = f'Попытка удалить видео: {msg_args}'
            case 6:
                self.msg_txt = f'Удаление видео:\n{msg_args}'
                self.msg_log = f'Удаление видео: {msg_args}'
            case 7:
                self.msg_txt = f'Все видео успешно удалены'
                self.msg_log = self.msg_txt
            case 8:
                self.msg_txt = f'Не удалось удалить видео:\n{msg_args}'
                self.msg_log = f'Не удалось удалить видео: {msg_args}'
            case 9:
                self.msg_txt = f'Добавлено видео: {msg_args[0].title}'
                self.msg_log = (f'Добавлено видео: {msg_args[0].title}, {msg_args[0].duration}, '
                                f'{msg_args[0].adult_mode}, {msg_args[1]}')
            case 10:
                self.msg_txt = f'Удалено видео: {msg_args[0].title}'
                self.msg_log = (f'Удалено видео: {msg_args[0].title}, {msg_args[0].duration}, '
                                f'{msg_args[0].adult_mode}, {msg_args[1]}')
            case _:
                self.msg_txt = ''
                self.msg_log = f'Сообщение об ошибке!'
        self.log_this()

        if (not self.silent and self.msg_txt) or msg_mandatory:
            print(self.msg_txt)

    def __str__(self):
        return f'Лог активности'

    def __repr__(self):
        return self.msg_txt
