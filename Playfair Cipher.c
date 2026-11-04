#include <stdio.h>
#include <string.h>
#include <ctype.h>

char matrix[5][5];

void generate_matrix(char *key) {
    int alpha[26] = {0};
    int r = 0, c = 0, i;
    alpha['J' - 'A'] = 1; // Treat J as I

    for (i = 0; key[i] != '\0'; i++) {
        if (isalpha(key[i])) {
            char ch = toupper(key[i]);
            if (ch == 'J') ch = 'I';
            if (alpha[ch - 'A'] == 0) {
                matrix[r][c++] = ch;
                alpha[ch - 'A'] = 1;
                if (c == 5) { c = 0; r++; }
            }
        }
    }
    for (i = 0; i < 26; i++) {
        if (alpha[i] == 0) {
            matrix[r][c++] = i + 'A';
            if (c == 5) { c = 0; r++; }
        }
    }
}

void find_pos(char ch, int *row, int *col) {
    int r, c; /* Declared outside the loop for strict compiler compatibility */
    if (ch == 'J') ch = 'I';
    for (r = 0; r < 5; r++) {
        for (c = 0; c < 5; c++) {
            if (matrix[r][c] == ch) {
                *row = r; 
                *col = c; 
                return;
            }
        }
    }
}

void playfair_encrypt(char *text) {
    char prep[512] = "";
    int len = 0, i;

    // Filter non-alphas and handle duplicates
    for (i = 0; text[i] != '\0'; i++) {
        if (isalpha(text[i])) {
            char ch = toupper(text[i]);
            if (ch == 'J') ch = 'I';
            
            if (len > 0 && len % 2 != 0 && prep[len-1] == ch) {
                prep[len++] = 'X'; // insert X for duplicates
            }
            prep[len++] = ch;
        }
    }
    if (len % 2 != 0) prep[len++] = 'X';
    prep[len] = '\0';
    
    printf("Prepared Text: %s\n", prep);
    printf("Encrypted: ");

    for (i = 0; i < len; i += 2) {
        int r1 = 0, c1 = 0, r2 = 0, c2 = 0;
        find_pos(prep[i], &r1, &c1);
        find_pos(prep[i+1], &r2, &c2);

        if (r1 == r2) {
            printf("%c%c", matrix[r1][(c1+1)%5], matrix[r2][(c2+1)%5]);
        } else if (c1 == c2) {
            printf("%c%c", matrix[(r1+1)%5][c1], matrix[(r2+1)%5][c2]);
        } else {
            printf("%c%c", matrix[r1][c2], matrix[r2][c1]);
        }
    }
    printf("\n");
}

int main() {
    char text[256], key[256];

    printf("Enter the keyword: ");
    fgets(key, sizeof(key), stdin);
    key[strcspn(key, "\n")] = 0;

    printf("Enter the plaintext: ");
    fgets(text, sizeof(text), stdin);
    text[strcspn(text, "\n")] = 0;

    generate_matrix(key);
    playfair_encrypt(text);
    return 0;
}