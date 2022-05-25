# fileSimpleTokenizer
a simple module for tokenize **large** text document
## readFile(parameter): only take one argument as like path object. type: string:
example: readFile('root/folder/file.txt')
## tokenizer(target, source, caseSensetive = True)
target: str, path to save file as txt.
source: str, path to read txt file
caseSensensetive: bool, cased or uncased. example:  'Joseph Forest is a good man' 
caseSensetive = False: 'joseph forest is a good man'
