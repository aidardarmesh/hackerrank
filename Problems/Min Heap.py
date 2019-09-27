class MinHeap:
    items = []
    size = 0

    def get_left_child_index(self, parent_index):
        return 2*parent_index+1
    
    def get_right_child_index(self, parent_index):
        return 2*parent_index+2
    
    def get_parent_index(self, child_index):
        return (child_index-1) // 2

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def left_child(self, index):
        return self.items[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.items[self.get_right_child_index(index)]

    def parent(self, index):
        return self.items[self.get_parent_index(index)]
    
    def is_empty(self):
        return self.size == 0

    def poll(self):
        item = self.items[0]
        self.size -= 1
        self.items[0] = self.items[self.size]
        self.items.pop()
        self.heapify_down()

        return item

    def add(self, item):
        self.items.append(item)
        self.size += 1
        self.heapify_up()
    
    def heapify_up(self):
        index = self.size - 1

        while(self.has_parent(index) and self.parent(index) > self.items[index]):
            parent_index = self.get_parent_index(index)
            self.items[index], self.items[parent_index] = self.items[parent_index], self.items[index]
            index = parent_index
        
    def heapify_down(self):
        index = 0

        while(self.has_left_child(index)):
            smallerChildIndex = self.get_left_child_index(index)

            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smallerChildIndex = self.get_right_child_index(index)
            
            if self.items[index] < self.items[smallerChildIndex]:
                break
                
            self.items[index], self.items[smallerChildIndex] = self.items[smallerChildIndex], self.items[index]
            index = smallerChildIndex

m = MinHeap()
m.add(2)
print(m.items, m.size)
m.add(1)
print(m.items, m.size)
print(m.poll())
print(m.items)
print(m.poll(), m.items)
m.add(8)
m.add(1)
m.add(5)
m.add(9)
print(m.items)
print(m.poll(), m.poll(), m.poll(), m.poll())