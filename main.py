from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.uix.image import AsyncImage
import random
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

# Dictionary of English words and their Spanish translations
word_dict = {
    "hello": "hola",
    "goodbye": "adiós",
    "thank you": "gracias",
    "the": "el",
    "of": "de",
    "that": "ese",
    "and": "y",
    "to": "a",
    "in": "en",
    "a": "un",
    "be": "ser",
    "itself": "se",
    "no": "no",
    "to have": "tener",
    "by": "por",
    "with": "con",
    "his, her, its, their": "su",
    "for": "para",
    "like": "como",
    "to be": "estar",
    "to have": "tener",
    "to": "a",
    "the": "la",
    "all": "todo",
    "but": "pero",
    "more": "más",
    "to do": "hacer",
    "or": "o",
    "to be able to": "poder",
    "to say": "decir",
    "this": "este",
    "to go": "ir",
    "other": "otro",
    "that": "ese",
    "if": "si",
    "me": "me",
    "already": "ya",
    "to see": "ver",
    "because": "porque",
    "to give": "dar",
    "when": "cuando",
    "he": "él",
    "very": "muy",
    "without": "sin",
    "time": "tiempo",
    "much": "mucho",
    "to know": "saber",
    "what": "qué",
    "on": "en",
    "my": "mi",
    "some": "alguno",
    "same": "mismo",
    "I": "yo",
    "also": "también",
    "until": "hasta",
    "year": "año",
    "two": "dos",
    "to want": "querer",
    "between": "entre",
    "like this": "así",
    "first": "primero",
    "since": "desde",
    "big": "grande",
    "neither": "ni",
    "us": "nos",
    "to arrive": "llegar",
    "to pass": "pasar",
    "time": "tiempo",
    "she": "ella",
    "yes": "sí",
    "day": "día",
    "one": "uno",
    "well": "bien",
    "little": "poco",
    "to have to": "deber",
    "then": "entonces",
    "to put": "poner",
    "thing": "cosa",
    "so much": "tanto",
    "man": "hombre",
    "to seem": "parecer",
    "our": "nuestro",
    "so": "tan",
    "where": "donde",
    "now": "ahora",
    "part": "parte",
    "after": "después",
    "life": "vida",
    "to stay": "quedar",
    "always": "siempre",
    "to believe": "creer",
    "to talk": "hablar",
    "to carry": "llevar",
    "to leave": "dejar",
    "nothing": "nada",
    "each": "cada",
    "to follow": "seguir",
    "less": "menos",
    "new": "nuevo",
    "to find": "encontrar",
    "to happen": "pasar",
    "people": "gente"
    # Add more words as needed

    # Add more words as needed
}

class QuizApp(App):
    def build(self):
        self.score = 0
        self.num_questions = None
        self.remaining_questions = list(word_dict.keys())
        self.current_question = None
        self.correct_answer = None

        self.question_label = Label(text="", font_size=50,bold=True,color=(0, 0, 0, 1))
        self.answer_input = TextInput(multiline=False, font_size=70)
        self.answer_input.bind(on_text_validate=self.check_answer)
        self.score_label = Label(text="Your Score: 0", font_size=50,bold=True,color=(0, 0, 0, 1))

        layout = BoxLayout(orientation='horizontal')
        with layout.canvas.before:
            Color(0.2, 9, 0.7, 1)  # Set the background color to dark gray
            self.bg_image = Rectangle(source='quiz3.jpg', size=(1950,1000))

        self.num_questions_input = TextInput(multiline=False, font_size=50, hint_text="Please enter the number of questions\nhere:")
        num_questions_panel = BoxLayout(orientation='horizontal')
        num_questions_panel.add_widget(Label(text="Welcome to\nLanguage\nMastery\nQuiz!\n", font_size=130,bold=True, color=(0, 0, 0, 1)))
        num_questions_panel.add_widget(self.num_questions_input)

        
        start_button = Button(text="Start Quiz",size_hint_x=None, width=200 )
        start_button.bind(on_press=self.start_quiz)

        layout.add_widget(num_questions_panel)
        layout.add_widget(start_button)

        return layout
        
       
            

    
    def start_quiz(self, instance): 
            try:
                self.num_questions = int(self.num_questions_input.text)
            except ValueError:
                popup = Popup(title='Error', content=Label(text='Please enter a valid number'), size_hint=(None, None), size=(300, 200))
                popup.open()
                return

            self.remaining_questions = random.sample(list(word_dict.keys()), min(self.num_questions, len(word_dict)))
            self.score = 0
            self.next_question()
        
        # Remove the widgets for number input panel and start button
            self.root.clear_widgets()

            layout = BoxLayout(orientation='vertical')
            layout.add_widget(self.question_label)
            layout.add_widget(self.answer_input)
            layout.add_widget(self.score_label)
           

            self.root.add_widget(layout)

    def next_question(self):
        if len(self.remaining_questions) == 90:
            self.question_label.text = "Quiz Complete!"
            self.answer_input.disabled = True
            return

        self.current_question = random.choice(self.remaining_questions)
        self.remaining_questions.remove(self.current_question)
        self.correct_answer = word_dict[self.current_question]

        self.question_label.text = f"What is the English translation of '{self.correct_answer}'?"
        self.answer_input.text = ""

    def check_answer(self, instance):
        answer = self.answer_input.text.strip().lower()
        if answer == self.current_question:
            self.score += 1
            self.score_label.text = f"Your Score: {self.score}"
            self.question_label.text = "Correct! Next question:"
            Clock.schedule_once(self.next_question_delay, 2)
        else:
            self.question_label.text = f"Wrong answer. Correct translation is '{self.current_question}'. "
    # Delay before proceeding to the next question
            Clock.schedule_once(self.next_question_delay, 3)

    def next_question_delay(self, dt):
        self.next_question()
     
       

if __name__ == '__main__':
    QuizApp().run()