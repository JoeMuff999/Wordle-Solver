

from re import T
from typing import List
import sys
import copy



def init() -> List[int]:
    word_list = open('trimmed_words.txt', 'r')
    word_bank = []
    for word in word_list:
        if word[0].isupper():
            continue
        word_bank.append(word.strip())

    return word_bank


def main(word_bank: List[int]):
    omit = set()
    must_contain = set()
    known_letters = dict()
    remaining_words = copy.copy(word_bank)
    while True:
        to_omit = input("Enter greyed letters\n")
        to_omit.lower()
        to_omit = set([c.lower() for c in to_omit])
        omit = omit.union(to_omit)
        print("omitted letters " + str(set(omit)))

        word = input(
            "Enter correct locations as Caps, enter present letters as lowercase. enter unknowns as question marks\n")

        for idx, c in enumerate(word):
            if c == '?':
                continue
            if c.islower():
                must_contain.add(c)
            else:
                # this is iffy because we can have double letters
                # if c in must_contain:
                # must_contain.remove(c)

                known_letters[idx] = c.lower()

        # compute possibilities
        new_remaining = []
        for word in remaining_words:
            letter_set = set([c.lower() for c in word])
            letter_list = [c.lower() for c in word]
            # make sure no greyed letters
            if contains_omitted(letter_set, to_omit):
                continue

            # make sure green and yellow letters
            if not matches_known_letters(letter_list, known_letters) or not contains_known_letters(letter_set, must_contain):
                continue 
        
            new_remaining.append(word)
        remaining_words = copy.copy(new_remaining)
        print("Possibilties " + str(len(remaining_words)))
        if(len(remaining_words) < 1000):
            print(remaining_words)
        else:
            print("too many possibilites lol")
        msg = input("Continue y/n ?\n")
        if msg == "n":
            break

    print("ty for using :3")

def contains_known_letters(letter_set, must_contain):
    for c in must_contain:
        if c not in letter_set:
            return False
    return True

def matches_known_letters(letter_list : List[chr], known_letters):
    for key in known_letters:
        letter = known_letters[key]
        if letter_list[key] != letter:
            return False
    return True


def contains_omitted(letter_set, omitted):
    for l in omitted:
        if l in letter_set:
            return True
    return False


if __name__ == "__main__":
    word_bank = init()
    main(word_bank)
