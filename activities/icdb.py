from icdbtree import TreeNode

class BinarySearchTreeNode(TreeNode):

    def __contains__(self, lbl):
        """ Fill this in! """

    def add(self, lbl):
        if lbl < self.label() and self.left() == None:
            new_leaf = BinarySearchTreeNode(None, lbl, None)
            self.set_left(new_leaf)
        elif lbl < self.label():
            self.left().add(lbl)
        elif lbl > self.label() and self.right() == None:
            new_leaf = BinarySearchTreeNode(None, lbl, None)
            self.set_right(new_leaf)
        elif lbl > self.label():
            self.right().add(lbl)


def example_binary_search_tree():
    chocolate = BinarySearchTreeNode(None, "chocolate", None)
    macaroon = BinarySearchTreeNode(None, "macaroon", None)
    shortbread = BinarySearchTreeNode(None, "shortbread", None)
    gingerbread = BinarySearchTreeNode(chocolate, "gingerbread", macaroon)
    root = BinarySearchTreeNode(gingerbread, "oatmeal", shortbread)
    return root
