# txt2html

## Usage

```
$ python txt2html.py < input.txt > output.html
```

## Structure

### Lexical Analysis

Token: block, lines

`util`: to break things into block and lines

### Syntax Analysis

Syntax Rules: rules and filters

`rules`: syntax rules for each token

`parse`: token visitor

### Interpreter

Semantics/Interpretation: handler

`handlers`
	
## TODO
1. Debug framework
2. Refactor filter to a standalone class
3. Populate more rules and filters