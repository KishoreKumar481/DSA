from collections import deque

dq = deque([10, 20, 30])

dq.append(40)
dq.appendleft(5)
dq.extend([50, 60])
dq.extendleft([2, 4])
dq.remove(4)
dq.clear()

print(dq)