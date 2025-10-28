## Finding the longest palindrome(s) in a string

Programming challenge based on the conversation in the office today (2025-10-28).

Write a function that take a string argument and finds the longest palindrome
in it (ignore non-alphabetic chars and case). If there are multiple
equally-long longest palindromes, return them all. E.g.:

    "" -> {""}
    "tillbest" -> {"ll"}
    "leonie meiners" -> {"niemein"}
    "jackson emanuel" -> {"a", "c", "e", "j", "k", "l", "m", "n", "o", "s", "u"}
    
(Interesting that Jackson's name has the six-letter consecutive sequence "jklmno".)

I think there might be many ways to skin this cat (sorry, Jules).

I put a small test suite [here](tests/test_core.py).
