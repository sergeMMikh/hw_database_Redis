from pymemcache.client import base
import datetime
import time


if __name__ == '__main__':

    client = base.Client(('127.0.0.1', 11211))
    start = datetime.datetime.now()

    # Add keys with TTL 5s
    print("Add keys")
    for i in range(1, 6):
        time.sleep(1)
        client.add(f'key{i}', f'data{i}', 5)
        print(f"Working time: {datetime.datetime.now() - start}\t add key: key{i}")

    # Check keys
    print("\nCheck keys")
    for j in range (1, 7):
        for i in range(1, 6):
            key_name = f"key{i}"
            print(f"Working time: {datetime.datetime.now() - start}\tkey{i}: {client.get(key_name)}")
        time.sleep(1)
        print("")
