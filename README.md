# Vocalize

**Vocalize** is an interactive tool designed to facilitate audio transcription and text refinement through an AI-driven workflow. It supports recording audio, transcribing it into text, and enriching the transcription with more concise and coherent summaries using artificial intelligence.

## Project Overview

Vocalize is a shell script-based application that combines multiple tools such as **whisper**, **tgpt**, and **whiptail** to provide an efficient and user-friendly audio-to-text transcription process. This tool is particularly useful for users who need to transcribe audio files into text, refine the transcribed text with the help of AI, and manage the transcriptions seamlessly within the terminal.

The tool offers two main modes of operation:
1. **Interactive Mode**: This mode presents a menu-driven interface where users can record audio, transcribe it, refine it with AI, and manage saved files easily.
2. **Minimal Mode**: This mode hides most of the UI elements, only showing the audio recording screen, allowing for a more focused experience.

## How It Works

1. **Audio Recording**: Users can record audio directly from their microphone using the `arecord` command. Once recorded, the audio is converted to the appropriate format using `ffmpeg` and saved in a temporary location.
2. **Transcription**: Using **Whisper**, the recorded audio is transcribed into text in Portuguese. The transcription can be viewed, copied to the clipboard, or saved as a file.
3. **Text Enrichment**: The transcribed text can be improved with the help of **tgpt**, which rewrites the transcription to be more concise and clear, adhering to the user-defined prompt for summarization.
4. **Clipboard Integration**: Both the original transcription and the AI-enhanced text can be copied to the clipboard for easy pasting into other applications.
5. **File Management**: The application allows saving the recorded audio and transcriptions, or removing them from the system when no longer needed. It also supports playback of the recorded audio files directly from the terminal using **mpv**.

## Features

- **Audio Recording**: Record audio directly from the microphone with a simplified interface.
- **Transcription**: Convert audio to text using Whisper with support for Portuguese (Brazil).
- **Text Enrichment**: Improve the quality of the transcribed text with an AI-based prompt.
- **Clipboard Support**: Easily copy the transcribed or AI-enhanced text to the system clipboard.
- **File Management**: Save, delete, or open transcriptions and audio recordings.
- **Minimal Mode**: Run the application with only the audio recording interface visible for a distraction-free experience.
- **Interactive Mode**: Use an easy-to-navigate terminal menu to access all features of the tool.

## Requirements

- **[Whisper.cpp](https://github.com/ggerganov/whisper.cpp)**: A speech-to-text engine for audio transcription.
- **[tgpt](https://github.com/aandrew-me/tgpt)**: A command-line interface to interact with GPT-based AI models.
- **whiptail**: A utility for creating dialog boxes in shell scripts.
- **mpv**: A media player to playback recorded audio.
- **arecord**: For recording audio from the microphone.
- **ffmpeg**: To convert audio files into the appropriate format for transcription.
- **xclip**: A clipboard manager that allows copying text to the system clipboard.

## Installation

### Prerequisites

Before installing **Vocalize**, ensure that you have the necessary dependencies installed on your system. For a Debian-based OS, you can install them using the following commands:

```bash
sudo apt update
sudo apt install -y arecord ffmpeg whiptail mpv xclip
```

- **arecord**: A command-line sound recorder for capturing audio from your microphone.
- **ffmpeg**: A powerful tool to process audio and video files.
- **whiptail**: A tool to create dialog boxes in shell scripts.
- **mpv**: A media player used to play back the recorded audio.
- **xclip**: A clipboard manager that allows copying text to the system clipboard.

### tgpt and whisper.cpp

Comming soon...

### Installing Vocalize

1. Clone the repository or download the source files for **Vocalize**.
   
2. Navigate to the **Vocalize** directory and run the following command to install the tool:

```bash
sudo make install
```

This will install **Vocalize** into `/usr/local/bin` by default. You can specify a different installation path by setting the `prefix` variable during installation, like this:

```bash
sudo make install prefix=/custom/path
```

After installation, the tool will be available to use from the terminal as `vocalize`.

### Uninstallation

To remove **Vocalize** from your system, you can use the following command:

```bash
sudo make uninstall
```

This will remove the `vocalize` executable from the installation directory.

## Usage

(To be added...)

## License

All software is covered by the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

