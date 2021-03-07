def tree_node(l, lbl, r):
    return [l, lbl, r]


def label(node):
    return node[1]


def left(node):
    return node[0]


def right(node):
    return node[2]


def set_left(node, left_node):
    node[0] = left_node


def set_right(node, right_node):
    node[2] = right_node


def leaf(lbl):
    return tree_node(None, lbl, None)


def is_leaf(node):
    return (left(node) == None) and (right(node) == None)


def favorites():
    leaf8 = leaf(8)
    leaf12407 = leaf(12407)
    leaf51897 = leaf(51897)
    node1729 = tree_node(leaf8, 1729, leaf12407)
    root = tree_node(node1729, 34969, leaf51897)
    return root


def viz(node):
    """
    IMPORTANT: You don't have to understand this function just yet.

    It's provided here to allow easier visualization of a tree, but
    uses a programming concept called "recursion" that
    we'll introduce later in the course.

    """
    def viz_helper(node, indent):
        result = ""
        if node == None:
            return result
        result = result + str(label(node)) + "\n"
        if left(node) != None:
            left_str = viz_helper(left(node), indent+2)
            result = result + (" " * indent) + "--L--> " + left_str
        if right(node) != None:
            right_str = viz_helper(right(node), indent+2)
            result = result + (" " * indent) + "--R--> " + right_str
        return result
    print(viz_helper(node, 0).strip())


def insertion_point(root, lbl):
    node = root
    done = False
    while not done:
        if label(node) > lbl and left(node) != None:
            node = left(node)
        elif label(node) < lbl and right(node) != None:
            node = right(node)
        else:
            done = True
    return node


def is_favorite(root, lbl):
    """ Fill in with your solution. """


def insert(root, lbl):
    """ Fill in with your solution. """


