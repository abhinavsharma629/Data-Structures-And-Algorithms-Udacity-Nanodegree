import random
import string
import secrets

# Active Directory Class
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []


    # add user to group
    def add_user(self,user):
        self.users.append(user)

    # add sub group to group
    def add_group(self, group):
        self.groups.append(group)

    # get all groups of current group
    def get_groups(self):
        return self.groups

    # get all users of current group
    def get_users(self):
        return self.users

    # get name of user
    def get_name(self):
        return self.name



# check if user is a part of the current group / subgroups of this current group
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
        user(str): user name/id
        group(class:Group): group to check user membership against
    """
    if(user==None or group==None):
        return False

    if user in group.users:
        return True
    else: # using BFS instead of DFS to avoid any infinite space traversal and find if the element lies more efficiently than DFS
        userFound=False
        queue=[]
        queue.append(group)
        size=1
        while(len(queue)!=0):
            for i in range(0,size):
                ele=queue.pop()
                if(user in ele.users):
                    userFound=True
                    break
                else:
                    for j in ele.groups:
                        queue.append(j)
            if(userFound):
                break
            size=len(queue)
        if(userFound):
            return True
        else:
            return False
    # user not found
    return False










#-----------------------------------HELPERS-----------------------------------------------------------



def basic_test_helper():
    # main group 1
    parent = Group("parent") # main_group1
    child = Group("child")   # sub_group1 -> main_group1
    child1 = Group("child1")   # sub_group2 -> main_group1
    sub_child = Group("subchild")   # sub_sub_group1 -> sub_group1
    sub_sub_child = Group("sub_sub_child")   # sub_sub_sub_group1 -> sub_sub_group1


    # main group 2
    parent1 = Group("parent1") # main_group1
    child101 = Group("child101")   # sub_group1 -> main_group1
    child102 = Group("child102")   # sub_group1 -> main_group1
    sub_child101 = Group("subchild101")   # sub_sub_group1 -> sub_group1
    sub_sub_child101 = Group("sub_sub_child101")   # sub_sub_sub_group1 -> sub_sub_group1


    sub_sub_child_child101="i am child of sub_sub_child"
    p_child101 = "i am child of parent"
    p1_child101 = "i am child of parent1"


    parent.add_group(child)
    parent.add_user(p_child101)
    child.add_group(child1)
    child1.add_group(sub_child)
    sub_child.add_group(sub_sub_child)
    sub_sub_child.add_user(sub_sub_child_child101)


    parent1.add_group(child101)
    parent1.add_user(p1_child101)
    parent1.add_group(child102)
    child101.add_group(sub_child101)
    sub_child101.add_group(sub_sub_child101)


    print ("Pass" if  (False == is_user_in_group(None, None)) else "Fail")
    print ("Pass" if  (False == is_user_in_group("xyz", None)) else "Fail")
    print ("Pass" if  (False == is_user_in_group(None, Group("test1"))) else "Fail")
    print ("Pass" if  (True == is_user_in_group(sub_sub_child_child101, parent)) else "Fail")
    print ("Pass" if  (True == is_user_in_group(p_child101, parent)) else "Fail")
    print ("Pass" if  (False == is_user_in_group(p1_child101, parent)) else "Fail")


    # # Test 1 when no groups and no users given -> False
    # print(is_user_in_group(None, None)) # invalid input

    # # Test 2 when no groups and no users given  -> False
    # print(is_user_in_group("xyz", None)) # invalid input

    # # Test 3 when no groups and no users given  -> False
    # print(is_user_in_group(None, Group("test1"))) # invalid input

    # # Test 4 when user exists in last sub_group and main parent is given    -> True
    # print(is_user_in_group(sub_sub_child_child101, parent))

    # # Test 5 when user exists in main parent and main parent is given   -> True
    # print(is_user_in_group(p_child101, parent))

    # # Test 6 when user exists in diff main parent and main parent is given  -> False
    # print(is_user_in_group(p1_child101, parent))





#------------------------ ADVANCED HELPERS FOR RANDOM CHECKUPS------------------------------------------

"Main helper to add users and groups logic"
active_groups_list=[]
active_groups_users=[]

def test_helper_for_adding_users_and_groups(user=None, group=None,group1=None):
    if(user==None and group==None):
        return "Must give atleast one param"
    else:
        if(len(active_groups_list)==0):
            if(group==None):
                return "Must add atleast one parent first"

        if(group and user):
            group.add_user(user)
            active_groups_users.append(user)
            return "Added User and Group"
        elif(group and group1):
            #create_group=Group(groupName)
            group.add_group(group1)
            active_groups_list.append(group)
            active_groups_list.append(group1)
            return "Added Group to Group"
        elif(group):
            #create_group=Group(groupName)
            active_groups_list.append(group)
            return "Added Group"
        else:
            return "Give a group to add user to"


# check for random users in random groups
def test_helper_for_checking_if_present():

    for i in range(0,100):

        group_ind=random.randint(0,len(active_groups_list)-1)
        user_ind=random.randint(0,len(active_groups_users)-1)

        if is_user_in_group(active_groups_users[user_ind],active_groups_list[group_ind]):
            print("User {} FOUND in group {}".format(active_groups_users[user_ind],active_groups_list[group_ind]))
        else:
            print("User {} not found in group {}".format(active_groups_users[user_ind],active_groups_list[group_ind]))

        print("Group members are: ")
        print("Sub Groups",active_groups_list[group_ind].groups)
        print("Sub Users",active_groups_list[group_ind].users)
        print("\n")



# Add random groups and subgroups and users
def runner():
    for i in range(0,100):
        if(i%2==0):
            # add user to group
            if(len(active_groups_list)>1):
                user = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(7))
                print(test_helper_for_adding_users_and_groups(user, active_groups_list[random.randint(0,len(active_groups_list)-1)]))

        elif(i%3==0):
            # add group to group
            print(test_helper_for_adding_users_and_groups(None,Group(''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(10))),Group(''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(10)))))
        else:
            # add group
            print(test_helper_for_adding_users_and_groups(None,Group(''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(10))),None))



if __name__ == '__main__':
    basic_test_helper()

    # runner()
    # print("Done adding")
    # test_helper_for_checking_if_present()



'''

 ------------------
|   u1, u2,       |
|    ---          |
|   | g |         |
|    ---          |
|_________________|

'''
