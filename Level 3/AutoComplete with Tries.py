## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.head=Trie()

    def insert(self, char):
        self.head.insert(char)
        ## Add a child node in this Trie

## The Trie itself containing the root node and insert/find functions

class Trie:
    head=None

    def __init__(self):
        self.hmap={}
        self.isEnd=False


    def insert(self, word: str) -> None:
        newNode=Trie()

        if(self.head==None):
            self.head=Trie()
            self.head.hmap[word[0]]=newNode

        head_cpy=self.head
        for i in word:
            if(i in head_cpy.hmap):
                head_cpy=head_cpy.hmap[i]
            else:
                newNode=Trie()
                head_cpy.hmap[i]=newNode
                head_cpy=newNode
        #print("inserted",word)
        head_cpy.isEnd=True


    def search(self, word: str) -> bool:
        if(self.head==None):
            return False
        head_cpy=self.head
        for i in word:
            if(i in head_cpy.hmap):
                head_cpy=head_cpy.hmap[i]
            else:
                return False
        if(head_cpy.isEnd==True):
            return True
        else:
            return False


    def find(self, prefix):
        if(self.head==None):
            return False
        head_cpy=self.head
        for i in prefix:
            if(i in head_cpy.hmap):
                head_cpy=head_cpy.hmap[i]
            else:
                return None
        return head_cpy




class TrieNode:
    suff_list=[]
    def __init__(self, trie_head):
        self.head=trie_head

    def insert(self, char):
        self.head.insert(char)

    def suffixes(self, suffix = ''):
        self.suff_list=[]
        new_head=self.head.find(suffix)
        if(new_head):
            self.suff_list=[]
            self.findSuffixes(new_head,"")
        return self.suff_list

    def findSuffixes(self, head_cpy, str):

        if(head_cpy==None):
            return "";
        elif(head_cpy.isEnd):
            self.suff_list.append(str)

        for i,j in head_cpy.hmap.items():
            self.findSuffixes(j, str+i)
        return self.suff_list

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(TrieNode(MyTrie).suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');
