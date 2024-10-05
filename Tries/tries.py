#!/usr/bin.env python3

# can be found in leetcode qns 208

# A tries (aka prefix tree) is a tree data structure used to efficiently store & retrieve keys in a dataset of strings
# (or the way i interpret is retrieve substrings/ strings from dataset of strings).
# This can be used in programs such as autocomplete, spellchecker, or even contains() methods.

# Trie implementation
# use a node?
# None
# |  \
# "a" "b" => # if this is the end, all the nodes in next_char_list will be empty
#             # if b is the end, is_end will be true

class Node:
    def __init__(self, char):
        self.curr_char = char
        self.is_end = False
        self.next_char_list = [False] * 26

    def f_is_end(self): # cant be the same name as a variable
        return self.is_end

    def set_end(self):
        self.is_end = True

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            # add the c into the layers, indicate a break at the last char
            pos = ord(c) - ord("a") # only lowercase english letters
            if not curr.next_char_list[pos]:
                curr.next_char_list[pos] = Node(pos)
            curr = curr.next_char_list[pos]
        
        # curr is the last node now
        curr.set_end()

    def search(self, word: str) -> bool:
        # return true if the string is in the trie => need a indicator that the char is the end of the word
        curr = self.head
        for c in word:
            if not curr.next_char_list[ord(c)-ord("a")]:
                return False
            curr = curr.next_char_list[ord(c)-ord("a")]
        
        # check if its the end of the string
        return curr.f_is_end()

    def startsWith(self, prefix: str) -> bool:
        # return true if there is a string with this prefix
        curr = self.head
        for c in prefix:
            if not curr.next_char_list[ord(c)-ord("a")]:
                return False
            curr = curr.next_char_list[ord(c)-ord("a")]
        return True

def main():
    # Code to test Trie
    # refer to leetcode test cases

    # Your Trie object will be instantiated and called as such:
    # obj = Trie()
    # obj.insert(word)
    # param_2 = obj.search(word)
    # param_3 = obj.startsWith(prefix)
    pass

if __name__ == "__name__":
    main()
