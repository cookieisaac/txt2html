class Rule:
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True
        
class ParagraphRule(Rule):
    type = 'paragraph'
    def condition(self, block):
        return True
        
class HeadingRule(Rule):
    type = 'heading'
    def condition(self, block):
        return not '\n' in block and len(block) <= 70 and not block[-1]==':'
        