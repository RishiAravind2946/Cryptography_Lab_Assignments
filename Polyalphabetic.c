#include <stdio.h>
#include <string.h>
#include <ctype.h>

void vigenere_encrypt(char *text, char *key) {
    int text_len = strlen(text);
    int key_len = strlen(key);
    int i, j = 0;

    // Convert key to uppercase
    for (i = 0; i < key_len; i++) {
        key[i] = toupper(key[i]);
    }

    printf("Encrypted: ");
    for (i = 0; i < text_len; i++) {
        if (isalpha(text[i])) {
            char base = isupper(text[i]) ? 'A' : 'a';
            int p = text[i] - base;
            int k = key[j % key_len] - 'A';
            
            char encrypted_char = ((p + k) % 26) + base;
            printf("%c", encrypted_char);
            j++; // Only advance key index on alphabetic characters
        } else {
            // Preserve spaces, numbers, and special characters
            printf("%c", text[i]);
        }
    }
    printf("\n");
}

int main() {
    char text[256], key[256];

    printf("Enter the plaintext: ");
    fgets(text, sizeof(text), stdin);
    text[strcspn(text, "\n")] = 0;

    printf("Enter the keyword: ");
    fgets(key, sizeof(key), stdin);
    key[strcspn(key, "\n")] = 0;

    vigenere_encrypt(text, key);
    return 0;
}