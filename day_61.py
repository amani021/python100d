#-------- DAY 61 "extra exercise" --------
import json, re

facts = {
    1: 'an easy to learn',
    2: 'powerful programming language',
    3:'has efficient high-level data structures',
    4: 'a simple but effective approach to object-oriented programming',
}
x = re.search(r'\bpo\w+', facts[2])
print('Python is:', x.group())
print(json.dumps(facts, indent=2, separators=('',' -> ')))
