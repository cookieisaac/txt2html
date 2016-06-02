from util import lines, blocks
from rules import *
from filters import *

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
        
    def addFilter(self, filter):
        self.filters.append(filter)
        
        
    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            #Update block with filter. eg: *this* to <em>this</em>
            for filter in self.filters:
                block = filter.filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end('document')
        
class BasicTextParser(Parser):
    def __init__(self, handler):
        Parser.__init__(self, handler)
        
        #Note: The order of rules matters here. Only one rule will apply to a block
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())
        #Note '.+' is greedy whereas '.+?' is lazy/non-greedy
        self.addFilter(EmphasisFilter())
        self.addFilter(UrlFilter())
        self.addFilter(EmailFilter())

    