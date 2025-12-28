import unittest
from typing import Any

# Импорт ООП-реализации
from stack_oop import Stack, Queue

# Импорт функциональной реализации
from stack_fp import (
    create_stack, stack_push, stack_pop, stack_peek,
    stack_is_empty, stack_size,
    create_queue, queue_enqueue, queue_dequeue, queue_front,
    queue_is_empty, queue_size
)

class TestOOPStack(unittest.TestCase):
    """Тесты для ООП-реализации стека"""
    
    def test_stack_basic_operations(self):
        stack: Stack[int] = Stack()
        
        # Проверка пустого стека
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)
        self.assertIsNone(stack.peek())
        self.assertIsNone(stack.pop())
        
        # Добавление элементов
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        # Проверка состояния
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.peek(), 3)
        
        # Удаление элементов
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertIsNone(stack.pop())
        self.assertTrue(stack.is_empty())

class TestOOPQueue(unittest.TestCase):
    """Тесты для ООП-реализации очереди"""
    
    def test_queue_basic_operations(self):
        queue: Queue[str] = Queue()
        
        # Проверка пустой очереди
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size(), 0)
        self.assertIsNone(queue.front())
        self.assertIsNone(queue.dequeue())
        
        # Добавление элементов
        queue.enqueue('A')
        queue.enqueue('B')
        queue.enqueue('C')
        
        # Проверка состояния
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.front(), 'A')
        
        # Удаление элементов
        self.assertEqual(queue.dequeue(), 'A')
        self.assertEqual(queue.dequeue(), 'B')
        self.assertEqual(queue.dequeue(), 'C')
        self.assertIsNone(queue.dequeue())
        self.assertTrue(queue.is_empty())

class TestFPStack(unittest.TestCase):
    """Тесты для функциональной реализации стека"""
    
    def test_stack_basic_operations(self):
        stack = create_stack()
        
        # Проверка пустого стека
        self.assertTrue(stack_is_empty(stack))
        self.assertEqual(stack_size(stack), 0)
        self.assertIsNone(stack_peek(stack))
        
        popped, _ = stack_pop(stack)
        self.assertIsNone(popped)
        
        # Добавление элементов
        stack = stack_push(stack, 1)
        stack = stack_push(stack, 2)
        stack = stack_push(stack, 3)
        
        # Проверка состояния
        self.assertFalse(stack_is_empty(stack))
        self.assertEqual(stack_size(stack), 3)
        self.assertEqual(stack_peek(stack), 3)
        
        # Удаление элементов
        item1, stack = stack_pop(stack)
        self.assertEqual(item1, 3)
        
        item2, stack = stack_pop(stack)
        self.assertEqual(item2, 2)
        
        item3, stack = stack_pop(stack)
        self.assertEqual(item3, 1)
        
        item4, stack = stack_pop(stack)
        self.assertIsNone(item4)
        self.assertTrue(stack_is_empty(stack))

class TestFPQueue(unittest.TestCase):
    """Тесты для функциональной реализации очереди"""
    
    def test_queue_basic_operations(self):
        queue = create_queue()
        
        # Проверка пустой очереди
        self.assertTrue(queue_is_empty(queue))
        self.assertEqual(queue_size(queue), 0)
        self.assertIsNone(queue_front(queue))
        
        dequeued, _ = queue_dequeue(queue)
        self.assertIsNone(dequeued)
        
        # Добавление элементов
        queue = queue_enqueue(queue, 'A')
        queue = queue_enqueue(queue, 'B')
        queue = queue_enqueue(queue, 'C')
        
        # Проверка состояния
        self.assertFalse(queue_is_empty(queue))
        self.assertEqual(queue_size(queue), 3)
        self.assertEqual(queue_front(queue), 'A')
        
        # Удаление элементов
        item1, queue = queue_dequeue(queue)
        self.assertEqual(item1, 'A')
        
        item2, queue = queue_dequeue(queue)
        self.assertEqual(item2, 'B')
        
        item3, queue = queue_dequeue(queue)
        self.assertEqual(item3, 'C')
        
        item4, queue = queue_dequeue(queue)
        self.assertIsNone(item4)
        self.assertTrue(queue_is_empty(queue))

class TestBothImplementations(unittest.TestCase):
    """Сравнительные тесты обеих реализаций"""
    
    def test_stack_equivalence(self):
        """Проверка эквивалентности поведения стеков"""
        
        # ООП стек
        oop_stack: Stack[int] = Stack()
        oop_stack.push(1)
        oop_stack.push(2)
        oop_stack.push(3)
        
        # Функциональный стек
        fp_stack = create_stack()
        fp_stack = stack_push(fp_stack, 1)
        fp_stack = stack_push(fp_stack, 2)
        fp_stack = stack_push(fp_stack, 3)
        
        # Проверка эквивалентности
        self.assertEqual(oop_stack.size(), stack_size(fp_stack))
        self.assertEqual(oop_stack.peek(), stack_peek(fp_stack))
        
        # Удаление и проверка
        oop_result = oop_stack.pop()
        fp_result, fp_stack = stack_pop(fp_stack)
        self.assertEqual(oop_result, fp_result)
    
    def test_queue_equivalence(self):
        """Проверка эквивалентности поведения очередей"""
        
        # ООП очередь
        oop_queue: Queue[str] = Queue()
        oop_queue.enqueue('X')
        oop_queue.enqueue('Y')
        oop_queue.enqueue('Z')
        
        # Функциональная очередь
        fp_queue = create_queue()
        fp_queue = queue_enqueue(fp_queue, 'X')
        fp_queue = queue_enqueue(fp_queue, 'Y')
        fp_queue = queue_enqueue(fp_queue, 'Z')
        
        # Проверка эквивалентности
        self.assertEqual(oop_queue.size(), queue_size(fp_queue))
        self.assertEqual(oop_queue.front(), queue_front(fp_queue))
        
        # Удаление и проверка
        oop_result = oop_queue.dequeue()
        fp_result, fp_queue = queue_dequeue(fp_queue)
        self.assertEqual(oop_result, fp_result)

if __name__ == '__main__':
    unittest.main()