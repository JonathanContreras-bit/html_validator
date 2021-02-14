#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking
    whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    # enforces proper order / formatting
    stack = []
    if _extract_tags(html):
        for tag in _extract_tags(html):
            if tag[1] != '/':
                stack.append(tag)
            else:
                if len(stack) == 0:
                    return False
                if (stack[-1][1] != '/' and tag[2:] == stack[-1][1:]):
                    stack.pop()
        return len(stack) == 0
    else:
        return html == ''

    # HINT:
    # use the _extract_tags function below to generate a list of html tags
    # without any extra text;
    # then process these html tags using the balanced parentheses algorithm
    # from the class/book
    # the main difference between your code and the code from class will be
    # that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used
    directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input
    string, stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = []
    for i in range(len(html)):
        count = 1
        if html[i] == '<':
            while ((i + count) < len(html)) and (html[i + count] != '>'):
                count += 1
            if (i + count) >= len(html):
                return tags
            else:
                string = html[i:i + count + 1]
                if ' ' in string:
                    space_i = string.index(' ')
                    string = string[:space_i] + string[-1]
                tags.append(string)
    return tags
