import gi
import subprocess
import os
import time
import asyncio
import wave

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

        self.record_button = Gtk.ToggleButton(label="Gravar")
        self.record_button.connect("toggled", self.on_record_toggle)
        vbox.pack_start(self.record_button, True, True, 0)

        self.delete_button = Gtk.Button(label="Excluir")
        self.delete_button.connect("clicked", self.on_delete_clicked)
        vbox.pack_start(self.delete_button, True, True, 0)

        self.play_button = Gtk.ToggleButton(label="Ouvir")
        self.play_button.connect("toggled", self.on_play_clicked)
        vbox.pack_start(self.play_button, True, True, 0)

        self.save_button = Gtk.Button(label="Salvar")
        self.save_button.connect("clicked", self.on_save_clicked)
        vbox.pack_start(self.save_button, True, True, 0)

        self.whisper_button = Gtk.Button(label="Whisper")  # Renamed for clarity
        self.whisper_button.connect("clicked", self.on_whisper_clicked)
        vbox.pack_start(self.whisper_button, True, True, 0)

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
        self.playing = False

    def format_time(self, seconds):
        m, s = divmod(seconds, 60)
        return f"{int(m):02d}:{int(s):02d}"

    def on_record_toggle(self, button):
        if button.get_active():
            button.set_label("Pausar")
            self.start_recording()
        else:
            button.set_label("Gravar")
            self.stop_recording()

    def start_recording(self):
        self.is_recording = True
        self.recording_start_time = time.time()
        self.record_process = subprocess.Popen(['arecord', '-f', 'cd', self.filename],
                                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.status_label.set_text(f"Gravando áudio...")
        self.progress_time_label.set_text("00:00")
        GLib.timeout_add_seconds(1, self.update_recording_time)

    def update_recording_time(self):
        if self.is_recording:
            elapsed_time = time.time() - self.recording_start_time
            self.progress_time_label.set_text(self.format_time(elapsed_time))
            return True  # Continue calling this method
        return False  #

    def get_wav_length(self, filename):
        with wave.open(filename, 'r') as wav_file:
            frames = wav_file.getnframes()
            rate = wav_file.getframerate()
            duration = frames / float(rate)
            return duration

    def update_progress_bar(self, progress_bar, duration, start_time):
        elapsed_time = time.time() - start_time
        fraction = elapsed_time / duration
        progress_bar.set_fraction(fraction)
        if elapsed_time < duration:
            return True  # Continue the timeout
        else:
            progress_bar.set_fraction(1.0)  # Ensure the progress bar completes
            return False  # Stop the timeout

    def start_progress_bar_update(self, progress_bar, filename):
        duration = self.get_wav_length(filename)
        start_time = time.time()
        GLib.timeout_add_seconds(1, self.update_progress_bar, progress_bar, duration, start_time)

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
        if not self.playing:
            if self.playback_process and self.playback_process.poll() is None:
                self.playback_process.terminate()

            if os.path.exists(self.filename):
                self.playback_process = subprocess.Popen(['aplay', self.filename])
                self.status_label.set_text(f"Ouvindo áudio...")
                button.set_label("Parar")
                self.playing = True
                self.start_progress_bar_update(self.progress_bar, self.filename)

            else:
                self.status_label.set_text(f"Nenhum áudio para ouvir!")
                button.set_label("Ouvir")
                button.set_active(False)
        else:
            button.set_label("Ouvir")
            self.playing = False
            self.playback_process.terminate()


    def on_save_clicked(self, button):
        if os.path.exists(self.filename):
            save_filename = f"audio_{int(time.time())}.wav"
            os.rename(self.filename, save_filename)
            self.status_label.set_text(f"Áudio salvo como: {os.path.basename(save_filename)}")
        else:
            self.status_label.set_text(f"Nenhum áudio para salvar!")

    def on_whisper_clicked(self, button):
        self.status_label.set_text("Rodando o Whisper...")
        asyncio.ensure_future(self.run_whisper_async())

    async def run_whisper_async(self):
        cmd = ['whisper', '-f', 'txt', '--language', 'pt', '-o', '.', self.filename]
        process = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        await process.communicate()
        GLib.idle_add(self.process_finished, process)

    def process_finished(self, process):
        self.status_label.set_text("Texto gerado!")
        text_file = self.filename.replace(".wav", ".txt")
        if os.path.exists(text_file):
            with open(text_file) as txt:
                print(txt.read())

def start_gtk_app():
    win = AudioRecorder()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

def asyncio_iteration(*args):
    loop = asyncio.get_event_loop()
    loop.stop()
    loop.run_forever()
    return True

if __name__ == "__main__":
    win = AudioRecorder()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()

    loop = asyncio.get_event_loop()

    GLib.idle_add(asyncio_iteration)

    # Instead of using asyncio.get_event_loop().run_until_complete, just call Gtk.main()
    Gtk.main()
