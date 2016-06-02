import re
from util import lines, blocks
from rules import *

class Parser:
    """
    A parser reads a text file, apply rules and control a handler.
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []
        
    def addRule(self, rule):
        self.rules.append(rule)
        
    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)
        
        
    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            #Update block with filter. eg: *this* to <em>this</em>
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end('document')
        
class BasicTextParser(Parser):
    def __init__(self, handler):
        Parser.__init__(self, handler)
        #self.addRule(HeadingRule())
        self.addRule(ParagraphRule())
        #Note '.+' is greedy whereas '.+?' is lazy/non-greedy
        self.addFilter(r'\*(.+?)\*', 'emphasis')

    