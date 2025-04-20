# words

Currently the only argument to supply the `wordly` cli application
is a sequence of one or more words. The output will either be a
definition of a word or None if the dict server could not supply
a definition for you. The output of the definitions is not ordered.

## Flags

| flag               | Description                            | example   |
| ------------------ | -------------------------------------- | --------- |
| `-p`, `--port`     | Specify the port number. Default: 2628 | 8001      |
| `-H`, `--hostname` | Specify the server. Default: dict.org  | localhost |
