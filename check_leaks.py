import hashlib
import requests
import sys
import time

def check_hibp(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Erro ao acessar Have I Been Pwned (senhas)")
        return False

    hashes = (line.split(':') for line in response.text.splitlines())
    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            print(f"[HIBP] Senha encontrada! Vazamentos: {count}")
            return True
    print("[HIBP] Senha segura.")
    return False

def check_hibp_email_simulado(email):
    print(f"[HIBP-EMAIL] 🔍 Verificando e-mail: {email}")
    # Simulação com base no nome do e-mail
    if "@" in email.lower() or "123" in email:
        print(f"[HIBP-EMAIL] ⚠️ E-mail {email} encontrado em 3 vazamentos simulados:")
        print(" - LinkedIn (2016)")
        print(" - MySpace (2013)")
        print(" - Adobe (2013)")
        return True
    else:
        print(f"[HIBP-EMAIL] ✅ E-mail {email} não encontrado em vazamentos simulados.")
        return False

def check_cybernews(email):
    print("[Cybernews] ⚠️ Verificação simulada. Requer browser/headless ou CAPTCHA.")
    return False

def check_fsecure(email):
    print("[F-Secure] ⚠️ Verificação simulada. Requer interação humana (CAPTCHA/email).")
    return False

def check_mozilla(email):
    print("[Mozilla Monitor] ⚠️ Verificação simulada. Requer criação de conta/email.")
    return False

def main():
    if len(sys.argv) != 3:
        print("Uso: python check_leaks.py <email> <senha>")
        sys.exit(1)

    email = sys.argv[1]
    password = sys.argv[2]

    print(f"Verificando credenciais: {email} / {password}")
    print("== Iniciando verificação ==")
    check_hibp_email_simulado(email)
    check_hibp(password)
    check_cybernews(email)
    check_fsecure(email)
    check_mozilla(email)

if __name__ == "__main__":
    main()
