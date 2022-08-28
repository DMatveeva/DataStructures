class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() == 0:
            return None
        else:
            return self.stack[self.size() - 1]


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size


    def DepthFirstSearch(self, VFrom, VTo):
        for v in self.vertex:
            v.Hit = False
        vertex_from = self.vertex[VFrom]
        stack = Stack()
        vertex_from.Hit = True
        stack.push(vertex_from)
        self.depth_first_search_recursive(VFrom, VTo, stack)
        return stack.stack

    def depth_first_search_recursive(self, v_from, v_to, stack):
        vertex_from = self.vertex[v_from]
        i = 0
        while i < self.max_vertex:
            if self.m_adjacency[v_from][i] == 0:
                i += 1
                continue
            vertex = self.vertex[i]
            if vertex.Hit:
                i += 1
                continue
            vertex_from.Hit = True
            stack.push(vertex)
            if v_to == i:
                return stack
            else:
                self.depth_first_search_recursive(i, v_to, stack)
            i += 1
        stack.pop()
        if stack.size() == 0:
            return stack
        else:
            v = stack.peek()
            v.Hit = True
            self.depth_first_search_recursive(stack.peek(), v_to, stack)

    # узлы задаются позициями в списке vertex
    # возвращается список узлов -- путь из VFrom в VTo
    # или [] если пути нету

    def AddVertex(self, v):
        new_vertex = Vertex(v)
        new_index = 0
        while new_index < self.max_vertex:
            if not self.vertex[new_index]:
                break
            new_index += 1
        self.vertex[new_index] = new_vertex
        j = 0
        while j <= new_index:
            self.m_adjacency[j][new_index] = 0
            self.m_adjacency[new_index][j] = 0
            j += 1

    def RemoveVertex(self, v):
        i = v
        while i < self.max_vertex - 1:
            self.vertex[i] = self.vertex[i + 1]
            i += 1
        self.vertex[self.max_vertex - 1] = None
        x = 0

        while x < self.max_vertex - 1:
            y = v + 1
            while y < self.max_vertex - 1:
                self.m_adjacency[y][x] = self.m_adjacency[y + 1][x]
                y += 1
            x += 1

        y = 0
        while y < self.max_vertex - 1:
            x = v + 1
            while x < self.max_vertex - 1:
                self.m_adjacency[y][x] = self.m_adjacency[y][x + 1]
                x += 1
            y += 1

    def IsEdge(self, v1, v2):
        return True if self.m_adjacency[v1][v2] == 1 else False


    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0






