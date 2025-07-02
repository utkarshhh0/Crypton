#include <stdio.h>
#include <string.h>

// Encrypt text using Caesar cipher
void caesarEncrypt(char text[], int key) {
    for (int i = 0; text[i] != '\0'; i++) {
        char ch = text[i];
        if (ch >= 'a' && ch <= 'z') {
            text[i] = (ch - 'a' + key) % 26 + 'a';
        } else if (ch >= 'A' && ch <= 'Z') {
            text[i] = (ch - 'A' + key) % 26 + 'A';
        }
    }
}

// Decrypt Caesar cipher text
void caesarDecrypt(char text[], int key) {
    for (int i = 0; text[i] != '\0'; i++) {
        char ch = text[i];
        if (ch >= 'a' && ch <= 'z') {
            text[i] = (ch - 'a' - key + 26) % 26 + 'a';
        } else if (ch >= 'A' && ch <= 'Z') {
            text[i] = (ch - 'A' - key + 26) % 26 + 'A';
        }
    }
}

int main() {
    char text[100];
    int key;

    printf("Enter text: ");
    fgets(text, sizeof(text), stdin);
    text[strcspn(text, "\n")] = '\0'; // Remove newline

    printf("Enter key (shift value): ");
    scanf("%d", &key);

    // Encrypt the text
    caesarEncrypt(text, key);
    printf("Encrypted text: %s\n", text);

    // Decrypt the text
    caesarDecrypt(text, key);
    printf("Decrypted text: %s\n", text);

    return 0;
}