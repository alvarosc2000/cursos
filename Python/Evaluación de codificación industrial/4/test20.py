# =========================
# SUPER EXAMEN INDUSTRIAL – Clase Única
# =========================
# Objetivo: Evaluar codificación estructurada, OOP y manejo de colecciones
# Nivel: Entry/Mid
# Tiempo sugerido: 120 min
# Lenguaje: Python 3
# =========================

class SuperIndustrialExam:
    """
    Clase que contiene varios ejercicios de programación industrial.
    Cada ejercicio está definido con cabeceras y descripción detallada.
    """

    # =========================
    # EJERCICIO 1: Inventario de Piezas
    # =========================
    class Inventory:
        """
        Inventario digital de piezas de repuesto.

        Métodos a implementar:

        - add_item(code: str, quantity: int)
            Agrega piezas al inventario.
            Si el código ya existe, suma la cantidad.
            Lanza ValueError si quantity <= 0.

        - remove_item(code: str, quantity: int) -> bool
            Reduce la cantidad de piezas.
            Retorna True si se eliminó correctamente.
            Retorna False si no hay suficiente stock.

        - get_stock(code: str) -> int
            Retorna cantidad actual del código.
            Retorna 0 si el código no existe.

        - get_total_items() -> int
            Retorna suma total de todas las piezas.

        - list_items() -> list
            Retorna una lista con todos los códigos de inventario.

        - find_item(code: str) -> bool
            Retorna True si el código existe, False si no.
        """
        def __init__(self):
            self.items = {}

        def add_item(self, code: str, quantity: int):
            if not code or quantity <= 0:
                raise ValueError("Argumentos erroneos")
            if code in self.items:
                self.items[code] += quantity
            else:
                self.items[code] = quantity

        def remove_item(self, code: str, quantity: int) -> bool:
            if code in self.items:
                self.items[code] -= quantity
                if self.items[code] == 0:
                    del self.items[code]
                    return True
                return False
            

        def get_stock(self, code: str) -> int:
            return self.items.get(code,0)

        def get_total_items(self) -> int:
            return sum(self.items.values())

        def list_items(self) -> list:
            return self.items.copy()

        def find_item(self, code: str) -> bool:
            return code in self.items

    # =========================
    # EJERCICIO 2: Contenedor de Sensores
    # =========================
    class SensorData:
        """
        Contenedor de lecturas enteras de sensores.

        Métodos a implementar:

        - add_reading(value: int)
            Agrega una nueva lectura.
            Lanza ValueError si value < 0.

        - remove_reading(value: int) -> bool
            Elimina la primera ocurrencia del valor.
            Retorna True si se eliminó, False si no se encontró.

        - get_median() -> float
            Devuelve la mediana de todas las lecturas.
            Lanza RuntimeError si no hay lecturas.

        - get_average() -> float
            Devuelve el promedio de las lecturas.
            Retorna None si no hay lecturas.

        - get_latest() -> int
            Retorna la última lectura agregada.
            Retorna None si no hay lecturas.

        - get_min() -> int
            Retorna la lectura mínima registrada.
            Retorna None si no hay lecturas.

        - get_max() -> int
            Retorna la lectura máxima registrada.
            Retorna None si no hay lecturas.

        - reset()
            Limpia todas las lecturas almacenadas.
        """
        def __init__(self):
            self.lecturas = []

        def add_reading(self, value: int):
            if value < 0:
                raise ValueError("Valor erroneo")
            
            self.lecturas.append(value)

        def remove_reading(self, value: int) -> bool:
            if value in self.lecturas:
                self.lecturas.remove(value)
                return True
            return False

        def get_median(self) -> float:
            if not self.lecturas:
                raise RuntimeError("Array vacio")
            
            ordenadas= sorted(self.lecturas)
            mitad = len(ordenadas) // 2
            
            if mitad % 2 == 0:
                return (ordenadas[mitad-1]+ordenadas[mitad])/2
            else:
                return ordenadas[mitad]

        def get_average(self) -> float:
            if not self.lecturas:
                return None
            total = 0
            for elem in range(len(self.lecturas)):
                total+=self.lecturas[elem]
            
            return total/(len(self.lecturas))

        def get_latest(self) -> int:
            if not self.lecturas:
                return None
            return self.lecturas[-1]

        def get_min(self) -> int:
            if not self.lecturas:
                return None
            return min(self.lecturas)

        def get_max(self) -> int:
            if not self.lecturas:
                return None
            return max(self.lecturas)
        
        def reset(self):
            self.lecturas.clear()
        
    # =========================
    # EJERCICIO 3: Planificación de Producción
    # =========================
    class ProductionPlanner:
        """
        Gestiona órdenes de producción con prioridades.

        Métodos a implementar:

        - add_order(order: str, priority: int)
            Agrega una orden con prioridad.
            Lanza ValueError si order está vacío o priority < 0.

        - pop_next() -> str
            Devuelve la orden con mayor prioridad y la elimina.
            Lanza RuntimeError si no hay órdenes.

        - list_orders() -> list
            Retorna lista de órdenes actuales ordenadas por prioridad descendente.

        - update_priority(order: str, priority: int)
            Actualiza la prioridad de una orden existente.
            Lanza KeyError si la orden no existe.

        - remove_order(order: str) -> bool
            Elimina una orden específica.
            Retorna True si se eliminó, False si no existe.

        - find_order(order: str) -> bool
            Retorna True si la orden existe, False si no.
        """
        def __init__(self):
            self.ordenes = {}

        def add_order(self, order: str, priority: int):
            if not order or priority < 0:
                raise ValueError("error")
            self.ordenes[order] = priority

        def pop_next(self) -> str:
            if not self.ordenes:
                raise RuntimeError("Errores")
            highest = max(self.ordenes, key=lambda t:self.ordenes[t])
            del self.ordenes[highest]
            return highest

        def list_orders(self) -> list:
            return sorted(self.ordenes, key=lambda t:self.ordenes[t], reverse=True)

        def update_priority(self, order: str, priority: int):
            if order not in self.ordenes:
                raise KeyError("erorr en la clave")
            self.ordenes[order] = priority

        def remove_order(self, order: str) -> bool:
            if order in self.ordenes:
                del self.ordenes[order]
                return True
            return False

        def find_order(self, order: str) -> bool:
            return order in self.ordenes

    # =========================
    # EJERCICIO 4: Catálogo Versionado
    # =========================
    class VersionedCatalog:
        """
        Catálogo de productos con control de versiones.

        Métodos a implementar:

        - add_product(name: str, price: float)
            Inserta producto nuevo.
            Lanza RuntimeError si ya existe.
            Guarda snapshot de versión.

        - remove_product(name: str)
            Elimina producto existente.
            Lanza KeyError si no existe.
            Guarda snapshot de versión.

        - update_price(name: str, price: float)
            Actualiza precio de producto existente.
            Lanza KeyError si no existe.
            Guarda snapshot de versión.

        - get_version(index: int) -> dict
            Retorna snapshot de versión específica.
            Lanza IndexError si el índice es inválido.

        - get_latest() -> dict
            Retorna snapshot más reciente.
            Lanza RuntimeError si no hay versiones.

        - list_products() -> list
            Retorna lista de todos los productos actuales.

        - find_product(name: str) -> bool
            Retorna True si producto existe, False si no.

        - get_max_price_product() -> dict
            Retorna el producto con mayor precio unitario.
            Retorna None si catálogo vacío.
        """
        def __init__(self):
            self.productos = {}
            self.versiones = []

        def snapshot(self):
            self.versiones.append(self.productos.copy())

        def add_product(self, name: str, price: float):
            if name in self.productos:
                raise RuntimeError("Producto ya existe")
            self.productos[name] = price
            self.snapshot()

        def remove_product(self, name: str):
            if name not in self.productos:
                raise KeyError("No existe")
            del self.productos[name]
            self.snapshot()

        def update_price(self, name: str, price: float):
            if name not in self.productos:
                raise KeyError("No existe")
            self.productos[name] = price
            self.snapshot()

        def get_version(self, index: int) -> dict:
            if index < 0 or index > len(self.versiones):
                raise RuntimeError("error en las versiones")
            
            return self.versiones[index].copy()

        def get_latest(self) -> dict:
            if not self.versiones:
                raise RuntimeError("Vacio")
            else:
                return self.versiones[-1].copy()

        def list_products(self) -> list:
            return list(self.productos.keys())

        def find_product(self, name: str) -> bool:
            return name in self.productos

        def get_max_price_product(self) -> dict:
            if not self.productos:
                return None
            return (sorted(self.productos, key=lambda t:self.productos[t], reverse=True))

