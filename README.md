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

## Installation

(To be added...)

## Usage

(To be added...)

## Requirements

- **[Whisper.cpp](https://github.com/ggerganov/whisper.cpp)**: A speech-to-text engine for audio transcription.
- **[tgpt](https://github.com/aandrew-me/tgpt)**: A command-line interface to interact with GPT-based AI models.
- **whiptail**: A utility for creating dialog boxes in shell scripts.
- **mpv**: A media player to playback recorded audio.
- **arecord**: For recording audio from the microphone.
- **ffmpeg**: To convert audio files into the appropriate format for transcription.

## License

All software is covered by the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

