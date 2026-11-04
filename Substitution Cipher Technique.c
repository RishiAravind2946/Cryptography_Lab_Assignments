#include <stdio.h>
#include <string.h>
#include <ctype.h>

void substitutionCipher(char text[], int key) {
    int i;
    char ch;
    
    for (i = 0; text[i] != '\0'; ++i) {
        ch = text[i];
        
        // Encrypt uppercase characters
        if (isupper(ch)) {
            ch = (ch + key - 'A') % 26 + 'A';
            text[i] = ch;
        }
        // Encrypt lowercase characters
        else if (islower(ch)) {
            ch = (ch + key - 'a') % 26 + 'a';
            text[i] = ch;
        }
        // Non-alphabetic characters remain unchanged
    }
}

int main() {
    char text[100];
    int key;
    
    printf("Enter the plain text: ");
    fgets(text, sizeof(text), stdin);
    
    // Remove newline character read by fgets
    text[strcspn(text, "\n")] = 0;
    
    printf("Enter the integer key (n): ");
    scanf("%d", &key);
    
    // Handle negative keys by converting them to positive equivalents
    if (key < 0) {
        key = (key % 26) + 26;
    }
    
    substitutionCipher(text, key);
    
    printf("Cipher Text: %s\n", text);
    
    return 0;
}