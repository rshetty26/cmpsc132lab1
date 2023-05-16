# LAB1
# REMINDER: The work in this assignment must be your own original work and must be completed alone

def frequency(txt):
    '''
        >>> frequency('mama')
        {'m': 2, 'a': 2}
        >>> answer = frequency('We ARE Penn State!!!')
        >>> answer
        {'w': 1, 'e': 4, 'a': 2, 'r': 1, 'p': 1, 'n': 2, 's': 1, 't': 2}
        >>> frequency('One who IS being Trained')
        {'o': 2, 'n': 3, 'e': 3, 'w': 1, 'h': 1, 'i': 3, 's': 1, 'b': 1, 'g': 1, 't': 1, 'r': 1, 'a': 1, 'd': 1}
    '''
    # - YOUR CODE STARTS HERE -

    txt = txt.lower()
    dict = {}

    for x in txt:
        if x.isalpha():
            if x in dict:
                dict[x] = dict[x] + 1
            else:
                dict[x] = 1

    return dict

    pass




def invert(d):
    """
        >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
        {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3})
        {1: ['one', 'uno'], 2: ['two', 'dos'], 3: 'three'}
        >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'}) 
        {'Sara': '123-456-78', 'Alex': ['987-12-585', '00000'], 'sara': '258715'}
    """
    # - YOUR CODE STARTS HERE -

    dict = {}

    for x in d:
        if d[x] in dict:
            if isinstance(dict[d[x]], list):
                dict[d[x]].append(x)
            else:
                dict[d[x]] = [dict[d[x]], x]
        else:
            dict[d[x]] = x

    return dict
    
    pass





def employee_update(d, bonus, year):
    '''
        >>> records = {2020:{"John":["Managing Director","Full-time",65000],"Sally":["HR Director","Full-time",60000],"Max":["Sales Associate","Part-time",20000]}, 2021:{"John":["Managing Director","Full-time",70000],"Sally":["HR Director","Full-time",65000],"Max":["Sales Associate","Part-time",25000]}}
        >>> employee_update(records,7500,2022)
        {2020: {'John': ['Managing Director', 'Full-time', 65000], 'Sally': ['HR Director', 'Full-time', 60000], 'Max': ['Sales Associate', 'Part-time', 20000]}, 2021: {'John': ['Managing Director', 'Full-time', 70000], 'Sally': ['HR Director', 'Full-time', 65000], 'Max': ['Sales Associate', 'Part-time', 25000]}, 2022: {'John': ['Managing Director', 'Full-time', 77500], 'Sally': ['HR Director', 'Full-time', 72500], 'Max': ['Sales Associate', 'Part-time', 32500]}}
    '''
    # - YOUR CODE STARTS HERE -

    d[year] = d[year-1]

    for x in d[year]:
        d[year][x][2] += bonus
    
    return d

    pass





if __name__ == "__main__":
    import doctest
    #doctest.run_docstring_examples(frequency, globals(), name='LAB1',verbose=True)   ## Uncomment this line if you want to run doctest by function. Replace get_words with the name of the function you want to run
    #doctest.testmod() ## Uncomment this line if you want to run the docstring in all functions
