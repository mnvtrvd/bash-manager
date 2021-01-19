from bash import add_alias
from bash import rm_alias
from bash import list_alias

def test():
    add_alias('cat', 'fdsaf')
    add_alias('dog', 'fdsaf')
    add_alias('frog', 'fdsaf')
    add_alias('turtle', 'fdsaf')
    add_alias('lion', 'fdsaf')

    list_alias()

    ''' before
    alias cat='fdsaf'
    alias dog='fdsaf'
    alias frog='fdsaf'
    alias turtle='fdsaf'
    alias lion='fdsaf'
    '''

    rm_alias('fmrog') # alias 'fmrog' does not exist
    rm_alias('tutle') # alias 'tutle' does not exist
    rm_alias('lion') # removed alias 'lion'

    add_alias('dog', 'fdsaf') # alias already exists
    add_alias('cat', 'fdsafdsf') # want to replace alias cat='fdsaf' ; n
    add_alias('frog', 'fdsafdsf') # want to replace alias cat='fdsaf' ; y
    add_alias('tiger', 'fdsafdsafdsa') # added alias tiger='fdsafdsafdsa'

    list_alias()

    ''' after
    alias cat='fdsaf'
    alias dog='fdsaf'
    alias turtle='fdsaf'
    alias frog='fdsafdsf'
    alias tiger='fdsafdsafdsa'
    '''

    rm_alias("cat")
    rm_alias("dog")
    rm_alias("turtle")
    rm_alias("frog")
    rm_alias("tiger")

test()