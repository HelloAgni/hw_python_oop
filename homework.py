from dataclasses import dataclass

@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

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
    LEN_STEP: float = 0.65

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
        distance = (
            self.action
            * self.LEN_STEP
            / self.M_IN_KM
        )
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        distance = (
            self.action
            * self.LEN_STEP
            / self.M_IN_KM
        )
        speed = (
            distance
            / self.duration
        )
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(type(self).__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65
    coeff_calories_1 = 18
    coeff_calories_2 = 20

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        super().get_mean_speed()
        training_time = self.duration * 60
        return ((self.coeff_calories_1
                * Training.get_mean_speed(self)
                - self.coeff_calories_2)
                * self.weight
                / self.M_IN_KM
                * training_time
                )


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65
    coeff_calories_1: float = 0.035
    coeff_calories_2: float = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        distance = (
            self.action
            * self.LEN_STEP
            / self.M_IN_KM
        )
        speed = (
            distance
            / self.duration
        )
        training_time = self.duration * 60
        return (
            (self.coeff_calories_1
             * self.weight
             + (speed ** 2
                // self.height)
             * self.coeff_calories_2
             * self.weight)
            * training_time
        )


class Swimming(Training):
    """Тренировка: плавание."""
    M_IN_KM: int = 1000
    LEN_STEP: float = 1.38  # 0.65
    coeff_calories_1: float = 1.1

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        speed = (
            self.length_pool
            * self.count_pool
            / self.M_IN_KM
            / self.duration
        )
        return speed

    def get_spent_calories(self) -> float:
        speed = (
            self.length_pool
            * self.count_pool
            / self.M_IN_KM
            / self.duration
        )
        return (
            (speed
             + self.coeff_calories_1)
            * 2
            * self.weight
        )


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    dict_type = {'SWM': Swimming,
                 'RUN': Running,
                 'WLK': SportsWalking
                 }
    if workout_type in dict_type:
        return dict_type[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
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
