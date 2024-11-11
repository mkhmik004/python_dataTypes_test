def create_squares_of_evens():
    """
    Task:
    - Create a list of squares for all even numbers from 1 to 20 using list comprehension.
    
    Return:
    - The list of squares of even numbers.
    """
    even_squres=[]
    for num in range(1,11):
        if num%2==0:
            even_squres.append(num**2)
        else:
            continue
    return even_squres
print(create_squares_of_evens())



def convert_to_dict(students):
    """
    Task:
    - Convert the list of student tuples into a dictionary where the name is the key and the grade is the value.
    
    Return:
    - The dictionary created from the list of students.
    """
    dict={}
    for student in students:
        dict[student[0]]=student[1]
    return dict


def access_value_x(nested):
    """
    Task:
    - Access the value of 'x' from the nested dictionary `nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}`.
    
    Return:
    - The value of 'x' (which is 10).
    """
    return nested['c']['x']


def append_to_list_in_dict(nested):
    """
    Task:
    - Append the value 6 to the list under key 'a' in the nested dictionary `nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}`.
    
    Return:
    - The updated dictionary.
    """
    nested['a'].append(6)
    return nested
print(append_to_list_in_dict({'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}))


def convert_tuple_to_list_and_append(nested):
    """
    Task:
    - Convert the tuple under key 'b' in the nested dictionary into a list and add the value 6 at the end.
    
    Return:
    - The updated dictionary.
    """
    nested['b']=(list(nested['b']))
    nested['b'].append(6)
    
  
    return nested
print(convert_tuple_to_list_and_append({'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}))
