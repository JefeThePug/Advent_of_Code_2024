"""
--- Part Two ---

The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the 
Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in 
what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the 
report instead counts as safe.

More of the above example's reports are now safe:

- 7 6 4 2 1: Safe without removing any level.
- 1 2 7 8 9: Unsafe regardless of which level is removed.
- 9 7 6 2 1: Unsafe regardless of which level is removed.
- 1 3 2 4 5: Safe by removing the second level, 3.
- 8 6 4 4 1: Safe by removing the third level, 4.
- 1 3 6 7 9: Safe without removing any level.

Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. 
How many reports are now safe?
"""

def check_part(arr: list[int]) -> bool:
    gap = all(abs(a - b) < 4 for a, b in zip(arr, arr[1:]))
    inc = all(a < b for a, b in zip(arr, arr[1:]))
    dec = all(a > b for a, b in zip(arr, arr[1:]))
    return gap and (inc or dec)

def check(arr: list[int]) -> bool:
    if check_part(arr): 
        return True
    for i in range(len(arr)):
        if check_part(arr[:i] + arr[i + 1:]): 
            return True
    return False

def get_num_safe(s: str) -> int:
    return sum(check(r) for r in map(lambda x: [*map(int, x.split())], s.split("\n")))
    
with open("input.txt") as f:
    print(get_num_safe(f.read()))
    
#717 reports safe
