#! /usr/bin/env python3

import sys, webbrowser

def main():
    args = sys.argv[1:]
    if not args:
        print(f"Usage: {sys.argv[0]} querystring")
        return
    list = []
    for arg in args:
        if '+' in arg:
            arg = arg.replace('+', '%2B')
        if ' ' in arg:
            arg = f'"{arg}"'
        arg = arg.replace(' ', '+')
        list.append(arg)
    s = '+'.join(list)
    url = f"http://www.google.com/search?q={s}"
    webbrowser.open(url)

if __name__ == '__main__':
    main()
