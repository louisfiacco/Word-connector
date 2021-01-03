import sys
import string
# Author: Prof. Fitzsimmons
# Date: Fall 2020
# Filename: words.py
#
# Description: Implementation of a search algorithm to find a
# shortest path of words from a given start word to a given
# goal word. At each step, any single letter in the word
# can be changed to any other letter, provided
# that the resulting word is also in the dictionary.
# 
# A dictionary of English words a text file, a start word,
# and a goal word are passed as command line arguments.
# 
# Usage: python3 words.py dictionaryFile startWord endWord

# Python queue implementation (https://docs.python.org/3.5/library/collections.html?highlight=deque#collections.deque)
from collections import deque

# Usage of deque: 
#   q = deque()   # declare new deque
#   q.append('A') # append A to the rear of the queue.
#   q.popleft()   # pop from the front of the queue.

class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

    # Nodes with the same state are viewed as equal
    def __eq__(self, other_node):
        return isinstance(other_node, Node) and self.state == other_node.state
    
    # Nodes with the same state hash to the same value
    # (e.g., when storing them in a set or dictionary)
    def __hash__(self):
        return hash(self.state)

def read_file(filename):
    """Read in each word from a dictionary where each
    word is listed on a single line."""
    print("Reading dictionary: " +filename)
    word_dict = set()

    dictionary = open(filename)

    # Read each word from the dictionary
    for word in dictionary:
        # Remove the trailing newline character
        word = word.rstrip('\n')

        # Convert to lowercase
        word = word.lower()

        word_dict.add(word)

    dictionary.close()

    return word_dict

def find_path(startWord, goalWord, word_dict):
    """Returns a list of words in word_dict
    that form the shortest path from startWord to goalWord,
    and returns None if no such path exists."""

    # Insert your code for searching here.

    if len(startWord) != len(goalWord):
        print('Words must be same length')
        return None

    frontier = deque()
    explored = list()
    s = Node(startWord, None)

    if s.state == goalWord:
        return frontier
        
    frontier.append(s)

    while len(frontier) != 0:
        letters = list(string.ascii_lowercase)
        x = frontier.popleft()
        explored.append(x.state)
        for i in range(len(startWord)):
            for letter in letters:
                list_word = list(x.state)
                list_word[i] = letter
                child = Node("".join(list_word), None)
                if child.state in word_dict and child.state not in explored:
                    if child not in frontier:
                        child.parent = x
                        if child.state == goalWord:
                            return child
                        frontier.append(child)
    return None

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 words.py dictionaryFile startWord goalWord")
    else:
        dictionaryFile = sys.argv[1]
        startWord = sys.argv[2]
        goalWord = sys.argv[3]

        word_dict = set()
        word_dict = read_file(dictionaryFile)

        if startWord not in word_dict:
            print(startWord + " is not in the given dictionary.")
        else:
            print("-- Shortest path from " + startWord + " to " + goalWord + " --")
            
            solution = (find_path(startWord, goalWord, word_dict))

            if(solution is None):
                print("None exists!")
            else:
                # I changed the orignal code here to print out and iterate through node values
                while solution is not None:
                    print (solution.state)
                    solution = solution.parent

if __name__ == "__main__":
    main()
