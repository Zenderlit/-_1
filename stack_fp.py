from typing import TypeVar, Generic, Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from typing import Protocol

T = TypeVar('T')

# Протокол для типизации
class StackProtocol(Protocol[T]):
    items: List[T]

class QueueProtocol(Protocol[T]):
    items: List[T]

# Типы для структур данных
@dataclass
class Stack(Generic[T]):
    """Структура данных Stack (стек)"""
    items: List[T]

@dataclass
class Queue(Generic[T]):
    """Структура данных Queue (очередь)"""
    items: List[T]

# ========== Функции для работы со стеком ==========

def create_stack() -> Stack[Any]:
    """Создание пустого стека"""
    return Stack(items=[])

def stack_push(stack: Stack[T], item: T) -> Stack[T]:
    """Добавление элемента на вершину стека"""
    return Stack(items=stack.items + [item])

def stack_pop(stack: Stack[T]) -> Tuple[Optional[T], Stack[T]]:
    """Удаление и возврат элемента с вершины стека"""
    if stack_is_empty(stack):
        return None, stack
    
    new_items = stack.items.copy()
    popped_item = new_items.pop()
    return popped_item, Stack(items=new_items)

def stack_peek(stack: Stack[T]) -> Optional[T]:
    """Просмотр элемента на вершине стека без удаления"""
    if stack_is_empty(stack):
        return None
    return stack.items[-1]

def stack_is_empty(stack: Stack[T]) -> bool:
    """Проверка, пуст ли стек"""
    return len(stack.items) == 0

def stack_size(stack: Stack[T]) -> int:
    """Возвращает количество элементов в стеке"""
    return len(stack.items)

def stack_to_str(stack: Stack[T]) -> str:
    """Строковое представление стека"""
    return f"Stack({stack.items})"

# ========== Функции для работы с очередью ==========

def create_queue() -> Queue[Any]:
    """Создание пустой очереди"""
    return Queue(items=[])

def queue_enqueue(queue: Queue[T], item: T) -> Queue[T]:
    """Добавление элемента в конец очереди"""
    return Queue(items=queue.items + [item])

def queue_dequeue(queue: Queue[T]) -> Tuple[Optional[T], Queue[T]]:
    """Удаление и возврат первого элемента очереди"""
    if queue_is_empty(queue):
        return None, queue
    
    new_items = queue.items.copy()
    dequeued_item = new_items.pop(0)
    return dequeued_item, Queue(items=new_items)

def queue_front(queue: Queue[T]) -> Optional[T]:
    """Просмотр первого элемента очереди без удаления"""
    if queue_is_empty(queue):
        return None
    return queue.items[0]

def queue_is_empty(queue: Queue[T]) -> bool:
    """Проверка, пуста ли очередь"""
    return len(queue.items) == 0

def queue_size(queue: Queue[T]) -> int:
    """Возвращает количество элементов в очереди"""
    return len(queue.items)

def queue_to_str(queue: Queue[T]) -> str:
    """Строковое представление очереди"""
    return f"Queue({queue.items})"