def lines(file):
    '''
    Tags an empty line onto the end of the file
    '''
    for line in file:
        yield line
    yield '\n'
    
def blocks(file):
    '''
    Generates block spliited by an empty line
    '''
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []