import time
import threading
import random

def main() -> None:
    time.sleep(1)
    open_file = open("new-file.txt", "a")
    for i in range(1):
        num = random.randint(0, 1200)
        open_file.write(str(num) + '\n')
    open_file.close()
main()


if __name__ == "__main__":
    times = 1000
    threads = []

    start = time.time()
    for _ in range(times):
        open('new-file.txt', 'a')
    print(f"Времы выполнения {time.time() - start}")

    for i in range(times):
        thread = threading.Thread(target=main, args=())
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
