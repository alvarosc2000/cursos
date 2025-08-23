# =========================
# Simulacro ICA #3 – Código Listo
# =========================

# --- EJERCICIO 1: InventoryManager ---
class InventoryManager:
    def __init__(self):
        """Inicializa un inventario vacío."""
        self.items = {}  # {nombre: cantidad}

    def add_item(self, name: str, quantity: int):
        """Agrega una cantidad al inventario, o crea el item si no existe."""
        self.items[name] = self.items.get(name, 0) + quantity


    def remove_item(self, name: str, quantity: int):
        """Remueve cantidad del inventario, no permite negativas."""
        if name in self.items:
            self.items[name] -= quantity
            if self.items[name] <= 0:
                del self.items[name]

    def get_total_items(self) -> int:
        """Devuelve el total de tipos de items en inventario."""
        return len(self.items)


# --- EJERCICIO 2: BankAccount (Encapsulación) ---
class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.__balance = balance  # atributo privado

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount: float):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return amount
        return 0

    def get_balance(self) -> float:
        return self.__balance


# --- EJERCICIO 3: Logger (Singleton Pattern) ---
class Logger:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.logs = []
        return cls.__instance

    def log(self, message: str):
        self.logs.append(message)

    def get_logs(self):
        return self.logs


# --- EJERCICIO 4: NotificationCenter (Observer Pattern) ---
class NotificationCenter:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, func):
        if func not in self.subscribers:
            self.subscribers.append(func)

    def notify(self, message: str):
        for func in self.subscribers:
            func(message)


# =========================
# TESTS DEL SIMULACRO
# =========================

def test_inventory_manager():
    inv = InventoryManager()
    inv.add_item("apple", 10)
    inv.add_item("banana", 5)
    inv.add_item("apple", 3)
    assert inv.items["apple"] == 13
    inv.remove_item("banana", 2)
    assert inv.items["banana"] == 3
    inv.remove_item("banana", 5)
    assert "banana" not in inv.items
    print("InventoryManager tests passed ✅")


def test_bank_account():
    acc = BankAccount("Alice", 100)
    acc.deposit(50)
    assert acc.get_balance() == 150
    withdrawn = acc.withdraw(70)
    assert withdrawn == 70
    assert acc.get_balance() == 80
    withdrawn = acc.withdraw(100)
    assert withdrawn == 0
    assert acc.get_balance() == 80
    print("BankAccount tests passed ✅")


def test_logger():
    logger1 = Logger()
    logger2 = Logger()
    assert logger1 is logger2  # Singleton
    logger1.log("Start")
    logger2.log("Process")
    assert logger1.get_logs() == ["Start", "Process"]
    print("Logger tests passed ✅")


def test_notification_center():
    messages = []

    def subscriber(msg):
        messages.append(msg)

    nc = NotificationCenter()
    nc.subscribe(subscriber)
    nc.notify("Hello")
    nc.notify("World")
    assert messages == ["Hello", "World"]
    print("NotificationCenter tests passed ✅")


# =========================
# EJECUCIÓN DE TESTS
# =========================

if __name__ == "__main__":
    print("----- Simulacro ICA #3 -----")
    print("Tiempo sugerido: 90 minutos para completarlo.\n")

    test_inventory_manager()
    test_bank_account()
    test_logger()
    test_notification_center()

    print("\nTodos los tests completados ✅ ¡Simulacro listo!")
