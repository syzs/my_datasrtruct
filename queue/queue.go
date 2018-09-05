package queue

/**
	队列的特性较为单一，基本操作即初始化、获取大小、添加元素、移除元素等。最重要的特性就是满足先进先出。
 */

// 定义每个节点Node结构体，照例Value的值类型可以是任意类型，节点的前后指针域指针类型为node
type node struct {
	value interface{}
	prev *node
	next *node
}

// 定义链表结构，定义出头结点和尾节点的指针，同时定义队列大小size
type LinkedQueue struct {
	head *node
	tail *node
	size int
}

// 获取队列大小，只需要获取LinkedQueue中的size大小即可
func (queue *LinkedQueue) Size() int{
	return queue.size
}

// Peek操作只需要获取队列队头的元素即可，不用删除；另外如果head指针域为nil，则需要nil
func (queue *LinkedQueue) Peak() interface{}{
	if queue.head == nil {
		return nil
	}
	return queue.head.value
}

// 添加操作在队列中是比较重要的操作，也要区分队尾节点是否为nil，根据是否为nil，执行不同的连接操作，最后队列的size要加1，为了不浪费内存新增节点的指针变量要置nil：
func (queue *LinkedQueue)Push(value interface{}){
	newNode := &node{value:value, prev:queue.head, next:nil}
	if queue.tail == nil{
		queue.head, queue.tail = newNode,newNode
	}else{
		queue.tail.next = newNode
		queue.tail = newNode
	}
	queue.size++
	newNode = nil
	return
}

// 队列的删除操作也是很简单，无非是节点的断开操作。在此之前，需要判断链表的状态即是否为nil？而后移除的队列最前端的节点，先用一个新的变量节点保存队列前面的节点，进行一系列操作之后，至nil，并将长度减少即可。
func (queue *LinkedQueue)Pop(){
	if queue.head == nil{
		return
	}
	firstNode := queue.head
	queue.head = firstNode.next
	queue.size--
	firstNode.prev = nil
	firstNode.prev = nil
	firstNode = nil
}

