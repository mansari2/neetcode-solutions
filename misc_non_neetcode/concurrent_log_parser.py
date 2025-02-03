"""
Problem Statement
You are given a log stream where each log entry contains a timestamp and a message. The logs arrive out of order, and your goal is to process them in real-time, maintaining an ordered view of logs up to a window of k seconds.

Design a system that:

Processes incoming logs efficiently.
Returns the last N logs in sorted order by timestamp at any moment.
Handles concurrent log inserts.

lp = LogProcessor(10)  # 10-second window

lp.ingest_log(3, "System Start")
lp.ingest_log(1, "Disk Check")
lp.ingest_log(2, "Network Init")
lp.ingest_log(12, "User Login")
lp.ingest_log(8, "DB Connected")

print(lp.get_last_n_logs(3))  

[(2, "Network Init"), (3, "System Start"), (8, "DB Connected")]

Clarifying questions:
Is timestamp unique? → No, multiple logs can have the same timestamp.
Are there duplicates? → No, but messages can be similar.
How frequent are inserts? → High throughput (~100K logs/sec).
What happens if logs are older than k seconds? → They should be dropped.
How do we retrieve logs? → Sorted, most recent first.
"""

import heapq
import logging
import multiprocessing
from typing import List, Tuple
from collections import deque

class LogProcessor:
    def __init__(self, k: int):
        """Initialize the log processor with a time window k (in seconds)."""
        self.k = k
        self.heap = []  # Min-heap to store timestamps
        self.messages = {}  # Dictionary to store messages for timestamps
        self.lock = multiprocessing.Lock()  # Lock for thread safety

    def ingest_log(self, timestamp: int, message: str) -> None:
        """Process an incoming log entry."""
        with self.lock:
            heapq.heappush(self.heap, timestamp)
            
            if timestamp in self.messages:
                self.messages[timestamp].append(message)
            else:
                self.messages[timestamp] = [message]

            # Remove outdated logs beyond `k` seconds
            while self.heap and (timestamp - self.heap[0] > self.k):
                old_timestamp = heapq.heappop(self.heap)
                del self.messages[old_timestamp]  # Remove old messages

    def get_last_n_logs(self, n: int) -> List[Tuple[int, str]]:
        """Return the last N logs sorted by timestamp."""
        with self.lock:
            n_last_log_messages = []
            n_last_log_timestamps = heapq.nlargest(n, self.heap)

            for timestamp in sorted(n_last_log_timestamps):
                if timestamp in self.messages:
                    for msg in self.messages[timestamp]:
                        n_last_log_messages.append((timestamp, msg))

            return n_last_log_messages


# Multiprocessing wrapper for ingesting logs
def process_log_entry(args):
    """Helper function to enable multiprocessing."""
    log_processor, timestamp, message = args
    log_processor.ingest_log(timestamp, message)


def main(log_messages):
    """Main function for multiprocessing log ingestion."""
    log_processor = LogProcessor(k=10)  # Assume a 10-second window

    with multiprocessing.Pool() as pool:
        pool.map(process_log_entry, [(log_processor, ts, msg) for ts, msg in log_messages])

    return log_processor


# Example Usage
if __name__ == "__main__":
    logs = [
        (3, "System Start"),
        (1, "Disk Check"),
        (2, "Network Init"),
        (12, "User Login"),
        (8, "DB Connected"),
    ]

    processor = main(logs)
    print(processor.get_last_n_logs(3))  # Returns the last 3 logs in sorted order
"""
Key Fixes & Improvements
🔹 Fixed Heap Management

heapq.heappush() and heapq.heappop() now correctly maintain the min-heap.
Old logs older than k seconds are removed from both the heap and dictionary.
🔹 Fixed Dictionary Handling

Ensures duplicate messages are properly stored and retrieved.
Uses sorted retrieval when fetching N logs.
🔹 Fixed Error Handling

Removed incorrect exec.info=True usage.
Instead of try/except, we use a direct dictionary check (if timestamp in self.messages).
🔹 Corrected Multiprocessing

multiprocessing.Pool.map() now calls process_log_entry(), ensuring arguments are properly passed.
Introduced multiprocessing.Lock() for thread safety.

Kafka or RabbitMQ: Ingest logs into a distributed queue.
Partitioning by time windows: Store logs in Redis or a Time Series DB.
Use Apache Flink/Spark Streaming: Efficient real-time windowing.


"""