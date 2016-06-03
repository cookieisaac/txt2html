# txt2html

Convert a txt file to html file

## Usage

```
$ python txt2html.py < input.txt > output.html
```

## Feature

### Inline Substitution
1. Support \*emphasis\* 

   *Rule*: `r'\*(.+?)\*'`  

2. Support url 

   *Rule*: `r'(http://[\.a-zA-Z/]+)'`  
   
3. Support email

   *Rule*: `r'[\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+'`  

### Block Markdown
1. Support title

   *Rule*: First heading
   
2. Support heading
   
   *Rule*: A block with no `\n` with less than 70 characters and the last charater is not `:`
   
3. Support list
   
   *Rule*: A consecutive array of list items
 
4. Support list items
   
   *Rule*: A block starting with `-`(hyphen)

5. Support paragraph

   *Rule*: A block that is not marked down as a heading/title or list/list items


## High Level Design

![alt tag](https://github.com/cookieisaac/txt2html/blob/master/misc/uml.png?raw=true)

### Lexical Analysis

Token: block, lines

`util`: to break things into block and lines (lexemes)

### Syntax Analysis

Syntax Rules: rules (conditions) and filters (regex)

`rules`: syntax rules for block-level token, e.g.: list, list item, title, heading, paragraph, etc.

`filters`: syntax rules for within-block elements, e.g.: email, url, emphasis, etc.

### Semantics Analysis

Semantics: How to interpret each rule on a block

`handlers`: handle rule action and filter, using visitor pattern

### Interpreter

`parser`: Assemble rules and filters 
	
## TODO
1. ~~Debug framework~~
2. ~~Refactor filter to a standalone class~~
3. ~~Populate more rules and filters~~
4. Potential Extension: Markdown for table and table item
5. Potential Extension: Support more markup language (Markdown, XML, YAML, etc)
