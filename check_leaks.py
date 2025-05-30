import hashlib
import requests
import argparse

import sys
import re

def check_hibp(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Erro ao acessar Have I Been Pwned")
        return False

    hashes = (line.split(':') for line in response.text.splitlines())
    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            print(f"[HIBP] Senha encontrada! Vazamentos: {count}")
            return True
    print("[HIBP] Senha segura.")
    return False

def check_cybernews(email):
    url = "https://cybernews.com/wp-admin/admin-ajax.php"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://cybernews.com",
        "Referer": "https://cybernews.com/personal-data-leak-check/",
        "User-Agent": "Mozilla/5.0"
    }
    data = {
        "action": "leakCheckEmail",
        "email": email
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        content = response.text.lower()
        if "not found" in content:
            print("[Cybernews] Email NÃO encontrado em vazamentos.")
            return False
        elif "found" in content or "leaked" in content or "been found" in content:
            print("[Cybernews] Email encontrado em vazamentos!")
            return True
        else:
            print("[Cybernews] Resposta ambígua. Conteúdo:", content[:150])
            return False
    except Exception as e:
        print(f"[Cybernews] Erro: {e}")
        return False
def check_fsecure(email):
    url = "https://www.f-secure.com/en/home/free-tools/identity-theft-check"
    print("[F-Secure] ⚠️ Requer submissão de formulário com reCAPTCHA, não é possível via requests.")
    return False

def check_mozilla(email):
    session = requests.Session()
    url = f"https://monitor.mozilla.org/api/breaches/{email}"

    try:
        response = session.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200 and response.json():
            breaches = response.json()
            print(f"[Mozilla] Email encontrado em {len(breaches)} vazamentos.")
            return True
        elif response.status_code == 200:
            print("[Mozilla] Email NÃO encontrado em vazamentos.")
            return False
        else:
            print(f"[Mozilla] Código de resposta inesperado: {response.status_code}")
            return False
    except Exception as e:
        print(f"[Mozilla] Erro: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Verifica vazamentos de e-mail e senha.")
    parser.add_argument('--email', required=True, help='Email para verificar')
    parser.add_argument('--password', required=True, help='Senha para verificar')
    args = parser.parse_args()

    email = args.email
    password = args.password


    print(f"Verificando credenciais: {email} / {password}")
    print("== Iniciando verificação ==")
    check_hibp(password)
    check_cybernews(email)
    check_fsecure(email)
    check_mozilla(email)

if __name__ == "__main__":
    main()
