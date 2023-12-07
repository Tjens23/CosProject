import random
from searchClass import search

if __name__ == "__main__":
    lst = [random.randint(0, 5000) for _ in range(1000)]
    print(f"Linear search {search.linearsearch(lst, 500)}")
    for i in range(2):
        print("")
    print(f"Binary search {search.binarysearch(lst, 500)}")