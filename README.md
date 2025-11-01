# 🌍 Tour Extraction System

Sistema inteligente de extração automática de tarifários turísticos usando agentes IA.

**Desenvolvido por:** Grupo 287 - I2A2 Academy  
**Cliente:** iFriend (Marketplace de Turismo)

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

## 🎯 Problema

A iFriend recebe dezenas de catálogos turísticos em PDF mensalmente. O processo manual de extração leva 2-3 horas por catálogo e é propenso a erros.

## 💡 Solução

Sistema baseado em agentes inteligentes que automatiza 100% do processo:

- 🤖 **CrewAI** para orquestração de agentes
- 🧠 **GPT-4o-mini** para extração inteligente
- 📄 **Docling** para OCR e processamento de PDFs
- 🔍 **FAISS** para busca semântica
- 📊 **Streamlit** para interface web

## 📊 Resultados

- ✅ **294 tours** extraídos automaticamente
- ⚡ **92% redução** no tempo de processamento
- 💰 **$0.005** custo por PDF
- 🎯 **95%+** precisão validada

## 🚀 Demo Online

Acesse a interface web: [tour-extraction.streamlit.app](https://tour-extraction.streamlit.app)

## 💻 Rodar Localmente

### Pré-requisitos

- Python 3.9+
- OpenAI API Key ([obter aqui](https://platform.openai.com/api-keys))

### Instalação
```bash
# 1. Clonar repositório
git clone https://github.com/SEU_USUARIO/tour-extraction-system.git
cd tour-extraction-system

# 2. Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate  # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Configurar API Key
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Editar .streamlit/secrets.toml e adicionar sua chave
```

### Uso

**Opção A - Interface Web (Recomendado):**
```bash
streamlit run app_streamlit.py
```

Acesse: http://localhost:8501

**Opção B - Linha de Comando:**
```bash
python main.py --pdf "input/PRIVATE_TOURS_FRANCE_2024-EN.pdf"
```

Resultados salvos em: `output/results/`

## 📂 Estrutura do Projeto
```
tour-extraction-system/
├── app_streamlit.py          # Interface web
├── main.py                    # CLI
├── src/
│   ├── chunker/              # Processamento de PDFs
│   ├── indexer/              # Busca semântica
│   ├── extractor/            # Agentes de extração
│   └── exporter/             # Geração de resultados
├── config/
│   └── settings.yaml         # Configurações
├── input/                    # PDFs de entrada
├── output/
│   ├── chunks/               # PDFs processados
│   ├── index/                # Índices vetoriais
│   └── results/              # Resultados finais
└── docs/                     # Documentação adicional
```

## 🛠️ Tecnologias

| Categoria | Tecnologia | Versão |
|-----------|-----------|--------|
| Agentes | CrewAI | 0.28.0 |
| LLM | OpenAI GPT-4o-mini | API |
| OCR | Docling | 1.0+ |
| Busca | FAISS | 1.7.4 |
| Embeddings | Sentence Transformers | 2.3.1 |
| Interface | Streamlit | 1.29.0 |
| Visualização | Plotly | 5.18.0 |

## 📈 Arquitetura
```
┌─────────────────────────────────────┐
│     Interface Streamlit              │
├─────────────────────────────────────┤
│  1. PDF Chunker (Docling + OCR)     │
│  2. Semantic Indexer (FAISS)        │
│  3. Tour Extractor (CrewAI + GPT)   │
│  4. Result Exporter (JSON + Excel)  │
├─────────────────────────────────────┤
│     Armazenamento Local              │
└─────────────────────────────────────┘
```

## 🗺️ Roadmap

### Fase 1 - MVP ✅ (Atual)
- [x] Pipeline de extração funcional
- [x] Interface Streamlit
- [x] CLI operacional
- [x] Exportação multi-formato

### Fase 2 - Produção 🚧 (Próxima)
- [ ] Frontend moderno (Lovable/React)
- [ ] API REST (FastAPI)
- [ ] Workflows n8n
- [ ] Deploy em cloud
- [ ] Banco de dados
- [ ] Autenticação

### Fase 3 - Escala 📅 (Futuro)
- [ ] Multi-tenancy
- [ ] Analytics avançado
- [ ] ML para melhorias
- [ ] Mobile app

## 👥 Equipe

**Grupo 287 - I2A2 Academy:**
- Bruno Leão
- Victor Hugo
- Jander Alves
- Gleice Kelly
- Wagner Lemos

## 📄 Licença

Este projeto foi desenvolvido como trabalho acadêmico para o curso "Agentes Autônomos com Redes Generativas" da I2A2 Academy.

## 🙏 Agradecimentos

- I2A2 Academy pela formação
- iFriend pelo caso real
- Comunidade CrewAI
- OpenAI pela API

## 📞 Contato

Para dúvidas ou sugestões, abra uma [issue](https://github.com/SEU_USUARIO/tour-extraction-system/issues).

---

**⭐ Se este projeto foi útil, considere dar uma estrela no GitHub!**
