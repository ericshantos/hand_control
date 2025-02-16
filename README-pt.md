[🇬🇧] Read in Englidh

# Controle por Gestos

<div>
<img src="https://img.shields.io/badge/pre--commit-verified-blue?logo=pre-commit" alt="pre-commit habilitado" />
<img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" alt="python 3.12 utilizado" />
<img src="https://img.shields.io/badge/Status-Active-success" alt="projeto concluído" />
<img src="https://img.shields.io/badge/Dependencies-Managed-blue" alt="Dependências gerenciadas" />
</div>

## Descrição

O projeto **Controle por Gestos** é uma aplicação que permite controlar o volume do sistema e o brilho da tela usando gestos manuais capturados por uma câmera. Ele utiliza a biblioteca **MediaPipe** para rastreamento das mãos e calcula a distância entre os dedos para ajustar as propriedades do sistema.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **OpenCV**: Captura e processamento de imagens.
- **MediaPipe**: Detecção e rastreamento das mãos.
- **Pycaw**: Controle do volume do sistema (somente para Windows).
- **screen_brightness_control**: Ajuste do brilho da tela.

## Funcionalidades

- Detecção de mãos em tempo real.
- Cálculo da distância entre o polegar e o indicador.
- Ajuste do volume do sistema ao detectar a mão esquerda.
- Ajuste do brilho da tela ao detectar a mão direita.
- Exibição das mãos processadas na tela.

## Estrutura do Projeto

```
Controle por Gestos/
│-- src/
│   │-- controllers/
│   │   │-- brightness.py
│   │   │-- volume.py
│   │   │-- controller.py
│   │-- utils/
│   │   │-- distance_calculator.py
│   │-- hand_tracker/
│   │   │-- initialize_detector.py
│   │   │-- landmark_processor.py
│-- main.py
│-- pre-commit-config.yaml
│-- setup.py
│-- .gitignore
│-- requirements.txt
│-- README.md
```

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/ericshantos/hand-control.git
   cd hand-control
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o pre-commit:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

5. Para testar o pre-commit manualmente:
   ```bash
   pre-commit run --all-files
   ```

6. Execute o script principal:
   ```bash
   python main.py
   ```

## Autor

Desenvolvido por **Eric dos Santos**.

- GitHub: [github.com/ericshantos](https://github.com/ericshantos)
- LinkedIn: [linkedin.com/in/eric-sh](https://linkedin.com/in/eric-sh)
- E-mail: ericshantos13@gmail.com

## Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
