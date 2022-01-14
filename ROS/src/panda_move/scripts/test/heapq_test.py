import itertools
import heapq

# pq = []                         
# entry_finder = {}               
REMOVED = '<removed-task>'      
# counter = itertools.count()

# def add_task(task, priority=0):
#     if task in entry_finder:
#         remove_task(task)
#     count = next(counter)
#     entry = [priority, count, task]
#     # entry를 entry_finder와 pq에 넣는다 -> 동일 포인터로 연결된다
#     # 따라서, entry_finder에서 원하는 entry를 찾아서 task를 바꾸면 pq에서도 task가 바뀐다
#     entry_finder[task] = entry
#     heapq.heappush(pq, entry)

# def remove_task(task):
#     entry = entry_finder.pop(task)
#     entry[-1] = REMOVED
#     print(entry)

# def pop_task():
#     while pq:
#         priority, count, task = heapq.heappop(pq)
#         # REMOVED가 pop되면 REMOVED가 아닌것이 pop될때까지 반복
#         if task is not REMOVED:
#             del entry_finder[task]
#             return task
#     raise KeyError('pop from an empty priority queue')

# def print_id():
#     print("pq=", end='')
#     for node in pq:
#         print(id(node), end=" ")
#     print()

#     print("ef=", end='')
#     for key, val in entry_finder.items():
#         print(id(val), end=" ")
#     print()

# add_task('b', 1)
# print(pq, entry_finder)
# add_task('a', 2)
# print(pq, entry_finder)
# add_task('c', 7)
# print(pq, entry_finder)
# print_id()
# add_task('a', 9)
# print(pq, entry_finder)
# popped = pop_task()
# print(popped, pq, entry_finder)
# popped = pop_task()
# print(popped, pq, entry_finder)

class PriorityQueue:
    def __init__(self):
        self.pq = []                         
        self.entry_finder = {}
        self.counter = itertools.count()
    
    def push(self, task, priority=0):
        if task in self.entry_finder:
            self.remove_task(task)

        count = next(self.counter)
        entry = [priority, count, task]
        
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove_task(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop(self):
        while self.pq:
            [priority, count, task] = heapq.heappop(self.pq)
            if task is not REMOVED:
                del self.entry_finder[task]
                return task

def main():
    test = PriorityQueue()
    test.push('b', 1)
    print(test.pq, test.entry_finder)
    test.push('a', 2)
    print(test.pq, test.entry_finder)
    test.push('c', 7)
    print(test.pq, test.entry_finder)
    test.push('a', 9)
    print(test.pq, test.entry_finder)
    popped = test.pop()
    print(popped, test.pq, test.entry_finder)
    popped = test.pop()
    print(popped, test.pq, test.entry_finder)

if __name__ == '__main__':
    main()