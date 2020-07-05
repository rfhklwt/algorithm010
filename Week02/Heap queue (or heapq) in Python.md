# Week02总结
## Heap queue (or heapq) in Python
heap数据结构主要用于表示priority queue。 在Python中，可以使用**heapq**模块使用。 在python中此数据结构的属性是每次弹出最小的堆元素（**最小堆**）。 每当元素被推入或弹出时，堆结构都将保持不变。 heap[0]的元素将会heap里面是最小的。

### 相关操作
- **heapify(iterable)**: 将可迭代对象转换为堆数据结构。 即按堆顺序。
- **heappush(heap, ele): 将参数中的ele插入堆中。 同时调整顺序，以便维护堆结构。
- **heappop(heap)**: 从堆中删除并返回**最小的元素**。 同时调整顺序，以便维护堆结构。
#### 代码示例如下：
```Python
# Python code to demonstrate working of
# heapify(), heappush() and heappop()

# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print ("The created heap is : ",end="")
print (list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)

# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(li))

# using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))
```
#### 输出
```
The created heap is : [1, 3, 9, 7, 5]
The modified heap after push is : [1, 3, 4, 7, 5, 9]
The popped and smallest element is : 1
```
- **heappushpop(heap, ele)**: 先push后pop
- **heapreplace(heap, ele)**: 先pop后push。
#### 示例代码：
```Python
# Python code to demonstrate working of
# heappushpop() and heapreplce()

# importing "heapq" to implement heap queue
import heapq

# initializing list 1
li1 = [5, 7, 9, 4, 3]

# initializing list 2
li2 = [5, 7, 9, 4, 3]

# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)

# using heappushpop() to push and pop items simultaneously
# pops 2
print ("The popped item using heappushpop() is : ",end="")
print (heapq.heappushpop(li1, 2))

# using heapreplace() to push and pop items simultaneously
# pops 3
print ("The popped item using heapreplace() is : ",end="")
print (heapq.heapreplace(li2, 2))
```
#### 输出
```
The popped item using heappushpop() is : 2
The popped item using heapreplace() is : 3
```
- **nlargest(k, iterable, key = fun)**: 返回迭代器里前k大的数，同时满足key。
- **nsmallest(k, iterable, key = fun)**: 返回迭代器里前k小的数，同时满足key。
#### 示例代码：
```Python
# Python code to demonstrate working of
# nlargest() and nsmallest()

# importing "heapq" to implement heap queue
import heapq

# initializing list
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

# using heapify() to convert list into heap
heapq.heapify(li1)

# using nlargest to print 3 largest numbers
# prints 10, 9 and 8
print("The 3 largest numbers in list are : ",end="")
print(heapq.nlargest(3, li1))

# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ",end="")
print(heapq.nsmallest(3, li1))
```
#### 输出
```
The 3 largest numbers in list are : [10, 9, 8]
The 3 smallest numbers in list are : [1, 3, 4]
```
#### 参考链接：
https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

