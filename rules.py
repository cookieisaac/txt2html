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
        
class TitleRule(HeadingRule):
    type = 'title'
    first = True
    
    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadingRule.condition(self, block)
        
class ListItemRule(Rule):
    # ListItem: A Block starts with a hyphen
    type = 'listitem'
    def condition(self, block):
        return block[0] == '-'
            
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True
        
class ListRule(ListItemRule):
    # List: Rest the begin of first list item and the end of last list item
    type = 'list'
    inList = False
    def condition(self, block):
        return True
            
    def action(self, block, handler):
        if not self.inList and ListItemRule.condition(self, block):
            self.inList = True
            handler.start(self.type)
        elif self.inList and not ListItemRule.condition(self, block):
            self.inList = False
            handler.end(self.type)
        return False