import threading
import time
import actions, dataGeneration


def print_numbers():
    for i in range(1, 11):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e']:
        print(letter)
        time.sleep(1)

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread3 = threading.Thread(target=dataGeneration.dataGen)

# Start the threads
thread1.start()
thread2.start()
thread3.start()

# Wait for the threads to finish
thread1.join()
thread2.join()
thread3.join()

# The program will now exit
