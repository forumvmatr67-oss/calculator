#main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.root_layout = BoxLayout(orientation='vertical')
        self.expression = TextInput(multiline=False, readonly=True, font_size=55)
        self.root_layout.add_widget(self.expression)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', 'DEL']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=40)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            self.root_layout.add_widget(h_layout)

        return self.root_layout

    def on_button_press(self, instance):
        current_text = self.expression.text
        button_text = instance.text

        if button_text == 'C':
            self.expression.text = ''
        elif button_text == 'DEL':
            self.expression.text = current_text[:-1]
        elif button_text == '=':
            try:
                result = str(eval(current_text))
                self.expression.text = result
            except Exception:
                self.expression.text = 'Error'
        else:
            self.expression.text = current_text + button_text

if __name__ == '__main__':
    CalculatorApp().run()
