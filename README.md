Use default words file `/usr/share/dict/words`:
```bash
# anagrams for `silent`
$ ./anagram.py solve silent
enlist
listen
tinsel
```
...or pass custom words file:
```
$ ./anagram.py solve -w words silent
```
...or index words file for reuse:
```
$ ./anagram.py index words | gzip > words.idx.json.gz
$ gunzip -c words.idx.json.gz | ./anagram.py solve -i - silent
```
