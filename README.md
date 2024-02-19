# Vocalize

O Vocalize é uma ferramenta simples desenvolvida em Python para gravar voz e transformá-la em texto. Esta ferramenta foi criada para facilitar a captura de áudio e sua posterior transcrição em texto.

Oferece uma interface gráfica intuitiva para gravar áudio, excluir gravações, ouvir o áudio gravado e salvar a transcrição em texto resultante.

## Dependências

Ele utiliza o módulo `arecord` para gravação de áudio e `aplay` para reprodução de áudio no sistema.

### Instalando através do código fonte

Clone o repositório:

``` sh
git clone https://github.com/calebe94/vocalize
```

Entre no diretório criado:

``` sh
cd vocalize/
```

E rode o seguinte comando:

``` sh
pip install .
```

## Buildando o pacote

Se você está contribuindo com o projeto e vai testar a distribuição do pacote, siga os seguintes passos:

Com o repositório já clonado e no diretório raiz do projeto, crie um ambiente virtual Python:

```sh
virtualenv venv
source venv/bin/activate
```

Instale o pacote `build`:

```sh
pip install --upgrade build
```

Agora rode o comando a seguir na pasta raiz do projeto:

```sh
$ python3 -m build
```

Agora para instalar o `vocalize` através do pacote gerado, basta rodar o seguinte comando:

``` sh
pip install dist/vocalize_*.tar.gz
```

## Uso

- Ao iniciar o aplicativo, você verá uma interface gráfica com opções para gravar, excluir, ouvir e salvar o áudio.
- Clique no botão "Gravar" para iniciar a gravação. O botão se transformará em "Pausar" durante a gravação.
- Você pode pausar a gravação a qualquer momento clicando novamente no botão "Gravar".
- Para excluir a gravação atual, clique no botão "Excluir".
- Para ouvir a gravação, clique no botão "Ouvir". Durante a reprodução, o botão se transformará em "Parar".
- Se desejar salvar a transcrição em texto do áudio gravado, clique no botão "Transcrever".

## Contribuindo

Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões para melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

# Desenvolvedor

| <img src="https://github.com/Calebe94.png?size=200" alt="Edimar Calebe Castanho"> |
|:---------------------------------------------------------------------------------:|
| [Edimar Calebe Castanho (Calebe94)](https://github.com/Calebe94)                  |

# Licença
All software is covered under [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
