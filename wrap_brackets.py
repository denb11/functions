

def wrap_brackets( text ):
    return "(" + text + ")"
#print(wrap_brackets("12345"))

def square_brackets( text ):
    return "[[[" + text + "]]]"
#print(square_brackets("(12345)"))

def square_minmax( text ):
    return "<<<" + text + ">>>"
print(square_minmax("[[[(12345)]]]" ))
