import sys
from handlers import HTMLRenderer
from parser import BasicTextParser

handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)
