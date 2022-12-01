#cups_input = "389125467"
cups_input = "364289715"

class Node:
    label = None
    next_node = None

    def __init__(self, label, next_node=None):
        self.label = label

    def __repr__(self):
        return self.label

    @property
    def display_list(self):
        head = self
        node = None
        ret = ''
        while node != head:
            if not node:
                node = head
            ret += f'{node.label} => '
            node = node.next_node
        return ret

    def pick_next(self):
        n = self.next_node
        for _ in range(0, 3):
            picked = n
            n = picked.next_node
            picked.next_node = None
            yield picked
        self.next_node = n

    def find_dest(self):
        labels = {}

        n = None
        while n != self:
            if not n:
                n = self
            labels[n.label] = n
            n = n.next_node

        sorted_labels = list(sorted(labels))
        if sorted_labels.index(self.label) > 0:
            destination = labels[sorted_labels[sorted_labels.index(self.label) - 1]]
        else:
            destination = labels[sorted_labels[-1]]

        return destination

    def append(self, nodes):
        orig_next = self.next_node
        cur = self
        while nodes:
            n = nodes.pop(0)
            cur.next_node = n
            cur = cur.next_node
        cur.next_node = orig_next

    @property
    def solution(self):
        cur = self
        while cur.label != "1":
            cur = cur.next_node

        ret = ''
        cur = cur.next_node
        while cur.label != "1":
            ret += cur.label
            cur = cur.next_node
        return ret

prev = None
head = None
for i, char in enumerate(cups_input):
    node = Node(char)
    if not head:
        head = node
    if prev:
        prev.next_node = node
    if i == len(cups_input) - 1:
        node.next_node = head
    prev = node

current = head

for move in range(1, 101):
    print(f'-- move {move} --')
    print(f'cups: {current.display_list}')
    picked = list(current.pick_next())
    print(f'picked : {picked}')
    dest = current.find_dest()
    print(f'destination : {dest}')
    dest.append(picked)
    current = current.next_node

print(f'Final cups : {current.display_list}')
print(f'Part 1 solution : {current.solution}')
