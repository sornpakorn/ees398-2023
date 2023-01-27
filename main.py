from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout


class MyApp(App):
    def build(self):
        screen = GridLayout(cols=2)

        screen.add_widget(Image(source='img.png'), Button(text='Pikaju'))
        screen.add_widget(Button(text='Kamex'))
        screen.add_widget(Button(text='Fushigidane'))
        screen.add_widget(Button(text='Butterfree'))

        # pika = Image(source='img.png')
        # screen.add_widget(pika)

        return screen


if __name__ == '__main__':
    MyApp().run()
