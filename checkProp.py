#!/usr/bin/env

'''
Currently script returns a list of duplicate keys
in properties files.

Future goal is to run a series of validation steps.

#TO DO:

1. Check K,V with double == operator are flagged.

2. Check K, V separated with whitespace on either side of operator
are included in count.

3. Check K, V e.g

CITIES=\
        Detroit,\
        Chicago,\
        Los Angeles

are included as duplicates.

4. Flag if double slashes are not escaped.

5. Flag where unicode characters are not escaped.


'''

import codecs
import os
from os import walk
import fnmatch


def findPropDupes(f):
    keys = []
    eq = '='
    with codecs.open(f, 'r', encoding='UTF-8') as source:
            for line in source:
                if any(x in line for x in eq):  # Excludes non k, v pairs.
                    keys.append(line.split('=', 1)[0])
            duplicates = [x for x in keys if keys.count(x) > 1]
            duplicates = (set(duplicates))  # Returns unique values.
            print(
                'duplicate key(s) found in: ' +
                f + ' - Key(s) is/are: ' +
                '\n' * 2 + '\n'.join(list(duplicates)))
    return len(duplicates)


def main():

    for dirName, subdirlist, filelist in walk('.'):
        for f in filelist:
            if fnmatch.fnmatch(f, '*.properties'):
                findPropDupes(os.path.join(dirName, f))


if __name__ == '__main__':
    main()
