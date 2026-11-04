#include <stdio.h>
#include <string.h>
#include <ctype.h>

void hill_encrypt(char *text, int key[2][2]) {
    char clean_text[256] = "";
    int len = 0, i, j;

    // Filter non-alphabetic characters and convert to uppercase
    for (i = 0; text[i] != '\0'; i++) {
        if (isalpha(text[i])) {
            clean_text[len++] = toupper(text[i]);
        }
    }
    clean_text[len] = '\0';

    // Pad with 'X' if length is odd
    if (len % 2 != 0) {
        clean_text[len] = 'X';
        clean_text[len + 1] = '\0';
        len++;
    }

    printf("Filtered & Padded Plaintext: %s\n", clean_text);
    printf("Encrypted: ");

    // Matrix multiplication
    for (i = 0; i < len; i += 2) {
        int p1 = clean_text[i] - 'A';
        int p2 = clean_text[i + 1] - 'A';

        int c1 = (key[0][0] * p1 + key[0][1] * p2) % 26;
        int c2 = (key[1][0] * p1 + key[1][1] * p2) % 26;

        printf("%c%c", c1 + 'A', c2 + 'A');
    }
    printf("\n");
}

int main() {
    char text[256];
    int key[2][2];

    printf("Enter the plaintext: ");
    fgets(text, sizeof(text), stdin);
    text[strcspn(text, "\n")] = 0; // Remove newline

    printf("Enter 2x2 key matrix elements (e.g., 3 3 2 5):\n");
    scanf("%d %d %d %d", &key[0][0], &key[0][1], &key[1][0], &key[1][1]);

    hill_encrypt(text, key);
    return 0;
}