#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def tag_wrapper(tag):
    def inner_function(s):
        return f"{tag}{s}{tag}"
    return inner_function


if __name__ == '__main__':
    tag = input('тег - ')
    s = input('строка - ')

    tag_wrapp = tag_wrapper(tag)
    print(tag_wrapp(s))


