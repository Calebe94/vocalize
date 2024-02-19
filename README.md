# Vocalize

O Vocalize é uma ferramenta simples desenvolvida em Python para gravar voz e transformá-la em texto. Esta ferramenta foi criada para facilitar a captura de áudio e sua posterior transcrição em texto.

Oferece uma interface gráfica intuitiva para gravar áudio, excluir gravações, ouvir o áudio gravado e salvar a transcrição em texto resultante.

## Dependências

Ele utiliza o módulo `arecord` para gravação de áudio e `aplay` para reprodução de áudio no sistema.

## Instalação

Para utilizar o Vocalize, siga estas etapas:

1. **Pré-requisitos:**
   - Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/).
   - Instale as dependências necessárias executando:
     ```
     pip install PyGObject
     ```

2. **Clone o repositório:**
   ```
   git clone https://github.com/seu_usuario/vocalize.git
   ```

3. **Acesse o diretório do projeto:**
   ```
   cd vocalize
   ```

4. **Execute o aplicativo:**
   ```
   python vocalize.py
   ```

## Uso

- Ao iniciar o aplicativo, você verá uma interface gráfica com opções para gravar, excluir, ouvir e salvar o áudio.
- Clique no botão "Gravar" para iniciar a gravação. O botão se transformará em "Pausar" durante a gravação.
- Você pode pausar a gravação a qualquer momento clicando novamente no botão "Gravar".
- Para excluir a gravação atual, clique no botão "Excluir".
- Para ouvir a gravação, clique no botão "Ouvir". Durante a reprodução, o botão se transformará em "Parar".
- Se desejar salvar a transcrição em texto do áudio gravado, clique no botão "Salvar".
- **Nota:** A funcionalidade "Whisper" está desativada neste momento e será implementada em futuras versões.

## Contribuindo

Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões para melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

# Desenvolvedor

| <img src="https://github.com/Calebe94.png?size=200" alt="Edimar Calebe Castanho"> |
|:---------------------------------------------------------------------------------:|
| [Edimar Calebe Castanho (Calebe94)](https://github.com/Calebe94)                  |

# Licença
All software is covered under [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
