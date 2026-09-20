class DownloadError(Exception):
    pass

class ResourceNotFoundError(DownloadError):
    pass

class DownloadTimeOutError(DownloadError):
    pass

class DownloadConnectionError(DownloadError):
    pass