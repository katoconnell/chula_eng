import tkinter as tk
import random

# List of Thai consonants and their pronunciation
thai_consonants = [
    ("ก", "ก ไก่ - gor gai"), ("ข", "ข ไข่ - kho khai"), ("ฃ", "ฃ ขวด - kho khuat"), ("ค", "ค ควาย - kho khwai"),
    ("ฅ", "ฅ คน - kho khon"), ("ฆ", "ฆ ระฆัง - kho rakhang"), ("ง", "ง งู - ngo ngu"), ("จ", "จ จาน - cho chan"),
    ("ฉ", "ฉ ฉิ่ง - cho ching"), ("ช", "ช ช้าง - cho chang"), ("ซ", "ซ โซ่ - so so"), ("ฌ", "ฌ เฌอ - cho choe"),
    ("ญ", "ญ หญิง - yo ying"), ("ฎ", "ฎ ชฎา - do chada"), ("ฏ", "ฏ ปฏัก - to patak"), ("ฐ", "ฐ ฐาน - tho than"),
    ("ฑ", "ฑ มณโฑ - tho montho"), ("ฒ", "ฒ ผู้เฒ่า - tho phuthao"), ("ณ", "ณ เณร - no nen"), ("ด", "ด เด็ก - do dek"),
    ("ต", "ต เต่า - to tao"), ("ถ", "ถ ถุง - tho thung"), ("ท", "ท ทหาร - tho thahan"), ("ธ", "ธ ธง - tho thong"),
    ("น", "น หนู - no nu"), ("บ", "บ ใบไม้ - bo baimai"), ("ป", "ป ปลา - po pla"), ("ผ", "ผ ผึ้ง - pho phueng"),
    ("ฝ", "ฝ ฝา - fo fa"), ("พ", "พ พาน - pho phan"), ("ฟ", "ฟ ฟัน - fo fan"), ("ภ", "ภ สำเภา - pho samphao"),
    ("ม", "ม ม้า - mo ma"), ("ย", "ย ยักษ์ - yo yak"), ("ร", "ร เรือ - ro ruea"), ("ล", "ล ลิง - lo ling"),
    ("ว", "ว แหวน - wo waen"), ("ศ", "ศ ศาลา - so sala"), ("ษ", "ษ ฤๅษี - so ruesi"), ("ส", "ส เสือ - so suea"),
    ("ห", "ห หีบ - ho hip"), ("ฬ", "ฬ จุฬา - lo chula"), ("อ", "อ อ่าง - o ang"), ("ฮ", "ฮ นกฮูก - ho nokhuk")
]

class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        self.root.geometry("400x400")  # Set a fixed window size

        self.current_card = random.choice(thai_consonants)
        self.showing_consonant = True

        # Flashcard UI
        self.card_frame = tk.Frame(root, width=350, height=250, bg="white", relief=tk.RAISED, bd=5)
        self.card_frame.pack(pady=20)

        self.label = tk.Label(self.card_frame, text=self.current_card[0], font=("Arial", 80), bg="white", wraplength=320, justify="center")
        self.label.pack(expand=True, fill=tk.BOTH)

        # Instruction Label
        self.instruction = tk.Label(root, text="Click the card to flip", font=("Arial", 12))
        self.instruction.pack(pady=5)

        # Button for Next
        self.next_button = tk.Button(root, text="Next", font=("Arial", 14), command=self.next_card)
        self.next_button.pack(pady=10)

        # Bind click event for flipping the card
        self.card_frame.bind("<Button-1>", self.flip_card)
        self.label.bind("<Button-1>", self.flip_card)

    def flip_card(self, event=None):
        """Flip between consonant and pronunciation while keeping size the same."""
        if self.showing_consonant:
            self.label.config(text=self.current_card[1], font=("Arial", 30))  # Keep the size fixed
        else:
            self.label.config(text=self.current_card[0], font=("Arial", 80))
        self.showing_consonant = not self.showing_consonant

    def next_card(self):
        """Move to the next flashcard while maintaining consistency."""
        self.current_card = random.choice(thai_consonants)
        self.label.config(text=self.current_card[0], font=("Arial", 80))
        self.showing_consonant = True

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardGame(root)
    root.mainloop()
