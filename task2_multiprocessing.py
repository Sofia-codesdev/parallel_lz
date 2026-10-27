import multiprocessing
import random

class PipeWorker:
    def __init__(self):
        # Создаем Pipe: parent_conn и child_conn
        self.parent_conn, self.child_conn = multiprocessing.Pipe()
        self.numbers = [random.randint(-1000000, 1000000) for _ in range(1000)]

    def generator_process(self, conn):
        """Процесс 1: Генерирует числа и отправляет их"""
        print(f"[Генератор] Сгенерировано {len(self.numbers)} чисел. Отправка...")
        for num in self.numbers:
            conn.send(num)
        conn.send(None)  # Сигнал завершения (Sentinel)
        conn.close()

    def calculator_process(self, conn):
        """Процесс 2: Получает числа и вычисляет квадраты"""
        print("[Вычислитель] Начало работы...")
        count = 0
        while True:
            try:
                num = conn.recv()
                if num is None:
                    break
                # Вычисляем квадрат (здесь можно добавить логику сохранения, 
                # но для демонстрации просто считаем)
                _ = num ** 2 
                count += 1
            except EOFError:
                break
        print(f"[Вычислитель] Обработано {count} чисел. Завершение.")
        conn.close()

    def run(self):
        print("\n--- Задание 2: Multiprocessing Pipe ---")
        
        # Создаем процессы
        p1 = multiprocessing.Process(target=self.generator_process, args=(self.child_conn,))
        p2 = multiprocessing.Process(target=self.calculator_process, args=(self.parent_conn,))

        # Запускаем
        p1.start()
        p2.start()

        # Ожидаем завершения
        p1.join()
        p2.join()
        print("Оба процесса завершены.")