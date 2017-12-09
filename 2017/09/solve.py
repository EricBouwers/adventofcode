#!/usr/bin/env python

import sys, re, ast

def cleanup(x):
    x = re.sub(r"\!.","", x)    
    x = re.sub(r"<[^>]*>", "", x)    
    return x

def list_val(x, level_val):
    result = level_val
    result += sum(map(lambda y: list_val(y, level_val+1), x))
    return result

def score(x):
    list_rep = x.replace("{","[").replace("}","]")
    list_rep = re.sub(r"\[,*\]","[]",list_rep)
    list_rep = re.sub(r",\]","]",list_rep)
    list_rep = re.sub(r"\[,","[",list_rep)
    l = ast.literal_eval(list_rep)
    return list_val(l, 1) 

def count_garbage(x):
    x = re.sub(r"\!.","", x)    
    start = len(x)
    x = re.sub(r"<[^>]*>", "<>", x)    
    return start - len(x)


if __name__ == '__main__':

    assert cleanup("<>") == ""
    assert cleanup("<random characters>") == ""
    assert cleanup("<<<<<>") == ""
    assert cleanup("<{!>}>") == ""
    assert cleanup("<!!>") == ""
    assert cleanup("<!!!>>") == ""
    assert cleanup("<{o\"i!a,<{i<a>") == ""

    assert score(cleanup("{}")) == 1 
    assert score(cleanup("{{{}}}")) == 6 
    assert score(cleanup("{{},{}}")) == 5 
    assert score(cleanup("{{{},{},{{}}}}")) == 16
    assert score(cleanup("{<a>,<a>,<a>,<a>}")) == 1 
    assert score(cleanup("{{<ab>},{<ab>},{<ab>},{<ab>}}")) == 9 
    assert score(cleanup("{{<!!>},{<!!>},{<!!>},{<!!>}}")) == 9 
    assert score(cleanup("{{<a!>},{<a!>},{<a!>},{<ab>}}")) == 3 

    assert count_garbage("<>") == 0
    assert count_garbage("<rancom characters>") == 17
    assert count_garbage("<<<<>") == 3
    assert count_garbage("<{!>}>") == 2
    assert count_garbage("<!!>") == 0
    assert count_garbage("<!!!>>") == 0
    assert count_garbage("<{o\"i!a,<{i<a>") == 10

    print score(cleanup(sys.argv[1]))
    print count_garbage(sys.argv[1])

