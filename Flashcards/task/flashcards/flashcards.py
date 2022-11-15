cards = dict()
print('Input the number of cards:')
n = int(input())
for i in range(n):
    print(f'The term for card #{i + 1}:')
    term = input().strip()
    print(f'The definition for card #{i + 1}:')
    definition = input().strip()
    cards[term] = definition

for term in cards:
    print(f'Print the definition of "{term}":')
    answer = input().strip()
    if answer == cards[term]:
        print('Correct!')
    else:
        print(f'Wrong. The right answer is "{cards[term]}".')


