Use default words file `/usr/share/dict/words`:
```bash
$ ./anagram.py solve silent
enlist
listen
tinsel
```
...or pass custom words file:
```bash
$ ./anagram.py solve -w words silent
```
...or index words file for reuse:
```bash
$ ./anagram.py index words | gzip > words.idx.json.gz
$ gunzip -c words.idx.json.gz | ./anagram.py solve -i - silent
```
