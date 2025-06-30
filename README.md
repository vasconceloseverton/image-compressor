
# 🖼️ ImageCompressor GUI (Python)

**ImageCompressor** é uma aplicação desktop moderna desenvolvida em **Python**, com arquitetura **MVC** e interface visual criada com `customtkinter`. O objetivo principal é permitir a compressão e redimensionamento de imagens `.jpg` e `.jpeg`, ideal para uso em páginas web ou arquivos otimizados.

---

## 🚀 Funcionalidades

- 📂 Seleção de pasta de entrada e saída via interface gráfica.
- ⚙️ Compressão de imagens com controle de **qualidade**.
- 📏 Redimensionamento automático com **manutenção de proporção** (largura e altura máximas configuráveis).
- 📊 **Barra de progresso** em tempo real.
- 🌙 Interface **moderna e responsiva** com `customtkinter`.
- 🧠 Arquitetura **MVC** para melhor organização e manutenção do código.

---

## 📸 Exemplos de Uso

https://github.com/vasconceloseverton/image-compressor/blob/main/TELA.png

### 1. Interface Principal

- Escolha a pasta com imagens de entrada.
- Escolha onde salvar as imagens comprimidas.
- Ajuste a qualidade e as dimensões máximas.
- Clique em "Iniciar Compressão".

A barra de progresso exibirá o andamento do processo.

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)

---

## 📁 Estrutura de Pastas

```
image_compressor/
├── controller/
│   └── compressor_controller.py
├── model/
│   └── image_compressor.py
├── view/
│   └── main_view.py
├── main.py
├── requirements.txt
└── README.md

```

---

## ⚙️ Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/vasconceloseverton/image-compressor.git
cd image-compressor
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

> **requirements.txt**
> ```txt
> customtkinter
> pillow
> ```

### 3. Execute o programa

```bash
python main.py
```

---

## 📦 Gerar Executável (.exe)

Se quiser gerar um `.exe`, instale o PyInstaller:

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed main.py
```

O executável será gerado na pasta `dist/`.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Desenvolvido por **Everton Vasconcelos**.  

