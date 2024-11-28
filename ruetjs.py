class Button:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape
    
    def buttonClick(self):
        print(f"{self.color} Button is clicked!")
        # print(self.color + " Button is clicked!")

class Link:
    def __init__(self, linkcolor):
        self.linkcolor = linkcolor

    def click(self, type):
        self.type = type

        if self.type == "New Tab":
            print("Open URL in New Tab")
        else:
            print("Open URL in current tab")
            