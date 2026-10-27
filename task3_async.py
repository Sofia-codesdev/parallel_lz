import asyncio
import time
import random

class AsyncRunner:
    def __init__(self):
        self.delays = [random.uniform(0.5, 2.0) for _ in range(5)]

    async def async_task(self, task_id, delay):
        """Асинхронная задача с задержкой"""
        await asyncio.sleep(delay)
        print(f"Задача {task_id} завершена (задержка {delay:.2f} сек)")
        return task_id

    def run_sequential_sync(self):
        """Последовательное выполнение (имитация через time.sleep)"""
        print("\n--- Последовательное выполнение ---")
        start = time.time()
        for i, delay in enumerate(self.delays):
            time.sleep(delay)
            print(f"Задача {i+1} завершена (задержка {delay:.2f} сек)")
        end = time.time()
        duration = end - start
        print(f"Общее время (последовательно): {duration:.2f} сек")
        return duration

    async def run_parallel_async(self):
        """Параллельное асинхронное выполнение"""
        print("\n--- Асинхронное (параллельное) выполнение ---")
        start = time.time()
        tasks = []
        for i, delay in enumerate(self.delays):
            tasks.append(self.async_task(i+1, delay))
        
        await asyncio.gather(*tasks)
        
        end = time.time()
        duration = end - start
        print(f"Общее время (асинхронно): {duration:.2f} сек")
        return duration

    def compare(self):
        # Запуск последовательного режима
        seq_duration = self.run_sequential_sync()
        
        # Запуск асинхронного режима
        asyncio.run(self.run_parallel_async())