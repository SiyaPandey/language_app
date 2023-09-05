import random
import tkinter as tk
from tkinter import messagebox

# Vocabulary data
vocabulary = {
    "apple": "manzana",
    "banana": "plátano",
    "carrot": "zanahoria",
    "dog": "perro",
    # Add more words and translations as needed
}

class VocabularyPracticeApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Language Learning App")
        
        self.word_label = tk.Label(root, text="", font=("Helvetica", 18))
        self.word_label.pack(pady=20)
        
        self.user_translation_entry = tk.Entry(root, font=("Helvetica", 16))
        self.user_translation_entry.pack(pady=10)
        
        self.check_button = tk.Button(root, text="Check", command=self.check_translation)
        self.check_button.pack(pady=10)
        
        self.continue_button = tk.Button(root, text="Continue", command=self.next_word)
        self.continue_button.pack(pady=10)
        self.continue_button.config(state=tk.DISABLED)
        
        self.initialize()
    
    def initialize(self):
        self.words = list(vocabulary.keys())
        self.current_word = None
        self.next_word()
    
    def next_word(self):
        if self.words:
            self.current_word = random.choice(self.words)
            self.word_label.config(text=f"What is the Spanish word for '{self.current_word}'?")
            self.user_translation_entry.delete(0, tk.END)
            self.continue_button.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Practice Completed", "You have practiced all the words!")
    
    def check_translation(self):
        user_translation = self.user_translation_entry.get().lower()
        correct_translation = vocabulary.get(self.current_word, "").lower()
        
        if user_translation == correct_translation:
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showinfo("Wrong", f"Wrong. The correct answer is '{correct_translation}'.")
        
        self.continue_button.config(state=tk.NORMAL)
    
def main():
    root = tk.Tk()
    app = VocabularyPracticeApp(root)
    root.mainloop()

if __name__ == "_main_":
    main()