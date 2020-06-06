# -*- coding: utf-8 -*-

"""A package that helps you iterate through parallel files."""


def iter_together(path_left: str, path_right: str):
    """Open The Two files, iterate over then, and zip them together.

    :param path_left:  A path to a CSV file
    :param path_right: A path to a CSV file
    :return:
    """
    with open(path_left) as left_file, open(path_right) as right_file:
        for left_line, right_line in zip(left_file, right_file):
            left_idx, left_value = left_line.strip().split(',')
            right_idx, right_value = right_line.strip().split(',')
            yield left_idx, left_value, right_value
