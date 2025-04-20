# Introduction

This site contains documentation for the `wordly` python
package. Wordly makes it easy to retrieve definitions of
words over the wire or locally.

Wordly will retrieve dictionary definitions from [dict.org](https://dict.org/bin/Dict)
by default but you may configure your own server hostname and port.

To get started with Wordly you have to install the package and run a command from
your console to retrieve a definition of a term.

```
$ pip install wordly

$ wordly programming
"programming" wn "WordNet (r) 3.0 (2006)"
programming
    n 1: setting an order and time for planned events [syn:
         {scheduling}, {programming}, {programing}]
    2: creating a sequence of instructions to enable the computer to
       do something [syn: {programming}, {programing}, {computer
       programming}, {computer programing}]
.
```

## References

[Dictionary Server Protocol](https://datatracker.ietf.org/doc/html/rfc2229)
