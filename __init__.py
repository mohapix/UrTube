from video import Video
from tube import UrTube


def watch_video(title):
    ur.watch_video(title)


def watch_video2(title, time_start):
    if not ur.current_user:
        print('Войдите в аккаунт, чтобы смотреть видео')
        return
    videos = ur.get_videos(title)
    if isinstance(videos, str):
        print(videos)
        return
    for i in range(len(videos)):
        if title == videos[i]:
            index = UrTube.uploaded_video_titles.index(videos[i])
            ur.watch_video2(index, time_start)
            return
    print('Видео не найдено')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
watch_video('Лучший язык программирования 2024 года!')

print('--------------------')
# Повторный прогон исходных данных с использованием метода просмотра видео №2
ur.log_out()

# Проверка на вход пользователя и возрастное ограничение
watch_video2('Для чего девушкам парень программист?', 0)
ur.log_in('vasya_pupkin', 'lolkekcheburek')
watch_video2('Для чего девушкам парень программист?', 0)
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
watch_video2('Для чего девушкам парень программист?', 0)

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
watch_video2('Лучший язык программирования 2024 года!', 190)
