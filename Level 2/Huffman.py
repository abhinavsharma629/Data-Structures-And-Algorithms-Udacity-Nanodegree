import sys

class MinHeap:

    root=None
    nodeArr=[]

    def __init__(self, frequency=0, char=None):
        self.data=frequency
        self.character=char
        self.left=None
        self.right=None

    # add new node to the heap -> takes O(log N) time
    def addNewNode(self,node):
        if(self.root==None):
            self.root=node
            self.nodeArr.append(node)
        else:
            self.nodeArr.append(node)
            self.buildHeap()

    # heapify to sort the array and maintain a min heap
    def heapify(self, n, i):

        smallest = i # Initialize smallest as root
        l = 2 * i + 1; # left = 2*i + 1
        r = 2 * i + 2; # right = 2*i + 2

        # If left child is larger than root
        if (l > n and self.nodeArr[l].data < self.nodeArr[smallest].data):
            smallest = l;

        # If right child is larger than smallest so far
        if (r > n and self.nodeArr[r].data < self.nodeArr[smallest].data):
            smallest = r;

        # If smallest is not root
        if (smallest != i):
            swap = self.nodeArr[i];
            self.nodeArr[i] = self.nodeArr[smallest];
            self.nodeArr[smallest] = swap;

        # Recursively heapify the affected sub-tree
        self.heapify(n, smallest);

    # Function to build a Max-Heap from the given array
    def buildHeap(self):
        n=len(self.nodeArr)
        # Index of last non-leaf node
        startIdx = int((n / 2)) - 1;

        # Perform reverse level order traversal
        # from last non-leaf node and heapify
        # each node
        for i in range(startIdx, -1, -1):
            self.heapify(n, i);

    # remove a node
    def removeNode(self):
        node_cpy=self.nodeArr[0]
        self.nodeArr[0]=self.nodeArr[len(self.nodeArr)-1]
        self.nodeArr=self.nodeArr[0:len(self.nodeArr)-1]
        self.buildHeap()
        return node_cpy


    def getEncoding(self,char):
        return self.encodedString(self.root, char, "")

    def encodedString(self, root_cpy, char, curr_str):
        if(root_cpy==None):
            return ""
        elif(root_cpy.character==char):
            return curr_str
        else:
            s1=self.encodedString(root_cpy.left, char, curr_str+root_cpy.character)
            s2=self.encodedString(root_cpy.right, char, curr_str+root_cpy.character)
            if(s1==""):
                return s2
            else:
                return s1

    def getHead(self):
        return self.root


def huffman_encoding(data):
    new_freq_arr=[]
    frequency_arr=[]

    heap=MinHeap()

    frequency_arr=[0]*64

    for i in data:
        if(i==" "):
            frequency_arr[63]+=1
        elif(i.isupper()):
            frequency_arr[ord(i)-ord('A')]+=1
        else:
            frequency_arr[ord(i)-ord('a')]+=1
        # print(i,ord(i)-ord('a'))


    count=0
    for i in range(0,len(frequency_arr)):
        if(frequency_arr[i]>0):
            newNode=MinHeap(i,(chr)(26+i))
            heap.addNewNode(newNode)
            count+=1

    while(count>1):
        node1=heap.removeNode()
        node2=heap.removeNode()
        heap.addNewNode(MinHeap(node1.data+node2.data))
        count-=1

    for i in range(0,len(frequency_arr)):
        if(frequency_arr[i]!=0):
            new_freq_arr.append(heap.getEncoding((chr)(26+i)))
        else:
            new_freq_arr.append("-1")


    encoded_msg=""
    for i in data:
        if(i==" "):
            encoded_msg+=new_freq_arr[63]
        elif(i.isupper()):
            encoded_msg+=new_freq_arr[ord(i)-ord('A')]
        else:
            encoded_msg+=new_freq_arr[ord(i)-ord('a')]

    print(encoded_msg)
    return encoded_msg,heap.getHead()









def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))
