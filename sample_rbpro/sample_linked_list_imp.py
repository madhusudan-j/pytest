
"""
doc this is sample module
"""
import sample_linked_list

class DataStructures:
    """
    This class will show data structures with inbuilt methods with example
    """
    # constructor method 
    def __init__(self, arg1=111, arg2=2222, arg3=33333):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def list_example(self):
        print("###################",self.arg1)
        # list data example
        my_list = [1, 2, 3, 'example', 3.132] #creating list with data
        print(my_list)
        # adding elements
        my_list.append([555, 12]) #add as a single element
        print(my_list)
        my_list.extend([234, 'more_example']) #add as different elements
        print(my_list)
        my_list.insert(1, 'insert_example') #add element i
        print(my_list)
        # deleting elements
        del my_list[5] #delete element at index 5
        print(my_list)
        my_list.remove('example') #remove element with value
        print(my_list)
        a = my_list.pop(1) #pop element from list
        print('Popped Element: ', a, ' List remaining: ', my_list)
        my_list.clear() #empty the list
        print(my_list)
        my_list = [1, 2, 3, 'example', 3.132, 10, 30]
        # accessing elements 
        for element in my_list: #access elements one by one
            print(element)
        print(my_list) #access all elements
        print(my_list[3]) #access index 3 element
        print(my_list[0:2]) #access elements from 0 to 1 and exclude 2
        print(my_list[::-1]) #access elements in reverse
        my_list = [1, 2, 3, 10, 30, 10]
        print(len(my_list)) #find length of list
        print(my_list.index(10)) #find index of element that occurs first
        print(my_list.count(10)) #find count of the element
        print(sorted(my_list)) #print sorted list but not change original
        my_list.sort(reverse=True) #sort original list
        print(my_list)

    def dict_example(self):
        my_dict = {'First': 'Python', 'Second': 'Java'}
        print(my_dict)
        my_dict['Second'] = 'C++' #changing element
        print(my_dict)
        my_dict['Third'] = 'Ruby' #adding key-value pair
        print(my_dict)
        a = my_dict.pop('Third') #pop element
        print('Value:', a)
        print('Dictionary:', my_dict)
        b = my_dict.popitem() #pop the key-value pair
        print('Key, value pair:', b)
        print('Dictionary', my_dict)
        my_dict.clear() #empty dictionary
        print('cleared', my_dict)
        my_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
        print(my_dict.keys()) #get keys
        print(my_dict.values()) #get values
        print(my_dict.items()) #get key-value pairs
        print(my_dict.get('First'))

    def tuple_example(self):
        my_tuple = (1, 2, 3, 'Kannada') #access elements
        for x in my_tuple:
            print(x)
        print(my_tuple)
        print(my_tuple[0])
        print(my_tuple[:])
        print(my_tuple[3][4])
        my_tuple = (1, 2, 3, ['hindi', 'python'])
        my_tuple[3][0] = 'english'
        print(my_tuple)
        print(my_tuple.count(2))
        print(my_tuple.index(['english', 'python']))

    def sets_example(self):
        my_set = {1, 2, 3,3, 4}
        print(my_set)
        my_set_2 = {3, 4, 5, 6}
        print(my_set.union(my_set_2), '----------', my_set | my_set_2)
        print(my_set.intersection(my_set_2), '----------', my_set & my_set_2)
        print(my_set.difference(my_set_2), '----------', my_set - my_set_2)
        print(my_set.symmetric_difference(my_set_2), '----------', my_set ^ my_set_2)
        my_set.clear()
        print(my_set)

def main():
    data_stuct_obj = DataStructures(9999999999)
    data_stuct_obj.sets_example()
if __name__=='__main__':
    # main()
    linked_list.main()
