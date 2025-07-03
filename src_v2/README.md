# 🔐 Crypton v2 — Multi-Cipher Crypting.

**Crypton v2** is a levelled-up terminal-based cryptography tool that supports **three classic encryption techniques**: Caesar, XOR, and Vigenère. Upgraded in Python, this version focuses on clarity, modularity, and giving users the power to explore symmetric encryption in its rawest form.

---

## ⚙️ Features

- ✅ Caesar cipher (shift-based substitution)
- ✅ XOR cipher (bitwise symmetric encryption)
- ✅ Vigenère cipher (polyalphabetic keyword-based encryption)
- ✅ Encrypt & decrypt through a simple terminal menu
- ✅ Supports uppercase and lowercase letters, preserves symbols
- ✅ Clean code structure with modular functions

---

## 🧪 Example Usage

```text
=== Crypton v2 (Caesar · XOR · Vigenère) ===

1) Caesar Encrypt
2) Caesar Decrypt
3) XOR Encrypt/Decrypt
4) Vigenère Encrypt
5) Vigenère Decrypt
0) Exit

Choice: 1
Enter text: HelloWorld
Enter shift (int): 9
Encrypted: QnuuxFxaum

Choice: 2
Enter text: QnuuxFxaum
Enter shift (int): 9
Decrypted: HelloWorld

Choice: 3
Enter text: HelloWorld
Enter XOR key (int 0‑255): 33
Result: iDMMNvNSME

Choice: 3
Enter text: iDMMNvNSME
Enter XOR key (int 0‑255): 33
Result: HelloWorld

Choice: 4
Enter text: HelloWorld
Enter keyword (letters only): password
Result: WeddkKfuad

Choice: 5
Enter text: WeddkKfuad
Enter keyword (letters only): password
Result: HelloWorld