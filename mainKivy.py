from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operator = ['/','*','+','-']
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation='vertical')
        self.solution = TextInput(
            multiline=False, readonly=True,
            background_color = (0, 0, 0, 1),  # Cor de fundo preta (RGBA)
            foreground_color = (1, 1, 1, 1),  # Cor dos números branca (RGBA)
            font_size = 55,  # Tamanho da fonte
            halign = 'right'  # Alinhamento à direita
        )
        main_layout.add_widget(self.solution)
        buttons = [
            ["7","8","9","/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            # BoxLayout com orientação horizontal
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)

            main_layout.add_widget(h_layout)
            # Adiciona esse layout ao arquivo main_layout;

            # Cria o botão igual (=),associa-o a um manipulador
            # de eventos e adiciona-oa main_layout
            equals_button = Button(
                text='=', pos_hint={'center_x': 0.5, 'center_y': 0.5}
            )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        # Clear the solution widget
        if button_text == 'C':
            self.solution.text = ''
        else:
            if current and (
                self.last_was_operator and button_text in self.operator):
                # Não adicione dois operadores um após o outro
                return
            elif current == "" and button_text in self.operator:
                # O primeiro caractere não pode ser um operador
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
                self.last_button = button_text
                self.last_was_operator = self.last_button in self.operator

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

if __name__ == '__main__':
    app = MainApp()
    app.run()
