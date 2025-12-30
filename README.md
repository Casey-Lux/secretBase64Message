# secret.py

Herramienta simple y directa para cifrar y descifrar **strings o archivos** usando una contraseña, con salida en **Base64**.

El cifrado es real (**AES** vía `cryptography`).
Base64 se usa únicamente para transporte.

---

## Requisitos

- Python **3.8+** (recomendado 3.10 o superior)
- `pip` operativo

Verificación rápida:

```bash
python --version
pip --version
```

---

## Instalación de dependencias

### Linux

(Opcional pero recomendado: entorno virtual)

```bash
python -m venv venv
source venv/bin/activate
pip install cryptography
```

Si hay errores compilando dependencias:

#### Debian / Ubuntu

```bash
sudo apt install build-essential libssl-dev
```

#### Arch Linux

```bash
sudo pacman -S base-devel openssl
```

---

### Windows

Instala Python desde:

https://www.python.org

(Marca **Add Python to PATH**)

Entorno virtual (opcional):

```bat
python -m venv venv
venv\Scripts\activate
```

Instala la dependencia:

```bat
pip install cryptography
```

Verificación:

```bash
python -c "from cryptography.fernet import Fernet; print('OK')"
```

---

## Uso

### Cifrar una cadena

```bash
python secret.py -c -p 1234 -s "mensaje secreto"
```

Salida: string cifrado en Base64.

---

### Descifrar una cadena

```bash
python secret.py -d -p 1234 -s "<BASE64>"
```

---

### Cifrar un archivo

```bash
python secret.py -c -p 1234 -s documento.txt
```

Genera:

```text
documento.txt.secret
```

---

### Descifrar un archivo

```bash
python secret.py -d -p 1234 -s documento.txt.secret
```

Restaura:

```text
documento.txt
```

---

## Notas importantes

- Base64 **no es cifrado**, solo codificación.
- La seguridad depende **completamente de la contraseña**.
- Si pierdes la contraseña, **no hay recuperación**.
- Pensado para simplicidad, claridad y control.
- No es para custodiar secretos críticos.

---

## Posibles mejoras futuras

- KDF más robusto (PBKDF2 / scrypt)
- Soporte stdin / stdout (pipes Unix)
- Manejo explícito de binarios
- Empaquetado como ejecutable

---

