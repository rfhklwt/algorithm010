# week01总结
## Queue in Python
**Queue**：是一种**先进先出**的数据结构
#### 相关操作
```
Enqueue：往queue加入一个item -> O(1)
Dequeue：往queue移除一个item -> O(1)
Front：获取queue最左边的item -> O(1)
Rear：获取queue最右边的一个item -> O(1)
```
#### 实现方式（3种）：
- list
- collections.deque
- queue.Queue

1. 采用list的话，一些等效操作如下：
```Python
queue = []
queue.append('a')
queue.pop(0) # 时间复杂度：O(n)
```
需要注意的是，用list来实现queue不太合适，因为在开始处插入或删除元素需要将所有其他元素移位一个，需要O(n)时间。另外如果list空了后再进行pop操作会抛出异常，因此不建议采用list来实现。

2. 采用collections模块中的deque类（实际上这是双端队列），是比较常用的类。因此从容器两端进行插入和读取都只仅仅O(1)的时间复杂度。一些等效操作如下：
```Python
queue = collections.deque()
queue.append('a')       # 从右端加入 -> O(1)
queue.appendleft('a')   # 从左端加入 -> O(1)
queue.pop()             # 从右端弹出 -> O(1)
queue.popleft()         # 从左端弹出 -> O(1)
```
3. 采用Python的内置模块queue，模块各种功能如下：
```
- maxsize – Number of items allowed in the queue.
- empty() – Return True if the queue is empty, False otherwise.
- full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
- get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
- get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
- put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
- put_nowait(item) – Put an item into the queue without blocking.
qsize() – Return the number of items in the queue. If no free slot is immediately available, raise QueueFull.
```
## Priority Queue in Python
Priority Queue是普通queue的一个扩展，它拥有如下特性：

1. An element with high priority is dequeued before an element with low priority.
2. If two elements have the same priority, they are served according to their order in the queue.

跟queue的对比如下：
1. 在Queue中，最早的元素首先被dequeued。 而在优先级队列中，基于最高优先级的元素将dequeued
2. 当元素从priority queue中弹出时，将以递增顺序或递减顺序获得结果。 同时，当从queue中弹出元素时，将在结果中获得FIFO（先入先出）数据顺序
#### 实现方式:
 - 采用queue来实现
```Python
# A simple implementation of Priority Queue using Queue.
class PriorityQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	# for checking if the queue is empty
	def isEmpty(self):
		return len(self.queue) == 0

	# for inserting an element in the queue
	def insert(self, data):
		self.queue.append(data)

	# for popping an element based on Priority
	def delete(self):
		try:
			max = 0
			for i in range(len(self.queue)):
				if self.queue[i] > self.queue[max]:
					max = i
			item = self.queue[max]
			del self.queue[max]
			return item
		except IndexError:
			print()
			exit()

if __name__ == '__main__':
	myQueue = PriorityQueue()
	myQueue.insert(12)
	myQueue.insert(1)
	myQueue.insert(14)
	myQueue.insert(7)
	print(myQueue)
	while not myQueue.isEmpty():
		print(myQueue.delete())
```
```
12 1 14 7
14
12
7
1
```
值得注意的是在上述代码中删除操作的时间复杂度为O(n)

 - 另一种更好的实现方式为使用Binary Heap，在Python中提供了heapq模块。若采用heapq数据结构，则插入和删除的时间复杂度将变为O(log(n))。

### 几类数据结构的时间复杂度总结(平均)
|                    | Access | Search | Insertion | Deletion |
|:------------------:|:------:|:------:|:---------:|:--------:|
| Array              |  O(1)  |  O(n)  |    O(n)   |   O(n)   |
| Stack              |  O(n)  |  O(n)  |    O(1)   |   O(1)   |
| Queue              |  O(n)  |  O(n)  |    O(1)   |   O(1)   |
| Singly-Linked List |  O(n)  |  O(n)  |    O(1)   |   O(1)   |
| Dpubly-Linked List |  O(n)  |  O(n)  |    O(1)   |   O(1)   |
| Skip List          |O(log(n))|O(log(n))|O(log(n))|O(log(n)) |

#### 参考链接：
1. https://www.geeksforgeeks.org/queue-in-python/
2. https://www.geeksforgeeks.org/priority-queue-in-python/