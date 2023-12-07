# python 3.9.6 64-bit
# 2023/12/6
""" 
Task: Implement a Simple Undo Feature in a Mini Text Editor

Objective:
    Create a mini text editor with the capability to add text and an 'undo' feature using a stack to demonstrate the First-In-Last-Out (FILO) principle.

Requirements:
1. Text Addition Functionality:
    Allow the user to add text to the current text.
    Each addition should be recorded as an operation on the stack.

2. Undo Functionality:
    Implement an 'undo' feature that reverts to the state before the most recent text addition.
    Use the stack's FILO behavior to achieve this.
    
Sample Implementation Details:
    Use a Python list as your stack.
    Push the current state of the text onto the stack each time new text is added.
    For 'undo', pop from the stack to return to the previous state.
    Continuously prompt the user for input, allowing them to add text or type "undo".
    After each operation, display the current state of the text.
    Optionally, include an exit condition like typing "exit" or "quit" to end the loop.

Example Workflow:
    Start with an empty text and an empty stack.
    User inputs "Hello" → text becomes "Hello".
    User inputs " World" → text becomes "Hello World".
    User types "undo" → text reverts to "Hello".
    User types "undo" again → text reverts to an empty state.
    (and so on...)

Key Considerations:
    Handle edge cases such as undoing when the stack is empty.
    Provide clear instructions and feedback to the user.
"""

class TextEditor():
    def __init__(self):
        self.text = [] 

    def Check_empty(self) -> bool:
        return len(self.text) == 0 # Boolean Value

    def Add_text(self, text):
        self.text.append(text)
        return f"Text:{' '.join(self.text)}"

    def Undo(self):
        if textEditor.Check_empty():
            return "You cannot undo nothing!"
        else:
            self.text.pop(-1) 
            return f"Text:{' '.join(self.text)}"

textEditor = TextEditor()

while True:
    user_input = input(": ") 
    if user_input.lower() == "undo":
        print(textEditor.Undo())
    elif user_input.lower() == 'quit':
        break
    else:
        print(textEditor.Add_text(user_input))
