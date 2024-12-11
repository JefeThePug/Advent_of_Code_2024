"""
--- Part Two ---
 https://adventofcode.com/2024/day/5#part2 
"""

from collections import defaultdict, deque

def middle_of_khan(rules: list[str]) -> int:
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for line in rules:
        a, b = map(int, line.split('|'))
        graph[a].append(b)
        in_degree[b] += 1
        if a not in in_degree:
            in_degree[a] = 0

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    sorted_numbers = []
    while queue:
        current = queue.popleft()
        sorted_numbers.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_numbers[len(sorted_numbers)//2]

def is_incorrect(rules: list[str], book: list[str]) -> bool:
    for rule in rules:
        A, B = rule.split("|")
        if A in book and B in book:
            if book.index(A) > book.index(B):
                return True
    return False

def incorrect_mid_pages(rules: list[str], books: list[list[str]]) -> int:    
    incorrect_books = [book for book in books if is_incorrect(rules, book)]
    
    result = 0
    for book in incorrect_books:
        applicable_rules = [rule for rule in rules if rule[:2] in book and rule[3:] in book]
        result += middle_of_khan(applicable_rules)
    return result    

with open("input.txt") as f:
    rules, books = [chunk.split("\n") for chunk in f.read().split("\n\n")]
    books = [b.split(",") for b in books]
    print(incorrect_mid_pages(rules, books))
    
# Sum of Corrected Middle Pages is 4713
