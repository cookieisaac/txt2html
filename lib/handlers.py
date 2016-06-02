class Handler:
    def callback(self, prefix, name, *args):
        method_name = prefix + name
        method = getattr(self, method_name, None)
        try:
            return method(*args)
        except Exception as e:
            print ("Exception caught for " + method_name)
            print (e)
            
    def start(self, name):
        self.callback('start_', name)
        
    def end(self, name):
        self.callback('end_', name)
    
    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                match.group(0)
            return result
        return substitution
    """
    An object that handles method calls from the Parser
    
    The implementation uses Visitor Pattern
    """
    
    
class HTMLRenderer(Handler):        
    def feed(self, block):
        print(block)
    
    def start_document(self):
        print('<html><head><title>...</title></head><body>')
        
    def end_document(self):
        print('</body></html>')
        
    def start_paragraph(self):
        print('<p>')
        
    def end_paragraph(self):
        print('</p>')
        
    def start_heading(self):
        print('<h2>')
        
    def end_heading(self):
        print('</h2>')
        
    def start_title(self):
        print('<h1>')
        
    def end_title(self):
        print('</h1>')
        
    def start_listitem(self):
        print('<li>')
        
    def end_listitem(self):
        print('</li>')
        
    def start_list(self):
        print('<ul>')
        
    def end_list(self):
        print('</ul>')
        
    def sub_emphasis(self, match):
        return '<em>%s</em>' % match.group(1)

    def sub_email(self, match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1)) 
        
    def sub_url(self, match):
        return '<a href="%s">%s</a>' % (match.group(1), match.group(1))

        
        