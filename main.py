from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from plyer import notification
import time

class AlarmeSonoreApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.layout.add_widget(Label(text="Alarme Musicale", font_size=25, color=(1, 0.5, 0, 1)))
        
        # Heure
        self.heure_input = TextInput(text=time.strftime("%H:%M"), multiline=False, halign='center', font_size=35)
        self.layout.add_widget(self.heure_input)
        
        # Message
        self.message_input = TextInput(text="C'est l'heure !", multiline=False, halign='center')
        self.layout.add_widget(self.message_input)
        
        # Bouton Activer
        self.btn_active = Button(text="ACTIVER", background_color=(0, 1, 0, 1))
        self.btn_active.bind(on_press=self.basculer_alarme)
        self.layout.add_widget(self.btn_active)

        # Bouton pour arrêter le son manuellement
        self.btn_stop_son = Button(text="COUPER LE SON", size_hint_y=None, height=50, disabled=True)
        self.btn_stop_son.bind(on_press=self.stop_musique)
        self.layout.add_widget(self.btn_stop_son)
        
        self.status_label = Label(text="En attente...")
        self.layout.add_widget(self.status_label)
        
        self.alarme_active = False
        self.son = None
        return self.layout

    def basculer_alarme(self, instance):
        if not self.alarme_active:
            self.alarme_active = True
            self.status_label.text = f"Programmée pour {self.heure_input.text}"
            self.btn_active.text = "ANNULER"
            self.btn_active.background_color = (1, 0, 0, 1)
            Clock.schedule_interval(self.verifier_heure, 1)
        else:
            self.alarme_active = False
            self.status_label.text = "Désactivée"
            self.btn_active.text = "ACTIVER"
            self.btn_active.background_color = (0, 1, 0, 1)
            Clock.unschedule(self.verifier_heure)
            self.stop_musique(None)

    def verifier_heure(self, dt):
        if time.strftime("%H:%M") == self.heure_input.text:
            self.declencher_alerte()
            return False # Arrête la vérification

    def declencher_alerte(self):
        # 1. Notification
        notification.notify(title="ALARME !", message=self.message_input.text)
        
        # 2. Musique
        self.son = SoundLoader.load('wake_up.mp3') # Assure-toi que le fichier est là !
        if self.son:
            self.son.play()
            self.son.loop = True # Pour que ça sonne en boucle
            self.btn_stop_son.disabled = False
        
        self.status_label.text = "DÉCLENCHÉE !"

    def stop_musique(self, instance):
        if self.son:
            self.son.stop()
            self.btn_stop_son.disabled = True
            self.status_label.text = "Son coupé"

if __name__ == "__main__":
    AlarmeSonoreApp().run()