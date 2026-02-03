from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import os

class BankakBooster(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.status_label = Label(text="حالة الاتصال: متوقف", font_size='20sp')
        layout.add_widget(self.status_label)
        
        btn_start = Button(text="ليغشت (تشغيل الوضع)", background_color=(0, 1, 0, 1))
        btn_start.bind(on_press=self.start_boost)
        layout.add_widget(btn_start)
        
        btn_stop = Button(text="و فاقي (إيقاف)", background_color=(1, 0, 0, 1))
        btn_stop.bind(on_press=self.stop_boost)
        layout.add_widget(btn_stop)
        
        return layout

    def start_boost(self, instance):
        # هنا يتم تشغيل الـ Ping لحل مشكلة الاستجابة
        os.system("ping -i 0.2 8.8.8.8 &") 
        self.status_label.text = "حالة الاتصال: فعال (تحسين الاستجابة)"

    def stop_boost(self, instance):
        os.system("pkill ping")
        self.status_label.text = "حالة الاتصال: متوقف"

if __name__ == '__main__':
    BankakBooster().run()
