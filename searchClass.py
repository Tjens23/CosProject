import time


class search:

    def linearsearch(list, target):
        list.sort()
        print(f"Sorted list {list}")
        start_time = time.time()
        for i in range(len(list)):
            if list[i] == target:
                elapsed_time = (time.time() - start_time)*1000
                print(f"Time elapsed: {elapsed_time} ms")
                return i
        elapsed_time = time.time() - start_time
        print(f"Time elapsed: {elapsed_time} ms")
        return None

    # Using the time module to calculate the time it takes to run the function
    def binarysearch(lst, target) -> [int, None]:
        lst.sort()
        print(f"Sorted list {lst}")
        start_time = time.time()
        first = 0
        last = len(lst) - 1

        while first <= last:
            midpoint = (first + last) // 2
            if lst[midpoint] == target:
                elapsed_time = time.time() - start_time * 1000
                print(f"Time elapsed: {elapsed_time} ms")
                return midpoint
            elif lst[midpoint] < target:
                first = midpoint + 1
            else:
                last = midpoint - 1

        elapsed_time = time.time() - start_time
        print(f"Time elapsed: {elapsed_time} ms")
        return None
