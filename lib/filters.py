import re

class Filter:
    def filter(self, block, handler):
            return re.sub(self.pattern, handler.sub(self.type), block)
    
class EmphasisFilter(Filter):
    type = 'emphasis'
    pattern = r'\*(.+?)\*'
    
class UrlFilter(Filter):
    type = 'url'
    pattern = r'(http://[\.a-zA-Z/]+)'
    
class EmailFilter(Filter):
    type = 'email'
    pattern= r'[\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+'