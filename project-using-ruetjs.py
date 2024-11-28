'''
import ruetjs
# import everything from ruetjs file

button1 = ruetjs.Button("Green", "Circular")
link1 = ruetjs.Link("Blue")

link1.click("New Tab")

print(button1.color)
'''

'''
import ruetjs as rj

button1 = rj.Button("Green", "Circular")
link1 = rj.Link("Blue")

link1.click("New Tab")

print(button1.color)
'''

from ruetjs import Button, Link
# import only Button and Link from ruetjs file

button1 = Button("Green", "Circular")
link1 = Link("Blue")

link1.click("New Tab")

print(button1.color)


class NewButton(Button):
    def __init__(self, color, shape, newvar):
        super().__init__(color, shape)
        self.newvar = newvar

nbtn = NewButton("Blue", "Square", "value")
nbtn.buttonClick()