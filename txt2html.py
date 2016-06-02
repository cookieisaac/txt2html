import sys
from lib.handlers import HTMLRenderer
from lib.parser import BasicTextParser

handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)
