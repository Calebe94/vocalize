#!/usr/bin/env python3
import gi
import subprocess
import os
import threading

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

class AudioRecorder(Gtk.Window):
    def __init__(self):
        super().__init__(title="Gravador de Áudio")
        self.set_border_width(10)
        self.set_default_size(300, 150)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.record_button = Gtk.ToggleButton(label="Iniciar Gravação")
        self.record_button.connect("toggled", self.on_record_toggle)
        vbox.pack_start(self.record_button, True, True, 0)

        self.delete_button = Gtk.Button(label="Excluir Gravação")
        self.delete_button.connect("clicked", self.on_delete_clicked)
        vbox.pack_start(self.delete_button, True, True, 0)

        self.play_button = Gtk.Button(label="Ouvir Gravação")
        self.play_button.connect("clicked", self.on_play_clicked)
        vbox.pack_start(self.play_button, True, True, 0)

        self.save_button = Gtk.Button(label="Salvar Gravação")
        vbox.pack_start(self.save_button, True, True, 0)

        self.progress_bar = Gtk.ProgressBar()
        vbox.pack_start(self.progress_bar, True, True, 0)

        self.filename = "temp_audio.wav"
        self.is_recording = False
        self.playback_process = None

    def on_record_toggle(self, button):
        if button.get_active():
            button.set_label("Pausar Gravação")
            self.start_recording()
        else:
            button.set_label("Iniciar Gravação")
            self.stop_recording()

    def start_recording(self):
        self.is_recording = True
        self.record_process = subprocess.Popen(['arecord', '-f', 'cd', self.filename],
                                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def stop_recording(self):
        if self.is_recording:
            self.record_process.terminate()
            self.is_recording = False

    def on_delete_clicked(self, button):
        if os.path.exists(self.filename):
            os.remove(self.filename)
        self.progress_bar.set_fraction(0)

    def on_play_clicked(self, button):
        if self.playback_process and self.playback_process.poll() is None:
            # Se já está tocando, para a reprodução atual
            self.playback_process.terminate()
        if os.path.exists(self.filename):
            self.playback_process = subprocess.Popen(['aplay', self.filename])
            # Atualiza a barra de progresso para indicar reprodução (simples indicação, sem controle de tempo real)
            GLib.timeout_add(100, self.monitor_playback)

    def monitor_playback(self):
        if self.playback_process.poll() is None:
            self.progress_bar.pulse()
            return True  # Continua chamando a função para pulsar a barra de progresso
        else:
            self.progress_bar.set_fraction(0)
            return False  # Para de chamar a função quando a reprodução terminar

    def on_save_clicked(self, button):
        # Implementação depende dos requisitos específicos (e.g., escolher novo local/nome para salvar)
        pass

if __name__ == "__main__":
    win = AudioRecorder()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
