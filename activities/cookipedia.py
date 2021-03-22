class TreeNode:

    def __init__(self, l, lbl, r):
        self.lt = l
        self.labl = lbl
        self.rt = r

    def __contains__(self, lbl):
        """ Fill this in! """

    def __eq__(self, node):
        """ Fill this in! """

    def label(self):
        return self.labl

    def left(self):
        return self.lt

    def right(self):
        return self.rt

    def set_label(self, new_label):
        self.labl = new_label

    def set_left(self, new_left_child):
        self.lt = new_left_child

    def set_right(self, new_right_child):
        self.rt = new_right_child

    def size(self):
        if self.left() == None and self.right() == None:
            return 1
        else:
            return 1 + self.lt.size() + self.rt.size()

    def __len__(self):
        return self.size()

    def __str__(self):
        def viz_helper(node, indent):
            result = ""
            if node == None:
                return result
            result = result + str(node.label()) + "\n"
            if node.left() != None:
                left_str = viz_helper(node.left(), indent+2)
                result = result + (" " * indent) + "--L--> " + left_str
            if node.right() != None:
                right_str = viz_helper(node.right(), indent+2)
                result = result + (" " * indent) + "--R--> " + right_str
            return result
        return viz_helper(self, 0).strip()

def cookie_taxonomy():
    choco_chip = TreeNode(None, "chocolate chip", None)
    rainbow_chip = TreeNode(None, "rainbow chip", None)
    ginger_snap = TreeNode(None, "ginger snap", None)
    speculoos = TreeNode(None, "speculoos", None)
    chip = TreeNode(choco_chip, "chip cookies", rainbow_chip)
    spice = TreeNode(ginger_snap, "spice cookies", speculoos)
    root = TreeNode(chip, "cookies", spice)
    return root

