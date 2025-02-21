import tkinter as tk
import random

# List of Thai consonants and their pronunciation
thai_consonants = [
    ("ก", "gor gai"),
    ("\u0e02", "kho khai"),
    ("\u0e03", "kho khuat"),
    ("\u0e04", "kho khwai"),
    ("\u0e05", "kho khon"),
    ("\u0e06", "kho rakhang"),
    ("\u0e07", "ngo ngu"),
    ("\u0e08", "cho chan"),
    ("\u0e09", "cho ching"),
    ("\u0e0a", "cho chang"),
    ("\u0e0b", "so so"),
    ("\u0e0c", "cho choe"),
]

class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.current_card = random.choice(thai_consonants)
        self.flipped = False
        
        self.card_frame = tk.Frame(root, width=300, height=200, bg="white", relief=tk.RAISED, bd=5)
        self.card_frame.pack(pady=20)
        
        self.label = tk.Label(self.card_frame, text=self.current_card[0], font=("Arial", 100))
        self.label.pack(expand=True)
        
        self.card_frame.bind("<Button-1>", self.flip_card)
        self.label.bind("<Button-1>", self.flip_card)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card, font=("Arial", 14))
        self.next_button.pack()
    
    def flip_card(self, event):
        if self.flipped:
            self.label.config(text=self.current_card[0])
        else:
            self.label.config(text=self.current_card[1])
        self.flipped = not self.flipped
    
    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.label.config(text=self.current_card[0])
        self.flipped = False

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardGame(root)
    root.mainloop()
