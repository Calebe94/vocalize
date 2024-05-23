# vocalize

O Vocalize é uma Simples ferramenta TUI desenvolvida em Shell Script para gravar voz e transformá-la em texto. Esta ferramenta foi criada para facilitar a captura de áudio e sua posterior transcrição em texto.

Oferece uma interface gráfica intuitiva para gravar áudio, excluir gravações, ouvir o áudio gravado e salvar a transcrição em texto resultante.

## Dependências

As dependências do projeto atual são os seguintes programas:

- [whisper](https://github.com/ggerganov/whisper.cpp)
- whiptail
- mpv
- arecord
- ffmpeg

### Instalando através do código fonte

Para clonar e executar o projeto, utilize os seguintes passos:

Clone o repositório:

```sh
git clone https://github.com/calebe94/vocalize
```

Instalação:

```sh
sudo make install
```

Após a instalação, basta rodar o `vocalize`.

## Uso

- Ao iniciar o script, uma interface será exibida com opções para gravar, excluir, ouvir, salvar e transcrever o áudio.
- A opção "Gravar" inicia a gravação do áudio, podendo ser interrompida a qualquer momento.
- O botão "Excluir Áudio" remove o arquivo de áudio gravado.
- Para ouvir o áudio gravado, clique em "Ouvir".
- A transcrição do áudio, se disponível, pode ser visualizada ao clicar em "Abrir Transcrição (experimental)".

## Contribuindo

Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões para melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

# Desenvolvedor

| <img src="https://github.com/Calebe94.png?size=200" alt="Edimar Calebe Castanho"> |
|:---------------------------------------------------------------------------------:|
| [Edimar Calebe Castanho (Calebe94)](https://github.com/Calebe94)                  |

## Licença

Todo o software está coberto pela [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
