# --- EJERCICIO 1: LibraryManager ---
class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn: str, title: str, author: str):
        self.books[isbn] = {"title": title, "author": author}

    def remove_book(self, isbn: str):
        if isbn in self.books:
            del self.books[isbn]

    def get_book(self, isbn: str):
        return self.books.get(isbn)


# --- EJERCICIO 2: BankAccount ---
class BankAccount:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id: int, initial_balance: float):
        self.accounts[account_id] = initial_balance

    def deposit(self, account_id: int, amount: float):
        if account_id in self.accounts:
            self.accounts[account_id] += amount

    def withdraw(self, account_id: int, amount: float):
        if account_id in self.accounts and self.accounts[account_id] >= amount:
            self.accounts[account_id] -= amount

    def get_balance(self, account_id: int) -> float:
        return self.accounts.get(account_id, 0)


# --- EJERCICIO 3: NotificationService ---
class NotificationService:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, func):
        self.subscribers.append(func)

    def notify(self, message: str):
        for func in self.subscribers:
            func(message)


# --- EJERCICIO 4: SettingsManager (Singleton) ---
class SettingsManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.settings = {}
        return cls.__instance

    def set(self, key: str, value):
        self.settings[key] = value

    def get(self, key: str):
        return self.settings.get(key)


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
