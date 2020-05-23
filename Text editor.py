class Text:
    def __init__(self):
        self.current = ''
        self.font = ''
        
    def write(self, text):
        self.current += text
    
    def set_font(self, font):
        self.font = '[' + font + ']' 

    def show(self):
        return self.font + self.current + self.font
    
    def restore(self, version):
        self.current, self.font = version
        

class SavedText:
    def __init__(self):
        self.versions = []
    
    def save_text(self, text):
        self.versions.append([text.current, text.font])
    
    def get_version(self, index):
        return self.versions[index]        


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()
    
    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
    
    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")
