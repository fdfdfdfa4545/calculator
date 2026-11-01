import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.config import Config
from kivy.lang import Builder

# Настройка размера окна
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False)

# Интерфейс в строке — внешний .kv файл не нужен
KV = """
<CalculatorRoot>:
    orientation: 'vertical'
    padding: 10
    spacing: 10

    TextInput:
        text: root.display_text
        font_size: 45
        readonly: True
        halign: 'right'
        size_hint_y: 0.25
        background_color: 0.15, 0.15, 0.15, 1
        foreground_color: 1, 1, 1, 1
        multiline: False

    GridLayout:
        cols: 4
        spacing: 5
        size_hint_y: 0.75

        Button:
            text: "C"
            font_size: 30
            background_color: 0.8, 0.2, 0.2, 1
            on_press: root.clear()
        Button:
            text: "("
            font_size: 30
            on_press: root.press(self.text)
        Button:
            text: ")"
            font_size: 30
            on_press: root.press(self.text)
        Button:
            text: "/"
            font_size: 30
            background_color: 0.2, 0.4, 0.8, 1
            on_press: root.press(self.text)

        Button:
            text: "7"
            font_size: 30
            on_press: root.press(self.text)
        Button:
            text: "8"
            font_size: 30
            on_press: root.press(self.text)
        Button:
            text: "9"
            font_size: 30
            on_press: root.press(self.text)
        Button:
            text: "*"
            font_size: 30
            background_color: 0.2, 0.4, 0.8, 1
            on_press: root.press(self.text)

        Button:
            text: "4"
            font_size: 30
            on_press: root.press(self.text)
        Button:
            text: "5"
            font_size: 30
            on_press: root.press(self.text)
        Button:
            text: "6"
            font_size: 30
            on_press: root.press(self.text)
        Button:
            text: "-"
            font_size: 30
            background_color: 0.2, 0.4, 0.8, 1
            on_press: root.press(self.text)

        Button:
            text: "1"
            font_size: 30
            on_press: root.press(self.text)
        Button:
            text: "2"
            font_size: 30
            on_press: root.press(self.text)
        Button:
            text: "3"
            font_size: 30
            on_press: root.press(self.text)
        Button:
            text: "+"
            font_size: 30
            background_color: 0.2, 0.4, 0.8, 1
            on_press: root.press(self.text)

        Button:
            text: "."
            font_size: 30
            on_press: root.press(self.text)
        Button:
            text: "0"
            font_size: 30
            on_press: root.press(self.text)
        Button:
            text: "="
            font_size: 30
            background_color: 0.2, 0.7, 0.3, 1
            on_press: root.calculate()
"""


class CalculatorRoot(BoxLayout):
    display_text = StringProperty("0")

    def press(self, button_text):
        current = self.display_text

        if current == "Error":
            current = ""
            self.display_text = ""

        operators = ["+", "-", "*", "/"]

        if button_text in operators and current and current[-1] in operators:
            self.display_text = current[:-1] + button_text
            return

        if current == "0" and button_text not in operators and button_text != ".":
            self.display_text = button_text
        else:
            self.display_text = current + button_text

    def clear(self):
        self.display_text = "0"

    def calculate(self):
        try:
            result = str(eval(self.display_text))
            if '.' in result and result.endswith('.0'):
                result = result[:-2]
            self.display_text = result
        except ZeroDivisionError:
            self.display_text = "Error"
        except Exception:
            self.display_text = "Error"


class CalculatorApp(App):
    def load_kv(self, filename=None):
        # Переопределяем метод, чтобы Kivy НЕ искал внешний .kv файл
        pass

    def build(self):
        Builder.load_string(KV)
        return CalculatorRoot()


if __name__ == "__main__":
    CalculatorApp().run()