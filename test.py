reservedWords = ['if','then','else','end','repeat','until','read','write']
specialSymbols = [':=','+','-','*','/','=','<', '(',')',';']

class token:
    tokenvalue=""
    tokentype=""
    def __init__(self, tokenvalue, tokentype):
        self.tokentype = tokentype
        self.tokenvalue = tokenvalue
    def is_ID(self):
        if(self.tokentype=="ID"):
            return True
        else:
            return False
    def is_NUM(self):
        if(self.tokentype=="NUM"):
            return True
        else:
            return False
    def is_reservedword(self):
        if(self.tokentype=="reserved words"):
            return True
        else:
            return False
    def is_terminator(self):
        if(self.tokenvalue==";"):
            return True
        else:
            return False
    def iscomparison(self):
        if((self.tokenvalue=='<')or(self.tokenvalue=='=')):
            return True
        else:
            return False
    def isaddop(self):
        if((self.tokenvalue=='+')or(self.tokenvalue=='-')):
            return True
        else:
            return False
    def ismulop(self):
        if((self.tokenvalue=='*')or(self.tokenvalue=='/')):
            return True
        else:
            return False
            
def scanner(given_lines):
    lines = [s.rstrip() for s in given_lines]
    lines = [s.lstrip() for s in lines]
    lines = [s.strip() for s in lines]
    linesStr = " ".join(lines)
    tokens = []
    iterator = 0
    while iterator < len(linesStr):
        token = getNextToken(linesStr, iterator)
        if not token:
            continue
        tokens.append(token)
    return tokens


def getNextToken(codeStr):
    global iterator
    startIndex = iterator
    # firstChar = codeStr[startIndex]
    # identifier 
    # special symbol
    # reserved Word 
    # number
    # comment

    isId = isIdentifier(codeStr,startIndex)
    if isId: 
        endIndex = isId
        identifier = codeStr[startIndex:endIndex]
        token =  token(identifier, 'ID')
        iterator = iterator + endIndex
        return token


    isWord = isReservedWord(codeStr,startIndex)
    if isWord: 
        endIndex = isWord
        identifier = codeStr[startIndex:endIndex]
        token =  token(identifier, 'reserved words')
        iterator = iterator + endIndex
        return token


    isSymbol = isSpecialSymbol(codeStr, startIndex)
    if isSymbol: 
        endIndex = isSymbol
        symbol = codeStr[startIndex:endIndex]
        token =  token(symbol, 'special symbols')
        iterator = iterator + endIndex
        return token

    isN = isNumber(codeStr, startIndex)
    if isN: 
        endIndex = isN
        number = codeStr[startIndex:endIndex]
        token =  token(number, 'NUM')
        iterator = iterator + endIndex
        return token


    isC = isComment(codeStr, startIndex)
    if isC: 
        endIndex = isC
        iterator = iterator + endIndex

    return

def isIdentifier(codeStr,startIndex):
    firstChar = codeStr[startIndex]

    if not firstChar.isalpha(): 
        return False

    while codeStr[startIndex].isalpha() or codeStr[startIndex].isDigit(): 
        startIndex = startIndex + 1
    
    return startIndex
    # return false 
    # or the end index of the identifier
    return False

def isReservedWord(codeStr,startIndex):
    endIndex = isIdentifier(codeStr,startIndex)
    if not endIndex: 
        return False
    identifier = codeStr[startIndex:endIndex]
    if identifier not in reservedWords: 
        return False
    
    return endIndex

    # return false 
    # or the end index of the identifier
    return False

def isSpecialSymbol(codeStr,startIndex):
    firstChar = codeStr[startIndex]
    secondChar = codeStr[startIndex + 1]
    # : 
    # = 
    if firstChar + secondChar in specialSymbols: 
        return startIndex + 2
    if firstChar not in specialSymbols: 
        return False
    
    return startIndex + 1

def isNumber(codeStr,startIndex):
    firstChar = codeStr[startIndex]

    if not firstChar.isdigit() or firstChar != '-':
        return False
    
    while codeStr[startIndex].isdigit() or codeStr[startIndex] == '.' : 
        startIndex = startIndex + 1
        # 4434.3332 

    # return false 
    # or the end index of the identifier
    return startIndex

def isComment(codeStr,startIndex):
    firstChar = codeStr[startIndex]
    if firstChar != '{':
        return False
    
    while codeStr[startIndex] != '}':
        startIndex = 1 + startIndex
    return startIndex