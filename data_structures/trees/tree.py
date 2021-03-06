from data_structures.trees.tree_node import Node
from data_structures.queue.double_ended_queue import Queue


class Tree(object):
    def __init__(self, value):
        self.root = Node(value)

    def set_root(self, node):
        self.root = node

    def get_root(self):
        return self.root

    def compare(self, node_1, node_2):
        if node_1.get_value() == node_2.get_value():
            return 0
        elif node_1.get_value() > node_2.get_value():
            return 1
        else:
            return -1

    def insert_with_loop(self, value):
        new_node = Node(value)
        node = self.root
        if node is None:
            self.root = new_node
            return

        while True:
            comparison = self.compare(node, new_node)
            if comparison == -1:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break
            elif comparison == 1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break
            else:
                node.set_value(value)
                break

    def insert_with_recursion(self, value):
        node = self.get_root()
        new_node = Node(value)
        if node is None:
            self.set_root(new_node)
            return

        self._insert_recursively(node, new_node)

    def _insert_recursively(self, node, new_node):
        comparison = self.compare(node, new_node)
        if comparison == 1:
            if node.has_left_child():
                self._insert_recursively(node.get_left_child(), new_node)
            else:
                node.set_left_child(new_node)
        elif comparison == -1:
            if node.has_right_child():
                self._insert_recursively(node.get_right_child(), new_node)
            else:
                node.set_right_child(new_node)
        else:
            node.set_value(new_node.get_value())

    def __repr__(self):
        root = self.root
        level = 0
        queue = Queue()
        queue.enqueue((root, level))
        visit_order = list()

        while not queue.is_empty():
            node, level = queue.dequeue()
            # if node is None: visit_order append a tuple of <empty> placeholder and level
            if node is None:
                visit_order.append(("<empty>", level))
                continue
            else:
                visit_order.append((node, level))
            # if node has left child: add child and it's level to queue, else, add None to queue
            if node.has_left_child():
                queue.enqueue((node.get_left_child(), level+1))
            else:
                queue.enqueue((None, level+1))
            # if node has right child: add child and it's level to queue, else, add None to queue
            if node.has_right_child():
                queue.enqueue((node.get_right_child(), level+1))
            else:
                queue.enqueue((None, level+1))

        s = "Tree"
        previous_level = -1
        # traverse the visit_order list to get the nodes and placeholders
        for node, level in visit_order:
            # if same level, keep adding node to s
            if level == previous_level:
                s += " | " + str(node)
            # if different level, break the line and add node to s, increase previous level
            else:
                s += "\n" + str(node)
                previous_level += 1
        return s

    def search(self, value):
        node = self.get_root()
        if node is None:
            return False
        new_node = Node(value)
        while True:
            comparison = self.compare(new_node, node)
            if comparison == 0:
                return True
            elif comparison == 1:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return False
            else:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    return False

    def delete(self, target_value):
        if self.root is None:
            return None

        previous_node = None
        current_node = self.root
        del_node = Node(target_value)

        while current_node:
            comparison = self.compare(del_node, current_node)
            if comparison == 0:
                if current_node.has_left_child() and current_node.has_right_child():
                    # current_node is a parent who has 2 children
                    right_sub_tree = current_node.get_right_child()
                    # traverse through the left of sub tree until find the smallest value
                    smallest_node = right_sub_tree.get_left_child()
                    previous_node = right_sub_tree
                    while smallest_node.get_left_child():
                        smallest_node = smallest_node.get_left_child()
                        previous_node = previous_node.get_left_child()

                    # replace current_node's value by smallest node's value of right sub tree
                    current_node.set_value(smallest_node.get_value())

                    if smallest_node.has_right_child():
                        previous_node.set_left_child(smallest_node.get_right_child())
                    else:
                        previous_node.set_left_child(None)
                    break
                elif current_node.has_left_child() and not current_node.has_right_child():
                    # current_node is a parent who has 1 left child
                    if previous_node.get_left_child() == current_node:
                        previous_node.set_left_child(current_node.get_left_child())
                    if previous_node.get_right_child() == current_node:
                        previous_node.set_right_child(current_node.get_left_child())
                    break
                elif not current_node.has_left_child() and current_node.has_right_child():
                    # current_node is a parent who has 1 right child
                    if previous_node.get_left_child() == current_node:
                        previous_node.set_left_child(current_node.get_right_child())
                    if previous_node.get_right_child() == current_node:
                        previous_node.set_right_child(current_node.get_right_child())
                    break
                else:
                    # current_node is a leaf
                    if previous_node.get_left_child() == current_node:
                        previous_node.set_left_child(None)
                    if previous_node.get_right_child() == current_node:
                        previous_node.set_right_child(None)
                    break
            elif comparison == 1:
                previous_node = current_node
                current_node = current_node.get_right_child()
            else:
                previous_node = current_node
                current_node = current_node.get_left_child()
