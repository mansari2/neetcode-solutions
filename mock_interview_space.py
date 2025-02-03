class LogProcessor:
    def __init__(self, k: int):
        """Initialize the log processor with a time window k (in seconds)."""
        pass
    
    def ingest_log(self, timestamp: int, message: str) -> None:
        """Process an incoming log entry."""
        pass
    
    def get_last_n_logs(self, n: int) -> List[Tuple[int, str]]:
        """Return the last N logs sorted by timestamp."""
        pass


"""
Logs come out of order

"""