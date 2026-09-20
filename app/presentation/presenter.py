from app.errors import DownloadError


class Presenter:
    def show_error(self, error: DownloadError) -> None:
        print(f"Ошибка: {error}")


    def show_result(self, speed: float):
        print(f"Скорость: {speed:.2f} MB/s")

