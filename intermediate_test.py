def add_to_list(numbers):
    """
    Task:
    - Add the number 6 to the given list `numbers`.
    
    Return:
    - The modified list.
    """
    numbers.append(6)
    return numbers
print(add_to_list([1,2,3,4,5]))

def remove_from_list(numbers):
    """
    Task:
    - Remove the number 3 from the given list `numbers`.
    
    Return:
    - The modified list.
    """
    numbers.remove(3)
    return numbers
print(remove_from_list([1,3,2,45,6,7,8]))


def insert_at_beginning(numbers):
    """
    Task:
    - Insert the number 0 at the beginning of the given list `numbers`.
    
    Return:
    - The modified list.
    """
    numbers.insert(0,0)
    return numbers
print(insert_at_beginning([1,2,3,5,6]))


def reverse_list(numbers):
    """
    Task:
    - Reverse the order of elements in the list `numbers`.
    
    Return:
    - The reversed list.
    """
    return numbers[::-1]
print(reverse_list([1,2,3,4,5,6]))


def create_new_tuple(t):
    """
    Task:
    - Create a new tuple that contains the first two elements of the tuple `t`.
    
    Return:
    - The new tuple with the first two elements.
    """
    return t[0:2]
print(create_new_tuple((1,2,3,4,5)))


def check_if_value_exists(t, value):
    """
    Task:
    - Check if the value 15 exists in the tuple `t`.
    
    Return:
    - True if the value exists, otherwise False.

    """
    if t.count(value)>0:
        return True
    else:
        return False
print(check_if_value_exists((1,2,3,45),2))
def find_intersection(set1, set2):
    """
    Task:
    - Find the intersection of sets `set1` and `set2`.
    
    Return:
    - The intersection of the two sets.
    """
    return set1.intersection(set2)
print(find_intersection({1,2,3,4},{3,4,6,87,6}))


def find_union(set1, set2):
    """
    Task:
    - Find the union of sets `set1` and `set2`.
    
    Return:
    - The union of the two sets.
    """
    return set1.union(set2)
print(find_union({1,2,3,4},{3,4,6,87,6}))

def find_difference(set1, set2):
    """
    Task:
    - Find the difference between set1 and set2 (i.e., set1 - set2).
    
    Return:
    - The difference between the two sets.
    """
    return set1.difference(set2)
print(find_difference({1,2,3,4},{3,4,6,87,6}))

def add_student(student_grades):
    """
    Task:
    - Add a new student 'David' with a grade of 92 to the dictionary `student_grades`.
    
    Return:
    - The updated dictionary with the new student.
    """
    student_grades['David']=92
    return student_grades
print(add_student({}))

def change_bob_grade(student_grades):
    """
    Task:
    - Change Bob’s grade to 95 in the dictionary `student_grades`.
    
    Return:
    - The updated dictionary with Bob’s grade changed.
    """
    student_grades['Bob']=95
    return student_grades
print(change_bob_grade({'Charlie':77}))

def delete_charlie(student_grades):
    """
    Task:
    - Delete 'Charlie' from the dictionary `student_grades`.
    
    Return:
    - The updated dictionary with Charlie removed.
    """
    student_grades.pop('Charlie')
    return student_grades
print(delete_charlie({'Charlie':77}))


def retrieve_alice_grade(student_grades):
    """
    Task:
    - Retrieve the grade of Alice from the dictionary `student_grades`.
    
    Return:
    - Alice's grade.
    """
    return student_grades['Alice']

