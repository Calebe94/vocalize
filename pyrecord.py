import gi
import subprocess
import os
import time

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

class AudioRecorder(Gtk.Window):
    def __init__(self):
        super().__init__(title="Gravador de Áudio")
        self.set_border_width(10)
        self.set_default_size(400, 250)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.status_label = Gtk.Label(label="Pronto")
        vbox.pack_start(self.status_label, True, True, 0)

        self.record_button = Gtk.ToggleButton(label="Iniciar Gravação")
        self.record_button.connect("toggled", self.on_record_toggle)
        vbox.pack_start(self.record_button, True, True, 0)

        self.delete_button = Gtk.Button(label="Excluir Gravação")
        self.delete_button.connect("clicked", self.on_delete_clicked)
        vbox.pack_start(self.delete_button, True, True, 0)

        self.play_button = Gtk.ToggleButton(label="Ouvir Gravação")
        self.play_button.connect("toggled", self.on_play_clicked)
        vbox.pack_start(self.play_button, True, True, 0)

        self.save_button = Gtk.Button(label="Salvar Áudio")
        self.save_button.connect("clicked", self.on_save_clicked)
        vbox.pack_start(self.save_button, True, True, 0)

        # Split horizontal para progress bar e tempo de progresso
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        self.progress_bar = Gtk.ProgressBar()
        hbox.pack_start(self.progress_bar, True, True, 0)

        self.progress_time_label = Gtk.Label(label="00:00")
        hbox.pack_end(self.progress_time_label, False, False, 0)

        self.filename = "temp_audio.wav"
        self.is_recording = False
        self.playback_process = None
        self.recording_start_time = None
        self.update_progress_id = None

    def format_time(self, seconds):
        m, s = divmod(seconds, 60)
        return f"{int(m):02d}:{int(s):02d}"

    def on_record_toggle(self, button):
        if button.get_active():
            button.set_label("Pausar Gravação")
            self.start_recording()
        else:
            button.set_label("Iniciar Gravação")
            self.stop_recording()

    def start_recording(self):
        self.is_recording = True
        self.recording_start_time = time.time()
        self.record_process = subprocess.Popen(['arecord', '-f', 'cd', self.filename],
                                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.status_label.set_text(f"Gravando áudio...")
        GLib.timeout_add_seconds(1, self.update_recording_time)

    def update_recording_time(self):
        if self.is_recording:
            elapsed_time = time.time() - self.recording_start_time
            self.progress_time_label.set_text(self.format_time(elapsed_time))
            return True
        return False

    def stop_recording(self):
        if self.is_recording:
            self.record_process.terminate()
            self.is_recording = False
            self.status_label.set_text(f"Gravação concluída!")
            self.progress_time_label.set_text("00:00")

    def on_delete_clicked(self, button):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            self.status_label.set_text(f"Áudio excluído com sucesso.")
            self.progress_time_label.set_text("00:00")
        else:
            self.status_label.set_text("Nenhum áudio para excluir!")
        self.progress_bar.set_fraction(0)

    def on_play_clicked(self, button):
        if self.playback_process and self.playback_process.poll() is None:
            self.playback_process.terminate()
        if os.path.exists(self.filename):
            self.playback_process = subprocess.Popen(['aplay', self.filename])
            self.status_label.set_text(f"Ouvindo áudio...")
            button.set_label("Reproduzindo...")
            if self.update_progress_id is not None:
                GLib.source_remove(self.update_progress_id)
            self.update_progress_id = GLib.timeout_add(100, self.update_playback_progress)
            button.set_active(False)
        else:
            self.status_label.set_text(f"Nenhum áudio para ouvir!")
            button.set_label("Ouvir Gravação")
            button.set_active(False)

    def update_playback_progress(self):
        # Esta função precisa ser ajustada para monitorar o progresso real da reprodução se possível.
        # Atualmente, ela só pulsa a progress_bar sem mostrar o tempo de progresso real.
        if self.playback_process.poll() is None:
            self.progress_bar.pulse()
            return True
        else:
            self.progress_bar.set_fraction(0)
            return False

    def on_save_clicked(self, button):
        if os.path.exists(self.filename):
            save_filename = f"audio_{int(time.time())}.wav"
            os.rename(self.filename, save_filename)
            self.status_label.set_text(f"Áudio salvo como: {os.path.basename(save_filename)}")
        else:
            self.status_label.set_text(f"Nenhum áudio para salvar!")

if __name__ == "__main__":
    win = AudioRecorder()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
