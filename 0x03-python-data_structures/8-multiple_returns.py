#!/usr/bin/python3
def multiple_returns(sentence):
    string_length = len(sentence)

    if string_length == 0:
        first_char = None
        _tuple = (string_length, first_char)
        return  _tuple
    else:
        first_char = sentence[0]
        _tuple = (string_length, first_char)
        return _tuple
