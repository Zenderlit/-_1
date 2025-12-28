from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')

class Stack(Generic[T]):
    """Класс Stack (стек) - структура данных LIFO (Last In, First Out)"""
    
    def __init__(self) -> None:
        """Инициализация пустого стека"""
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        """Добавление элемента на вершину стека"""
        self._items.append(item)
    
    def pop(self) -> Optional[T]:
        """Удаление и возврат элемента с вершины стека"""
        if not self.is_empty():
            return self._items.pop()
        return None
    
    def peek(self) -> Optional[T]:
        """Просмотр элемента на вершине стека без удаления"""
        if not self.is_empty():
            return self._items[-1]
        return None
    
    def is_empty(self) -> bool:
        """Проверка, пуст ли стек"""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Возвращает количество элементов в стеке"""
        return len(self._items)
    
    def __str__(self) -> str:
        """Строковое представление стека"""
        return f"Stack({self._items})"
    
    def __repr__(self) -> str:
        """Представление стека для отладки"""
        return f"Stack(items={self._items})"


class Queue(Generic[T]):
    """Класс Queue (очередь) - структура данных FIFO (First In, First Out)"""
    
    def __init__(self) -> None:
        """Инициализация пустой очереди"""
        self._items: List[T] = []
    
    def enqueue(self, item: T) -> None:
        """Добавление элемента в конец очереди"""
        self._items.append(item)
    
    def dequeue(self) -> Optional[T]:
        """Удаление и возврат первого элемента очереди"""
        if not self.is_empty():
            return self._items.pop(0)
        return None
    
    def front(self) -> Optional[T]:
        """Просмотр первого элемента очереди без удаления"""
        if not self.is_empty():
            return self._items[0]
        return None
    
    def is_empty(self) -> bool:
        """Проверка, пуста ли очередь"""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Возвращает количество элементов в очереди"""
        return len(self._items)
    
    def __str__(self) -> str:
        """Строковое представление очереди"""
        return f"Queue({self._items})"
    
    def __repr__(self) -> str:
        """Представление очереди для отладки"""
        return f"Queue(items={self._items})"