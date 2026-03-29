class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
    

        self.head.next = self.tail
        self.tail.prev = self.head

    def removenode(self, oldnode):
        prev_node=oldnode.prev #left node
        next_node=oldnode.next #right node

        prev_node.next=next_node
        next_node.prev=prev_node
      

      #  self.printList(self.head)
      


    def insertnode(self, newnode):
        

        firstnode=self.head.next
        self.head.next=newnode
        newnode.next=firstnode
        newnode.prev=self.head
        firstnode.prev=newnode


        #self.printList(self.head)
          

    

    def get(self, key: int):
       

        if key in self.cache:
            self.removenode(self.cache[key])
            self.insertnode(self.cache[key])
            return self.cache[key].val
        return -1

    def printList(self, head):
        curr = head
        while curr.next is not None:
            print(curr.val, end="->")
            curr = curr.next
        print(0)

    def put(self, key, val) -> None:
        
        newnode = Node(key, val)

        if key in self.cache:
            oldnode=self.cache[key]
            self.removenode(oldnode) #remve from linkedlist
            self.cache[key] = newnode # add in dict
            self.insertnode(newnode) #add in linked list

        if key not in self.cache:

            self.cache[key] = newnode # add in dict
            self.insertnode(newnode) #add in linked list

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.removenode(lru)
            del self.cache[lru.key]

    
    
    

    # Your LRUCache object will be instantiated and called as such:


lRUCache =  LRUCache(2);
lRUCache.put(1, 1);   #// cache is {1=1}
lRUCache.put(2, 2);  # // cache is {1=1, 2=2}
lRUCache.get(1);     # // return 1
lRUCache.put(3, 3);  # // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    # // returns -1 (not found)
lRUCache.put(4, 4);  #// LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);     #// return -1 (not found)
lRUCache.get(3);    # // return 3
lRUCache.get(4);     #// return 4 

