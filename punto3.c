#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 1024

int contar_ocurrencias(FILE *archivo, const char *palabra) {
    char linea[MAX_LINE];
    int conteo = 0;
    size_t len = strlen(palabra);

    while (fgets(linea, MAX_LINE, archivo)) {
        char *ptr = linea;
        while ((ptr = strstr(ptr, palabra)) != NULL) {
            conteo++;
            ptr += len;
        }
    }
    return conteo;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Uso: %s archivo palabra\n", argv[0]);
        return 1;
    }

    FILE *archivo = fopen(argv[1], "r");
    if (!archivo) {
        perror("Error al abrir el archivo");
        return 1;
    }

    int resultado = contar_ocurrencias(archivo, argv[2]);
    fclose(archivo);

    printf("'%s' se repite %d veces en el texto.\n", argv[2], resultado);
    return 0;
}
