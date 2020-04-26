import queue

q1 = queue.Queue(maxsize=5)  # maxsize的值要等于大于下面range的值
for i in range(5):
    q1.put(i)
while not q1.empty():
    print('q1:', q1.get())
print('\n')
q2 = queue.LifoQueue(maxsize=5)
for i in range(5):
    q2.put(i)
while not q2.empty():
    print('q2:', q2.get())
