import os

def find_files(suffix, path):
    #Using BFS for all dirs
    fin_list=[]

    '''----main_dir----
          /  \      \
         /    \      \
    Level1  Level 2   Level 3'''

    

    # If given path exists
    if(os.path.exists(path)):

      #If isFile
      if(os.path.isfile(path)):
        
        # if file has same extention as given suffix
        if("."+path.split(".")[1]==suffix):
          return [path]
        else:
          return []
      
      else:

        # Recurrsive approach for all subdirs of the given dir
        for subdir in os.listdir(path):
          fin_list.extend(find_files(suffix, path+"/"+subdir))

        return fin_list
    else:
      return fin_list

    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    #return None




print(find_files(".java", "C:/Users/User/Desktop/DSA NanoDegree"))