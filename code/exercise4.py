# WRITE YOUR CODE HERE
def is_nested(dictionary):
    for value in dictionary.values():
        if isinstance(value, (list, tuple, dict)):
            return True
    return False

# test code below

