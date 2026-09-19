from dataclasses import dataclass

@dataclass
class SpeedTestResult:
    errors: str | None = None
    size: int | None = None
    elapsed: float | None = None


@dataclass
class DownloadResult:
    errors: str | None = None
    size: int | None = None