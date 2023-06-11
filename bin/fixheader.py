#! /usr/bin/env python3

# Add some standard cpp magic to a header file

import sys

def main():
    args = sys.argv[1:]
    for filename in args:
        process(filename)

def process(filename):
    try:
        f = open(filename, 'r')
    except IOError as msg:
        sys.stderr.write('%s: can\'t open: %s\n' % (filename, str(msg)))
        return
    data = f.read()
    f.close()
    if data[:2] != '/*':
        sys.stderr.write('%s does not begin with C comment\n' % filename)
        return
    try:
        f = open(filename, 'w')
    except IOError as msg:
        sys.stderr.write('%s: can\'t write: %s\n' % (filename, str(msg)))
        return
    sys.stderr.write('Processing %s ...\n' % filename)
    magic = 'Py_'
    for c in filename:
        magic = magic + c.upper() if ord(c)<=0x80 and c.isalnum() else f'{magic}_'
    sys.stdout = f
    print('#ifndef', magic)
    print('#define', magic)
    print('#ifdef __cplusplus')
    print('extern "C" {')
    print('#endif')
    print()
    f.write(data)
    print()
    print('#ifdef __cplusplus')
    print('}')
    print('#endif')
    print('#endif /*', f'!{magic}', '*/')

if __name__ == '__main__':
    main()
