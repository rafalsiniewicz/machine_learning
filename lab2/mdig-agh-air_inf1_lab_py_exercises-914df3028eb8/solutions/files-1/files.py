#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path


def write_to_file(path: str) -> bool:
    file_existed = os.path.isfile(path)
    with open(path, 'w') as f:
        f.write("Kilroy was here!")
    return file_existed
