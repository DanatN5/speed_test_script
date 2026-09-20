from typing import Protocol
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from app.errors import (
    DownloadConnectionError,
    DownloadError,
    DownloadTimeOutError,
    ResourceNotFoundError,
)


class DownloaderProtocol(Protocol):
    def download(self, url: str): pass


class UrlLibDownloader:
    def download(self, url: str) -> int:
        try:
            with urlopen(url, timeout=10) as response:
                size = 0

                while chunk := response.read(1024*1024):
                    size += len(chunk)

                return size
        except HTTPError as error:
            if error.code == 404:
                raise ResourceNotFoundError("Ресурс не найден") from error

            raise DownloadError(f"Ошибка: {error.code}")

        except TimeoutError as error:
            raise DownloadTimeOutError("Время запроса истекло") from error

        except URLError as error:
            raise DownloadConnectionError("Не удается установить соединение") from error