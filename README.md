# get-git-object
Decode a git object for viewing, useful perhaps for some forensic case one day

git seems to store objects zlib compressed, with some minimal formatting. Linux's compress -d will not decode them though. This little utility does what I had hoped compress -d did.

Usage: ./gitit.py <file>

You can run it from a .git/objects directory like so, to dump everything:

for i in `find . -type f`; do /path/to/gitit.py $i; done
