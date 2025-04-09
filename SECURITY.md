# Política de Segurança

Obrigado por ajudar a manter este projeto seguro! Esta política descreve como relatar vulnerabilidades de forma responsável.

## 🔐 Relatando Vulnerabilidades

Se você encontrar uma vulnerabilidade de segurança neste projeto, **não abra uma issue pública**. Em vez disso, envie um e-mail detalhado para:

📧 **[lordbelle7@gmail.com]**

Inclua o máximo de informações possível:
- Descrição da vulnerabilidade
- Passos para reproduzir
- Potencial impacto
- Possível correção (se houver)

Nos comprometemos a responder em até **5 dias úteis** e a corrigir problemas críticos o mais rápido possível.

---

## 🧱 Escopo

Este projeto utiliza as seguintes tecnologias e pacotes relevantes para segurança:
- **Flask**: framework web Python
- **yt-dlp**: ferramenta de download de vídeos
- **Whisper** e **Transformers**: bibliotecas de IA
- **Docker/Docker Compose**: isolamento e execução

Certifique-se de relatar falhas relacionadas à:
- Execução remota de código (RCE)
- Injeção de comandos ou SQL
- Quebra de isolamento entre containers
- Vazamento de arquivos sensíveis (áudios, resumos)
- Acesso não autorizado a rotas ou arquivos

---

## 🔒 Boas práticas internas

Para contribuidores:
- Nunca suba arquivos `.env`, credenciais ou chaves
- Nunca exponha `DEBUG=True` em produção
- Utilize HTTPS e CORS adequadamente em deploys reais
- Use `.dockerignore` para evitar vazamento de `.venv` e arquivos sensíveis
- Aplique validação de entrada em rotas que usam `url` ou upload de arquivos
- Não mexa no arquivo app.py ou transcript.py, pode comprometer o funcionamento do código.
- Proibido fazer commit na main sem autorização do dono.

---

## 🛡️ Proteções planejadas

Quando tiver mudanças planejadas vou colocar aqui, mas planejo treinar uma IA do zero para esse projeto.

---

## 🤝 Agradecimentos

Agradeço a Deus, Jesus Cristo, minha mãe e meu cachorro Tobias.
