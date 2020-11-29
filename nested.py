#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
Reads lines in input.txt  & writes to output.txt
"""
__author__ = "kamela williamson"
# study hall on Tuesday night with Piero & group

import sys


def is_nested(line):
    """Validate a single input line for correct nesting"""
    # matched pairs are properly nested
    openers = ["(", "[", "{", "<", "(*"]
    closers = [")", "]", "}", ">", "*)"]
    stack = []
    count = 0
    while line:
        count += 1
        # get the 1st char from the line
        token = line[0]
        if line[:2] == "(*" or line[:2] == "*)":
            token = line[:2]
        # put it in the stack if it's an opening bracket
        if token in openers:
            stack.append(token)
        # if it's a closing bracket,find it's match
        # buddy & compare it to the pop
        if token in closers:
            # locate the token in the closers
            # use that location to find opening buddy
            expected_index = closers.index(token)
            expected_opener = openers[expected_index]
            if stack.pop() != expected_opener:

                print("NO", count)
                return
        line = line[len(token):]
# final stack check
    if len(stack) > 0:
        return ("NO " + str(count))
    else:
        return "YES"


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    with open('input.txt', 'r') as f:
        with open('output.txt', 'w') as output:
            for line in f:
                output.write(str(is_nested(line)) + '\n')


if __name__ == '__main__':
    main(sys.argv[1:])
