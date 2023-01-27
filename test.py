import requests
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grid = GridLayout(cols=1)
        self.label = Label(text='Enter a Pokemon name:')
        self.grid.add_widget(self.label)

        self.text_input = TextInput(multiline=False)
        self.text_input.bind(on_text_validate=self.get_pokemon_data)
        self.grid.add_widget(self.text_input)

        self.add_widget(self.grid)

    def get_pokemon_data(self, *args):
        pokemon_name = self.text_input.text
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.label.text = f'Name: {data["name"]}\nHeight: {data["height"]}\nWeight: {data["weight"]}'
        else:
            self.label.text = 'Pokemon not found'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm


if __name__ == '__main__':
    MyApp().run()
