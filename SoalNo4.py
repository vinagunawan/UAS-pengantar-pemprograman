NumberTree = [1, 2, 3, [4, 5], [6,[7,8,9]]]

def tampilkanNumber (tree):
    if isinstance (tree, list):
        for number in tree:
            tampilkanNumber (number)
    else:
        print(f'angka{tree}')

tampilkanNumber(NumberTree)