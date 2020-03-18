def makeGroceryList(groceries):
    """
    > makeGroceryList(['toilet paper', 'hand sanitizer', 'salt'])
    'toilet paper and hand sanitizer and salt'

    """
    result = ''
    firstGrocery = True
    for grocery in groceries:
        if not firstGrocery:
            result += ' and '
        result += grocery
        firstGrocery = False
    return result

def makeGroceryListVersion2(groceries):
    """
    > makeGroceryListVersion2(['toilet paper', 'hand sanitizer', 'salt'])
    'toilet paper and hand sanitizer and salt'

    """
    return ' and '.join(groceries)


def isMultipleWords(s):
    return ' ' in s

def makeTodaysGroceryList(groceries, predicate):
    """
    predicate is a function that takes a string as an argument and returns
    True if that string is on today's grocery list.
      
    > makeTodaysGroceryList(['toilet paper', 'hand sanitizer', 'salt'], isMultipleWords)
    'toilet paper and hand sanitizer'
      
    """
    todays = []
    for grocery in groceries:
        if predicate(grocery):
            todays.append(grocery)
    return ' and '.join(todays)  