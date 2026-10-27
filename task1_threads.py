import requests
import time
import threading

class WebDownloader:
    def __init__(self, urls):
        self.urls = urls

    def download_single(self, url):
        """Вспомогательная функция для скачивания одной страницы"""
        try:
            response = requests.get(url, timeout=10)
            print(f"Downloaded {url} (size: {len(response.content)} bytes)")
            return len(response.content)
        except Exception as e:
            print(f"Error downloading {url}: {e}")
            return 0

    def run_sequential(self):
        """Последовательная загрузка"""
        print("\n--- Последовательная загрузка ---")
        start_time = time.time()
        for url in self.urls:
            self.download_single(url)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Время последовательной загрузки: {duration:.2f} сек.")
        return duration

    def run_parallel(self):
        """Параллельная загрузка с использованием потоков"""
        print("\n--- Параллельная загрузка (Threads) ---")
        threads = []
        start_time = time.time()
        
        for url in self.urls:
            thread = threading.Thread(target=self.download_single, args=(url,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        end_time = time.time()
        duration = end_time - start_time
        print(f"Время параллельной загрузки: {duration:.2f} сек.")
        return duration

    def compare(self):
        """Сравнение результатов"""
        seq_time = self.run_sequential()
        par_time = self.run_parallel()
        
        print("\n--- Результаты сравнения ---")
        print(f"Последовательно: {seq_time:.2f} сек.")
        print(f"Параллельно:     {par_time:.2f} сек.")
        if par_time < seq_time:
            print(f"Параллельная загрузка быстрее в {seq_time / par_time:.2f} раз(а).")
        else:
            print("Параллельная загрузка не дала выигрыша (возможно, сработал лимит сети).")