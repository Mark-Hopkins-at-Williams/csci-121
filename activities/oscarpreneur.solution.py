phonebook = {'bert': ['555-1234', '567-1234'],
             'ernie': ['942-2345']}


def add_value(dictionary, key, new_value):
    """
    This should modify the dictionary so that the
    key is associated with its previous values
    AS WELL AS the new value.

    """
    dictionary[key] = dictionary[key] + [new_value]


