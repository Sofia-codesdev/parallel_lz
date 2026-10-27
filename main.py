from task1_threads import WebDownloader
from task2_multiprocessing import PipeWorker
from task3_async import AsyncRunner

def main():
    print("=== Лабораторная работа №6 (Вариант 1) ===")

    # --- Задание 1 ---
    urls = [
        "https://www.google.com",
        "https://www.github.com",
        "https://www.python.org",
        "https://www.stackoverflow.com",
        "https://www.wikipedia.org",
        "https://www.reddit.com",
        "https://www.youtube.com",
        "https://www.amazon.com",
        "https://www.microsoft.com",
        "https://www.apple.com"
    ]
    downloader = WebDownloader(urls)
    downloader.compare()

    # --- Задание 2 ---
    pipe_worker = PipeWorker()
    pipe_worker.run()

    # --- Задание 3 ---
    async_runner = AsyncRunner()
    async_runner.compare()

if __name__ == "__main__":
    main()