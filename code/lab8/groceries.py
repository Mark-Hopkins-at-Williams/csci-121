def makeGroceryList(groceries):
    """
    > makeGroceryList(['toilet paper', 'hand sanitizer', 'salt'])
    'toilet paper and hand sanitizer and salt'
      
    """
    raise NotImplementedError('fill this in!')

def isMultipleWords(s):
    return ' ' in s

def makeTodaysGroceryList(groceries, predicate):
    """
    predicate is a function that takes a string as an argument and returns
    True if that string is on today's grocery list.
  
    > makeTodaysGroceryList(['toilet paper', 'hand sanitizer', 'salt'], isMultipleWords)
    'toilet paper and hand sanitizer'
  
    """
    raise NotImplementedError('fill this in!')
  