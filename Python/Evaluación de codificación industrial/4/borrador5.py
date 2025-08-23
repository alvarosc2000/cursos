# --- EJERCICIO 1: LibraryManager ---
class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn: str, title: str, author: str):
        pass

    def remove_book(self, isbn: str):
        pass

    def get_book(self, isbn: str):
        pass


# --- EJERCICIO 2: BankAccount ---
class BankAccount:
    def __init__(self):
        self.accounts = {}
# --- EJERCICIO 1: LibraryManager ---
class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn: str, title: str, author: str):
        pass

    def remove_book(self, isbn: str):
        pass

    def get_book(self, isbn: str):
        pass


# --- EJERCICIO 2: BankAccount ---
class BankAccount:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id: int, initial_balance: float):
        pass

    def deposit(self, account_id: int, amount: float):
        pass

    def withdraw(self, account_id: int, amount: float):
        pass

    def get_balance(self, account_id: int) -> float:
        pass


# --- EJERCICIO 3: NotificationService ---
class NotificationService:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, func):
        pass

    def notify(self, message: str):
        pass


# --- EJERCICIO 4: SettingsManager (Singleton) ---
class SettingsManager:
    __instance = None

    def __new__(cls):
        pass

    def set(self, key: str, value):
        pass

    def get(self, key: str):
        pass


# =========================
# TESTS ICA #5
# =========================

def test_library_manager():
    lm = LibraryManager()
    lm.add_book("123", "Python 101", "Alice")
    lm.add_book("456", "Data Structures", "Bob")
    assert lm.get_book("123")["author"] == "Alice"
    lm.remove_book("123")
    assert lm.get_book("123") is None
    print("LibraryManager tests passed ✅")

def test_bank_account():
    ba = BankAccount()
    ba.create_account(1, 100.0)
    ba.deposit(1, 50.0)
    ba.withdraw(1, 30.0)
    assert ba.get_balance(1) == 120.0
    print("BankAccount tests passed ✅")

def test_notification_service():
    msgs = []

    def func(msg):
        msgs.append(msg)

    ns = NotificationService()
    ns.subscribe(func)
    ns.notify("Hello")
    assert msgs == ["Hello"]
    print("NotificationService tests passed ✅")

def test_settings_manager():
    s1 = SettingsManager()
    s2 = SettingsManager()
    s1.set("volume", 80)
    assert s2.get("volume") == 80
    assert s1 is s2
    print("SettingsManager tests passed ✅")


# =========================
# EJECUCIÓN DE TESTS
# =========================

if __name__ == "__main__":
    print("----- Tests ICA #4 -----")
    test_inventory_manager()
    test_customer_manager()
    test_event_notifier()
    test_configuration()

    print("\n----- Tests ICA #5 -----")
    test_library_manager()
    test_bank_account()
    test_notification_service()
    test_settings_manager()

    print("\nTodos los tests completados ✅ ¡Simulacros listos!")

    def create_account(self, account_id: int, initial_balance: float):
        pass

    def deposit(self, account_id: int, amount: float):
        pass

    def withdraw(self, account_id: int, amount: float):
        pass

    def get_balance(self, account_id: int) -> float:
        pass


# --- EJERCICIO 3: NotificationService ---
class NotificationService:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, func):
        pass

    def notify(self, message: str):
        pass


# --- EJERCICIO 4: SettingsManager (Singleton) ---
class SettingsManager:
    __instance = None

    def __new__(cls):
        pass

    def set(self, key: str, value):
        pass

    def get(self, key: str):
        pass

# =========================
# TESTS ICA #5
# =========================
def test_library_manager():
    lib = LibraryManager()
    lib.add_book("123", "Python 101", "Alice")
    lib.add_book("456", "Java Basics", "Bob")
    assert lib.get_book("123")["title"] == "Python 101"
    lib.remove_book("123")
    assert lib.get_book("123") is None
    print("LibraryManager tests passed ✅")


def test_bank_account():
    bank = BankAccount()
    bank.create_account(1, 1000)
    bank.deposit(1, 500)
    assert bank.get_balance(1) == 1500
    bank.withdraw(1, 300)
    assert bank.get_balance(1) == 1200
    bank.withdraw(1, 2000)  # no debería permitir
    assert bank.get_balance(1) == 1200
    print("BankAccount tests passed ✅")


def test_notification_service():
    triggered = []

    def listener(msg):
        triggered.append(msg)

    service = NotificationService()
    service.subscribe(listener)
    service.notify("Test message")
    assert triggered == ["Test message"]
    print("NotificationService tests passed ✅")


def test_settings_manager():
    s1 = SettingsManager()
    s2 = SettingsManager()
    s1.set("volume", 80)
    assert s2.get("volume") == 80  # singleton
    s2.set("brightness", 50)
    assert s1.get("brightness") == 50
    print("SettingsManager tests passed ✅")


if __name__ == "__main__":
    print("----- Simulacro ICA #5 -----")
    test_library_manager()
    test_bank_account()
    test_notification_service()
    test_settings_manager()
    print("Todos los tests completados ✅ ¡Simulacro ICA #5 listo!")
