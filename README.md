```bash
# use default words file `/usr/share/dict/words`:
$ ./anagram.py solve silent
enlist
listen
tinsel

# pass custom words file:
$ ./anagram.py solve -w words silent

# index words file for reuse
$ ./anagram.py index words | gzip > words.idx.json.gz
$ gunzip -c words.idx.json.gz | ./anagram.py solve -i - silent
```
