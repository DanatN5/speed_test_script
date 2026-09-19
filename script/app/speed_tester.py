from script.infrastructure.downloader import DownloaderProtocol
from script.DTO import SpeedTestResult, DownloadResult
import time


class SpeedTester:
    def __init__(self, downloader: DownloaderProtocol, url: str, request_count: int):
        self.downloader = downloader
        self.url = url
        self.request_count = request_count


    def run(self) -> list[SpeedTestResult]:
        results = []
        for _ in range(self.request_count):
            elapsed, download = self._make_request()

            if download.errors:
                results.append(
                    SpeedTestResult(errors=download.errors)
                    )
            else:
                results.append(
                    SpeedTestResult(
                        size=download.size,
                        elapsed=elapsed
                    )
                )

        return results


    def _make_request(self) -> tuple[float, DownloadResult]:
        start = time.perf_counter()
        data = self.downloader.download(self.url)
        elapsed = time.perf_counter() - start
        return elapsed, data
        

