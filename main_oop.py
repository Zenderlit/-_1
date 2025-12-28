from typing import Any
from stack_oop import Stack, Queue

def demonstrate_stack() -> None:
    """Демонстрация работы стека"""
    print("=== Демонстрация стека (ООП) ===")
    
    # Создаем стек для целых чисел
    stack: Stack[int] = Stack()
    
    # Добавляем элементы
    print("Добавляем элементы 1, 2, 3 в стек")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print(f"Стек после добавления: {stack}")
    print(f"Вершина стека: {stack.peek()}")
    print(f"Размер стека: {stack.size()}")
    
    # Удаляем элементы
    print("\nУдаляем элементы из стека:")
    while not stack.is_empty():
        item = stack.pop()
        print(f"Извлечен элемент: {item}")
    
    print(f"Стек пуст: {stack.is_empty()}")

def demonstrate_queue() -> None:
    """Демонстрация работы очереди"""
    print("\n=== Демонстрация очереди (ООП) ===")
    
    # Создаем очередь для строк
    queue: Queue[str] = Queue()
    
    # Добавляем элементы
    print("Добавляем элементы 'A', 'B', 'C' в очередь")
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    
    print(f"Очередь после добавления: {queue}")
    print(f"Первый элемент очереди: {queue.front()}")
    print(f"Размер очереди: {queue.size()}")
    
    # Удаляем элементы
    print("\nУдаляем элементы из очереди:")
    while not queue.is_empty():
        item = queue.dequeue()
        print(f"Извлечен элемент: {item}")
    
    print(f"Очередь пуста: {queue.is_empty()}")

def main() -> None:
    """Основная функция для демонстрации"""
    demonstrate_stack()
    demonstrate_queue()

if __name__ == "__main__":
    main()