class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


# Following the condition that Union of A and B  => A + Only(B) i.e no intersection twice
def union(llist1, llist2):
   # traversing through llist1

    if(llist1.head==None and llist2.head==None):
        return LinkedList()
    elif(llist1.head==None):
        return llist2
    elif(llist2.head==None):
        return llist1

    else:
        hmap={}
        llist3=llist1 # Linked List 1 full

        # for duplicacy and non intersection check
        head_ll1=llist1.head
        while(head_ll1.next!=None):
            if(not head_ll1.value in hmap):
                hmap[head_ll1.value]=1

            head_ll1=head_ll1.next



        if(not head_ll1.value in hmap):
            hmap[head_ll1.value]=1

        # union to ll3
        head_ll2=llist2.head
        while(head_ll2!=None):
            if(not head_ll2.value in hmap):
                hmap[head_ll2.value]=1
                llist3.append(Node(head_ll2.value))

            head_ll2=head_ll2.next

        return llist3



# Following the condition that Intersection of A and B  => Only(A) + Only(B) i.e no duplicates if present
def intersection(llist1, llist2):
    # Your Solution Here
    llist3=LinkedList()

    if(llist1.head==None or llist2.head==None):
        return llist3
    hmap={}
    head_ll1=llist1.head
    while(head_ll1.next!=None):
        if(not head_ll1.value in hmap):
            hmap[head_ll1.value]=1
        head_ll1=head_ll1.next

    head_ll2=llist2.head
    if(not head_ll1.value in hmap):
        hmap[head_ll1.value]=1

    #print(hmap)

    head_ll2=llist2.head
    while(head_ll2!=None):
        if(head_ll2.value in hmap):
            llist3.append(head_ll2.value)

        head_ll2=head_ll2.next

    return llist3



# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))



# Test case 3

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))


# Test case 4

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [6,32,4,9,6,1,11,21,1]
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))


# Test case 5

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
