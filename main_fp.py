from typing import Any, Tuple
from stack_fp import (
    # Стек
    create_stack, stack_push, stack_pop, stack_peek,
    stack_is_empty, stack_size, stack_to_str, Stack,
    # Очередь
    create_queue, queue_enqueue, queue_dequeue, queue_front,
    queue_is_empty, queue_size, queue_to_str, Queue
)

def demonstrate_stack_fp() -> None:
    """Демонстрация работы стека в функциональном стиле"""
    print("=== Демонстрация стека (Функциональный стиль) ===")
    
    # Создаем стек
    stack: Stack[int] = create_stack()
    print(f"Создан пустой стек: {stack_to_str(stack)}")
    
    # Добавляем элементы (иммутабельно - каждый раз создаем новый стек)
    print("\nДобавляем элементы 10, 20, 30 в стек:")
    stack = stack_push(stack, 10)
    stack = stack_push(stack, 20)
    stack = stack_push(stack, 30)
    
    print(f"Стек после добавления: {stack_to_str(stack)}")
    print(f"Вершина стека: {stack_peek(stack)}")
    print(f"Размер стека: {stack_size(stack)}")
    
    # Удаляем элементы
    print("\nУдаляем элементы из стека:")
    while not stack_is_empty(stack):
        item, stack = stack_pop(stack)
        print(f"Извлечен элемент: {item}, новый стек: {stack_to_str(stack)}")
    
    print(f"Стек пуст: {stack_is_empty(stack)}")

def demonstrate_queue_fp() -> None:
    """Демонстрация работы очереди в функциональном стиле"""
    print("\n=== Демонстрация очереди (Функциональный стиль) ===")
    
    # Создаем очередь
    queue: Queue[str] = create_queue()
    print(f"Создана пустая очередь: {queue_to_str(queue)}")
    
    # Добавляем элементы (иммутабельно - каждый раз создаем новую очередь)
    print("\nДобавляем элементы 'X', 'Y', 'Z' в очередь:")
    queue = queue_enqueue(queue, 'X')
    queue = queue_enqueue(queue, 'Y')
    queue = queue_enqueue(queue, 'Z')
    
    print(f"Очередь после добавления: {queue_to_str(queue)}")
    print(f"Первый элемент очереди: {queue_front(queue)}")
    print(f"Размер очереди: {queue_size(queue)}")
    
    # Удаляем элементы
    print("\nУдаляем элементы из очереди:")
    while not queue_is_empty(queue):
        item, queue = queue_dequeue(queue)
        print(f"Извлечен элемент: {item}, новая очередь: {queue_to_str(queue)}")
    
    print(f"Очередь пуста: {queue_is_empty(queue)}")

def complex_example() -> None:
    """Пример более сложного использования - симуляция обработки задач"""
    print("\n=== Пример: Симуляция обработки задач ===")
    
    # Создаем очередь задач
    tasks: Queue[str] = create_queue()
    
    # Добавляем задачи
    task_list = ["Задача 1", "Задача 2", "Задача 3", "Задача 4"]
    for task in task_list:
        tasks = queue_enqueue(tasks, task)
        print(f"Добавлена в очередь: {task}")
    
    # Создаем стек для выполненных задач
    completed: Stack[str] = create_stack()
    
    # Обрабатываем задачи
    print("\nОбработка задач:")
    while not queue_is_empty(tasks):
        task, tasks = queue_dequeue(tasks)
        print(f"Обрабатывается: {task}")
        
        # Помещаем в стек выполненных задач
        completed = stack_push(completed, f"Выполнено: {task}")
    
    # Выводим выполненные задачи в обратном порядке
    print("\nВыполненные задачи (в обратном порядке):")
    while not stack_is_empty(completed):
        task, completed = stack_pop(completed)
        print(f"  {task}")

def main() -> None:
    """Основная функция для демонстрации"""
    demonstrate_stack_fp()
    demonstrate_queue_fp()
    complex_example()

if __name__ == "__main__":
    main()