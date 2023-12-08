from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class CalculatorWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        print('test')
        self.inputs = BoxLayout()
        self.inputs.add_widget(TextInput(input_filter='float', multiline=False, size_hint=(0.2, 0.75)))
        self.inputs.add_widget(TextInput(input_filter='float', multiline=False,size_hint=(0.2, 0.75)))
        self.inputs.add_widget(TextInput(input_filter='float', multiline=False, size_hint=(0.2, 0.75)))

        self.listK_spinner = Spinner(
            text='Выберите K',
            values=('600', '640', '800', '1000', '1200', '1600', '3200', '8000'),
            size_hint=(None, None),
            size=(100, 50)
        )

        self.calculate_btn = Button(text='Рассчитать')
        self.calculate_btn.bind(on_press=self.calculate)

        self.add_widget(self.inputs)
        self.add_widget(self.listK_spinner)
        self.add_widget(self.calculate_btn)
        self.result_label = Label(text='')
        self.add_widget(self.result_label)

    def calculate(self, instance):
        try:
            a, b, c = [float(x.text) for x in self.inputs.children[::-1]]
            k = float(self.listK_spinner.text)
            kVa = 0.22 * (a + b + c)
            kVt = kVa * 0.9
            t = 3600 * 5 / k / kVt
            res_kVa = round(kVa, 2)
            res_kVt = round(kVt, 2)
            res_T = round(t, 2)
            self.result_label.text = f'kVa = {res_kVa}\nkVt = {res_kVt}\nt = {res_T}'
        except ValueError:
            self.result_label.text = 'Проверьте введенные данные.'


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()


if __name__ == '__main__':
    CalculatorApp().run()