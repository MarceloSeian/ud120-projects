#!/usr/bin/env python
"""
convert dos linefeeds (crlf) to unix (lf)
usage: dos2unix.py <input> <output>
"""
original = "C:/Users/rockm/OneDrive/Documentos/GitHub/ud120-projects/tools/python2_lesson06_keys.pkl"
destination = "C:/Users/rockm/OneDrive/Documentos/GitHub/ud120-projects/tools/python2_lesson06_keys_unix.pkl"

content = ''
outsize = 0
with open(original, 'rb') as infile:
  content = infile.read()
with open(destination, 'wb') as output:
  for line in content.splitlines():
    outsize += len(line) + 1
    output.write(line + str.encode('\n'))

print("Done. Saved %s bytes." % (len(content)-outsize))
