#! /usr/bin/env python3

"""Transform gprof(1) output into useful HTML."""

import html
import os
import re
import sys
import webbrowser

header = """\
<html>
<head>
  <title>gprof output (%s)</title>
</head>
<body>
<pre>
"""

trailer = """\
</pre>
</body>
</html>
"""

def add_escapes(filename):
    with open(filename) as fp:
        for line in fp:
            yield html.escape(line)


def main():
    filename = sys.argv[1] if sys.argv[1:] else "gprof.out"
    outputfilename = f"{filename}.html"
    input = add_escapes(filename)
    with open(outputfilename, "w") as output:
        output.write(header % filename)
        for line in input:
            output.write(line)
            if line.startswith(" time"):
                break
        labels = {}
        for line in input:
            m = re.match(r"(.*  )(\w+)\n", line)
            if not m:
                output.write(line)
                break
            stuff, fname = m.group(1, 2)
            labels[fname] = fname
            output.write('%s<a name="flat:%s" href="#call:%s">%s</a>\n' %
                         (stuff, fname, fname, fname))
        for line in input:
            output.write(line)
            if line.startswith("index % time"):
                break
        for line in input:
            m = re.match(r"(.*  )(\w+)(( &lt;cycle.*&gt;)? \[\d+\])\n", line)
            if not m:
                output.write(line)
                if line.startswith("Index by function name"):
                    break
                continue
            prefix, fname, suffix = m.group(1, 2, 3)
            if fname not in labels:
                output.write(line)
                continue
            if line.startswith("["):
                output.write('%s<a name="call:%s" href="#flat:%s">%s</a>%s\n' %
                             (prefix, fname, fname, fname, suffix))
            else:
                output.write('%s<a href="#call:%s">%s</a>%s\n' %
                             (prefix, fname, fname, suffix))
        for line in input:
            for part in re.findall(r"(\w+(?:\.c)?|\W+)", line):
                if part in labels:
                    part = f'<a href="#call:{part}">{part}</a>'
                output.write(part)
        output.write(trailer)
    webbrowser.open(f"file:{os.path.abspath(outputfilename)}")

if __name__ == '__main__':
    main()
