# adr-repr
Custom replica of python's builtin method repr()

For every kind of object, invoke x_repr() function

Snippet example:

x = {3:[4, 5], 5:6, (8,9):{44:{3:9, 7:7}}}
print(x_repr(x))

>>>>{3: [4, 5], 5: 6, (8, 9): {44: {3: 9, 7: 7}}}
