import time
import random


def waiting_game():
    print("Welcome to the waiting game")
    interval = random.randint(2, 4)
    print(f"Your goal is to wait for {interval} seconds")
    input("--- press ENTER to begin ---")

    start_time = time.perf_counter()

    input("--- Press ENTER to stop ---")
    end_time = time.perf_counter()

    delta = end_time - start_time
    if delta == interval:
        print(f"Congratulations! You waited exactly {interval} seconds")
    elif delta > interval:
        print(
            f"You waited for {delta} seconds which is longer than {interval}")
    else:
        print(f"You waited {delta} seconds which is less than {interval}")


if __name__ == "__main__":
    waiting_game()
