"""
--- Day 5: Print Queue ---
 https://adventofcode.com/2024/day/5 
"""

def mid_of_correct(rules: list[str], book: list[str]) -> int:
    for rule in rules:
        A, B = rule.split("|")
        if A in book and B in book:
            if book.index(A) > book.index(B):
                return 0
    return int(book[len(book)//2])

def correct_mid_pages(rules: list[str], books: list[list[str]]) -> int:
    return sum(mid_of_correct(rules, book) for book in books)

with open("input.txt") as f:
    rules, books = [chunk.split("\n") for chunk in f.read().split("\n\n")]
    books = [b.split(",") for b in books]
    print(correct_mid_pages(rules, books))
    
# Sum of Correct Middle Pages is 7307
