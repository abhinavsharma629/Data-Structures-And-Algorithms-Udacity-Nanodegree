# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        self.hmap={}
        self.handler=handler
        # Initialize the trie with an root node and a handler, this is the root path or home page node

    def insert(self, head, path, handler):
        head_cpy=head

        for i in path:
            if(i in head_cpy.hmap):
                head_cpy=head_cpy.hmap[i]
            else:
                newRoute=RouteTrie()
                head_cpy.hmap[i]=newRoute
                head_cpy=newRoute

        head_cpy.handler=handler
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

    def find(self, head, prefixPath):
        if(head==None):
            return None

        head_cpy=head
        for i in prefixPath:
            if(i in head_cpy.hmap):
                head_cpy=head_cpy.hmap[i]
            else:
                return None
        if(head_cpy.handler!=None):
            return head_cpy.handler
        else:
            return None
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, rootHandler):
        self.base=RouteTrie(rootHandler)
        self.rootHandler=rootHandler
        # Initialize the node with children as before, plus a handler

    def insert(self, path, handler):
        return self.base.insert(self.base, path, handler)
        # Insert the node as before

    def find(self, path):
        return self.base.find(self.base, path)



# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, rootHanlder, handler404):
        self.isPathFoundHandler=handler404
        self.base=RouteTrieNode(rootHanlder)
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!

    def add_handler(self, path, handler):
        isFound=self.lookup(path)
        path_arr=self.split_path(path)
        if(isFound):
            self.base.insert(path_arr, handler)
        else:
            return self.isPathFoundHandler
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

    def lookup(self, path):
        path_arr=self.split_path(path)
        isFound=self.base.find(path_arr)
        if(isFound):
            return isFound
        else:
            return self.isPathFoundHandler
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler


    def split_path(self, path):
        path=path.split("/")
        c=len(path)
        for i in path[::-1]:
            if(i==""):
                c-=1
            else:
                break
        #print(path[0:c])
        return path[0:c]
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here





# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/about/me", "me handler")  # add a route
router.add_handler("/home/checkin", "checkin handler")  # add a route

# some lookups with the expected output
print("Pass" if "root handler" == router.lookup("/") else "Fail") # should print 'root handler'
print("Pass" if "not found handler" == router.lookup("/home") else "Fail") # should print 'not found handler' or None if you did not implement one
print("Pass" if "about handler" == router.lookup("/home/about") else "Fail") # should print 'about handler'
print("Pass" if "about handler" == router.lookup("/home/about/") else "Fail") # should print 'about handler' or None if you did not handle trailing slashes
print("Pass" if "me handler" == router.lookup("/home/about/me") else "Fail") # should print 'me handler' or None if you did not implement one
print("Pass" if "me handler" == router.lookup("/home/about/me/") else "Fail") # should print 'me handler' or None if you did not implement one
print("Pass" if "not found handler" == router.lookup("/home/about/me/my") else "Fail") # should print 'not found handler' or None if you did not implement one
print("Pass" if "checkin handler" == router.lookup("/home/checkin") else "Fail") # should print 'checkin handler' or None if you did not implement one
print("Pass" if "not found handler" == router.lookup("/home/checkin/my") else "Fail") # should print 'not found handler' or None if you did not implement one
