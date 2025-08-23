class MedianContainer:
    def __init__(self):
        """Inicializa el contenedor vacío."""
        self.numbers = []

    def add_number(self, num: int):
        """Añade un número al contenedor."""
        self.numbers.append(num)

    def remove_number(self, num: int):
        """Elimina un número del contenedor (si existe)."""
        if num in self.numbers:
            self.numbers.remove(num)


    def get_median(self) -> float:
        """Devuelve la mediana actual o None si está vacío."""
        if not self.numbers:
            return None
        self.numbers.sort()
        mid = len(self.numbers) // 2
        if len(self.numbers) % 2 == 0:
            return (self.numbers[mid-1] + self.numbers[mid]) / 2
        return self.numbers[mid]


# Tests Q1
def test_median_container():
    mc = MedianContainer()
    assert mc.get_median() is None
    mc.add_number(5)
    assert mc.get_median() == 5
    mc.add_number(10)
    # mediana = (5 + 10)/2 = 7.5
    assert mc.get_median() == 7.5
    mc.remove_number(5)
    assert mc.get_median() == 10
    mc.remove_number(100)  # No debería fallar aunque el número no exista
    assert mc.get_median() == 10

if __name__ == "__main__":
    test_median_container()
    print("Todos los tests pasaron correctamente")
