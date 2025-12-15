class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Добавление элемента в стэк (в наш список)
        """

        self.items.append(item)
        print(f"Элемент добавлен в стэк: {item}")


    def pop(self):
        """
        Удаление верхнего элемента в стэке
        """

        item = self.items.pop()
        print(f"Удалённый из стэка элемент: {item}")
        return item
    

    def peek(self):
        """
        Просмотр верхнего элемента
        """

        return_items = f"Верхний элемент: {self.items[-1]}"
        return return_items
    
s = Stack()
s.push(3)
s.push(2)
s.push(1)
s.pop()
b = s.peek()
print(b)
    
# s.peek()