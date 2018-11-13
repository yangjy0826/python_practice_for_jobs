import collections
q = collections.deque()
print(q)
q.append(2)  # add to the right side
q.append(3)
print(q)
q.appendleft(1)  # add to the left side
print(q)
q.pop()  # Remove and return an element from the right side of the deque
print(q)
q.popleft()  # Remove and return an element from the left side of the deque
print(q)