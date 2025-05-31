# 🔐 LeakChecker - Verificador de Vazamento de Credenciais

Projeto da disciplina **Cloud Security** – GS1 – FIAP  
Autor: Leonardo Adriano  
RM: 554563

# Usage
```
check_leaks.py <email> <password>
```
## 📘 Descrição

Este projeto tem como objetivo verificar se **usuários e senhas** foram vazados na internet, utilizando os seguintes serviços públicos:

- [Have I Been Pwned](https://haveibeenpwned.com/)
- [Mozilla Monitor](https://monitor.firefox.com/)
- [Cybernews Leaked Database](https://cybernews.com/personal-data-leak-check/)
- [F-Secure Identity Theft Checker](https://www.f-secure.com/en/identity-theft-checker)

O script é desenvolvido em **Python** e é executado em ambiente seguro via **Docker**.

---

### 📦 Build da imagem

Clone o repositório e acesse a pasta do projeto:

```bash
git clone https://github.com/seu-usuario/leakchecker.git
cd leakchecker
docker build -t leakchecker:latest .
