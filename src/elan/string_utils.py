class string_utils:
    def __init__(self):
        pass

    def reverse(self, string):
        return string[::-1]
    
    def capitalize(self, string):
        return string.capitalize()

    def uppercase(self, string):
        return string.upper()  
    
    def lowercase(self, string):
        return string.lower()
    
    def title(self, string):
        return string.title()
    
    def swapcase(self, string):
        return string.swapcase()
    
    def isalpha(self, string):
        return string.isalpha()
    
    def isdigit(self, string):
        return string.isdigit()
    
    def isspace(self, string):
        return string.isspace()
    
    def isalnum(self, string):
        return string.isalnum()
    
    def islower(self, string):
        return string.islower()
    
    def isupper(self, string):
        return string.isupper()
    
    def istitle(self, string):
        return string.istitle()
    
    def isspace(self, string):
        return string.isspace()
    
    def ispunct(self, string):
        return string.ispunct()
    
    def isprintable(self, string):
        return string.isprintable()
    
    def isidentifier(self, string):
        return string.isidentifier()
    
    def isdecimal(self, string):
        return string.isdecimal()
    
    def reverse_words(self, string):
        return ' '.join(word[::-1] for word in string.split())
    

if __name__ == "__main__":
    string_utils()
    
    
