import time

from app.DTO import SpeedTestResult
from app.infrastructure.downloader import DownloaderProtocol


class SpeedTester:
    def __init__(self, downloader: DownloaderProtocol, url: str, request_count: int):
        self.downloader = downloader
        self.url = url
        self.request_count = request_count


    def test(self) -> float:
        results = []
        for _ in range(self.request_count):
            results.append(self._make_request())

        return self._calculate_average_speed_MBps(results)
            


    def _make_request(self) -> SpeedTestResult:
        start = time.perf_counter()
        size = self.downloader.download(self.url)
        elapsed = time.perf_counter() - start
        return SpeedTestResult(elapsed=elapsed, size=size)


    def _calculate_average_speed_MBps(self, requests: list[SpeedTestResult]) -> float:
        total_time = sum(r.elapsed for r in requests)
        total_size = sum(r.size for r in requests)

        return total_size / total_time / 1024 / 1024

        