# =========================
# EJERCICIO 5: TemperatureMonitor (Observer Pattern)
# =========================
class TemperatureMonitor:
    """
    Sistema de monitoreo de temperatura con alertas.

    Métodos:

    - add_temperature(value: float)
        Agrega nueva lectura de temperatura y notifica alertas si supera el umbral.

    - subscribe(func)
        Suscribe una función para recibir alertas.

    - notify_alert(value: float)
        Notifica a todos los suscriptores sobre temperatura crítica.

    - get_max_temperature() -> float
        Retorna la temperatura máxima registrada.
        Retorna None si no hay lecturas.

    - get_average_temperature() -> float
        Retorna promedio de temperaturas.
        Retorna None si no hay lecturas.

    - get_min_temperature() -> float
        Retorna la temperatura mínima registrada.
        Retorna None si no hay lecturas.

    - get_latest_temperature() -> float
        Retorna la última lectura registrada.
        Retorna None si no hay lecturas.
    """
    def __init__(self, threshold: float):
        self.temps = []
        self.threshold = threshold
        self.subscribers = []

    def add_temperature(self, value: float):
        if value is None:
            raise ValueError("Temperatura inválida")
        self.temps.append(value)
        if value > self.threshold:
            self.notify_alert(value)

    def subscribe(self, func):
        if callable(func) and func not in self.subscribers:
            self.subscribers.append(func)

    def notify_alert(self, value: float):
        for func in self.subscribers:
            func(value)

    def get_max_temperature(self) -> float:
        if not self.temps:
            return None
        return max(self.temps)

    def get_average_temperature(self) -> float:
        if not self.temps:
            return None
        return sum(self.temps) / len(self.temps)

    def get_min_temperature(self) -> float:
        if not self.temps:
            return None
        return min(self.temps)

    def get_latest_temperature(self) -> float:
        if not self.temps:
            return None
        return self.temps[-1]



# =========================
# TESTS ESQUELETO
# =========================
def run_super_exam_tests():
    print("=== TEST SUPER EXAM ===")

    # Inventory
    inv = SuperIndustrialExam.Inventory()
    inv.add_item("BOLT", 10)
    inv.remove_item("BOLT", 5)
    print("Inventory methods callable ✅")

    # SensorData
    sd = SuperIndustrialExam.SensorData()
    sd.add_reading(10)
    sd.get_average()
    print("SensorData methods callable ✅")

    # ProductionPlanner
    pp = SuperIndustrialExam.ProductionPlanner()
    pp.add_order("Order1", 2)
    pp.pop_next()
    print("ProductionPlanner methods callable ✅")

    # VersionedCatalog
    vc = SuperIndustrialExam.VersionedCatalog()
    vc.add_product("Drill", 100)
    vc.get_latest()
    print("VersionedCatalog methods callable ✅")

    # TemperatureMonitor
    tm = SuperIndustrialExam.TemperatureMonitor(threshold=50)
    tm.add_temperature(55)
    tm.get_max_temperature()
    print("TemperatureMonitor methods callable ✅")


if __name__ == "__main__":
    run_super_exam_tests()
