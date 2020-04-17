#!python3

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        return (self.size == 0)

    def contains(self, string):
        """Return True if this prefix tree contains the given string."""
        return (string in self.strings())

    def insert(self, string):
        """Insert the given string into this prefix tree."""
        # make sure the string not already in the tree
        if self.contains(string) is False:
            # find the node to start adding new letters from
            current_node, index = self._find_node(string)
            # for each index position in the string greater than index
            for i in range(index, len(string)):
                # returned, add a new child node of the node returned
                next_char = string[i]
                # print(next_char)
                new_node = PrefixTreeNode(next_char)
                current_node.add_child(next_char, new_node)
                # then move the current node to its child
                current_node = new_node
            # mark the last node to be added as terminal
            current_node.terminal = True
            # increment size of the tree
            self.size += 1
            # print('Size', self.size)

    def _find_node(self, string):
        """Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node."""
        # Match the empty string
        if len(string) == 0:
            # print('No previous strings')
            return self.root, 0
        # Start with the root node
        node = self.root
        # loop through the letters in string
        index = 0
        # on each iteration see it that letter is a child of node
        while index < len(string) and node.has_child(string[index]) is True:
            # if it is, then move node to that child, and move to next char
            node = node.get_child(string[index])
            # print('Moving to:', node, index, string)
            index += 1
        # return the pair of the node and the index
        return node, index

    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        # Create a list of completions in prefix tree
        completions = []
        node = self._find_node(prefix)[0]
        self._traverse(node, prefix, completions.append)
        return completions
        '''
        # find the node that's as far down as possible given the prefix
        node, index = self._find_node(prefix)
        # build strings based off traversing all the children of this node
        for child in node.children.keys():
            suffix = ''
            suffix = self._traverse()
        '''

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Create a list of all strings in prefix tree
        all_strings = []
        # TODO
        self._traverse(self.root, '', all_strings.append)
        return all_strings

    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function."""
        if node.is_terminal() is True and len(node.children) == 0:
            return prefix
        elif node.is_terminal() is True:
            visit(prefix)
            # return self._traverse(child, prefix + char, visit)
        # else:
        for char in node.children.keys():
            child = node.get_child(char)
            string = self._traverse(child, prefix + char, visit)
            visit(string)

        '''
        # visit the current node
        # visit(node)
        # if node marks the end, return the prefix
        if node.is_terminal() is True:
            return prefix
        else:
            strings = []
            # traverse down each of the children nodes
            for char in node.children.keys():
                child = node.get_child(char)
                string = self._traverse(child, prefix + char, None)
                strings.append(string)
            return strings
        '''


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


def main():
    # Simpe test case of string with partial substring overlaps
    strings = ['ABC', 'ABD', 'A', 'XYZ']
    create_prefix_tree(strings)

    # Create a dictionary of tongue-twisters with similar words to test with
    tongue_twisters = {
        'Seashells': 'Shelly sells seashells by the sea shore'.split(),
        # 'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
        # 'Woodchuck': ('How much wood would a wood chuck chuck'
        #                ' if a wood chuck could chuck wood').split()
    }
    # Create a prefix tree with the similar words in each tongue-twister
    for name, strings in tongue_twisters.items():
        print(f'{name} tongue-twister:')
        create_prefix_tree(strings)
        if len(tongue_twisters) > 1:
            print('\n' + '='*80 + '\n')


if __name__ == '__main__':
    main()
