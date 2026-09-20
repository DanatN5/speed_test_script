from app.errors import DownloadError
from app.infrastructure.downloader import UrlLibDownloader
from app.presentation.parser import Parser
from app.presentation.presenter import Presenter
from app.speed_tester.speed_tester import SpeedTester


def main() -> None:
    args = Parser().parse()

    downloader = UrlLibDownloader()
    speed_tester = SpeedTester(
        downloader=downloader,
        url=args.url,
        request_count=args.requests
    )

    presenter = Presenter()

    try:
        speed = speed_tester.test()
    except DownloadError as error:
        presenter.show_error(error=error)
    else:
        presenter.show_result(speed=speed)


if __name__ == "__main__":
    main()