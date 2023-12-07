class Sorting:
    def __init__(self, data):
        self.data = data

    def bubblesort(self):
        for i in range(len(self.data)):
            for j in range(len(self.data)-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
        return self.data

    def mergesort(self):
        if len(self.data) <= 1:
            return self.data

        # Split the list into two halves
        mid = len(self.data) // 2
        left_half = self.data[:mid]
        right_half = self.data[mid:]

        # Recursively sort each half
        left_half = Sorting(left_half).mergesort()
        right_half = Sorting(right_half).mergesort()

        # Merge the sorted halves
        return self.merge(left_half, right_half)

    @staticmethod
    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add the remaining elements, if any
        result.extend(left[i:])
        result.extend(right[j:])

        return result
