def tree_node(l, lbl, r):
    return [l, lbl, r]


def leaf(lbl):
    return tree_node(None, lbl, None)


def label(node):
    return node[1]


def left(node):
    return node[0]


def right(node):
    return node[2]


def set_label(node, new_label):
    node[1] = new_label


def set_left(node, left_node):
    node[0] = left_node


def set_right(node, right_node):
    node[2] = right_node


def is_leaf(node):
    return (left(node) == None) and (right(node) == None)


def example_expression_tree():
    eight = leaf(8)
    five = leaf(5)
    negative_two = leaf(-2)
    two = leaf(2)
    max_node = tree_node(negative_two, "max", two)
    min_node = tree_node(eight, "min", five)
    root = tree_node(min_node, "pow", max_node)
    return root


def viz(root):
    """ If you'd like, you can try to understand this function now. """
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
    print(viz_helper(root, 0).strip())


def evaluate(etree):
    if is_leaf(etree):
        return label(etree)
    else:
        func = eval(label(etree))
        left_value = evaluate(left(etree))
        right_value = evaluate(right(etree))
        return func(left_value, right_value)


def prefix_notation(node):
    """ Fill this in! """