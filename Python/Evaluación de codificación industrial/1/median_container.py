class MedianContainer:
    def __init__(self):
        self.numbers = []

    def add_number(self, num):
        self.numbers.append(num)

    def remove_number(self, num):
        if num in self.numbers:
            self.numbers.remove(num)

    def get_median(self):
        n = len(self.numbers)
        if n == 0:
            return None

        # Crear una copia ordenada
        sorted_nums = sorted(self.numbers)

        mid = n // 2
        if n % 2 == 0:  # par
            return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
        else:           # impar
            return sorted_nums[mid]
