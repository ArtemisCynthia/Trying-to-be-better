
"""节点类"""
class Node(object):
    def __init__(self, elem) -> None:
        self.elem = elem
        self.next = None

"""创建单链表"""
class SingleLinkList(object):
    def __init__(self, node = None) -> None:
        self.__head = node
    """链表是否为空"""
    def is_empty(self):
        return self.__head == None
    """链表长度"""
    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    """遍历整个链表"""
    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem, end = ' ')
            cur = cur.next
        print('\n')
    """链表头部添加元素"""
    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node
    """链表尾部添加元素"""
    def append (self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    """指定位置添加元素"""
    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            per = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                per = per.next
            node = Node(item)
            node.next = per.next
            per.next = node
    """删除结点"""
    def remove(self, item):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                    break
            else:
                pre = cur
                cur = cur.next
    """查找结点是否存在"""
    def search(self, item):
        cur = self.__head
        while not cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(3)
    ll.add(999)
    ll.insert(-3, 110)
    ll.insert(99, 111)
    print(ll.is_empty())
    print(ll.length())
    ll.travel()
    ll.remove(111)
    ll.travel() 