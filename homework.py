class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        """Метод выводит возвращает строку сообщения."""

        return(f'Тип тренировки: {self.training_type}; '
               f'Длительность: {self.duration:.3f} ч.; '
               f'Дистанция: {self.distance:.3f} км; '
               f'Ср. скорость: {self.speed:.3f} км/ч; '
               f'Потрачено ккал: {self.calories:.3f}.')


class Training:
    """Базовый класс тренировки."""

    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65  # 1.38
    coeff_calories_1 = 18
    coeff_calories_2 = 20

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        speed = distance / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass  # ??
        return InfoMessage(type(self).__name__,
                           self.duration,
                           self.get_distance(),  # ?
                           self.get_mean_speed(),
                           self.get_spent_calories())  # ?


class Running(Training):
    """Тренировка: бег."""
    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65  # 1.38
    coeff_calories_1 = 18
    coeff_calories_2 = 20

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self):
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        speed = distance / self.duration
        calories_1 = self.coeff_calories_1 * speed - self.coeff_calories_2
        return calories_1 * self.weight / self.M_IN_KM * self.duration  # try


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    pass


class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    Dict_type = {'SWM': 'Swimming',  # return dict_of[workout_type](*data)
                 'RUN': 'Running',
                 'WLK': 'Walking'
                 }
    if workout_type in Dict_type.keys():
        pass


def main(training: Training) -> None:
    """Главная функция."""
    info = Training.show_training_info()  # Объект класса InfoMessage
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
