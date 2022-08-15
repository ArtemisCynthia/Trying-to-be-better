class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None       # 初始设置下一节点为空
class SingleLinkList(object):
    def __init__(self, node=None): 
 #使用一个默认参数，传入头结点接收；没有传入时，默认头结点为空
        self.__head = node
    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None
    def length(self):
        cur = self.__head                  # cur游标，用来移动遍历节点
        count = 0                    # count记录数量
        while cur != None:
            count += 1
            cur = cur.next
        return count
    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print("\n")
    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node
    def append(self, item):
        node = Node(item)
        # 由于特殊情况当链表为空时没有next，所以在前面要做个判断
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    def insert(self, pos, item):
        if pos <= 0:    # 如果pos位置在0，当做头插法
            self.add(item)
        elif pos > self.length() - 1:
            # 如果pos位置比原链表长，那么都当做尾插法来做
            self.append(item)
        else:
            per = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                per = per.next
            # 当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = per.next
            per.next = node
    def remove(self, item):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:       # 先判断该节点是否是头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
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