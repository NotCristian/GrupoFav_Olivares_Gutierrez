#include <stdio.h>

int main() {
    int CLA, CAT, ANT, RES = 0;
    float SAL;

    printf("Ingrese la clave del trabajador: ");
    scanf("%d", &CLA);

    printf("Ingrese la categoria del empleado (1-4): ");
    scanf("%d", &CAT);

    printf("Ingrese la antiguedad del trabajador en annos: ");
    scanf("%d", &ANT);

    printf("Ingrese el salario del trabajador: ");
    scanf("%f", &SAL);

    // Comprobación de las condiciones
    if ((CAT == 3 || CAT == 4) && ANT > 5) {
        RES = 1;
    } else if (CAT == 2 && ANT > 7) {
        RES = 1;
    }

    // Impresión de resultados
    if (RES == 1) {
        printf("El empleado con clave %d cumple con las condiciones.\n", CLA);
    } else {
        printf("El empleado con clave %d NO cumple con las condiciones.\n", CLA);
    }

    return 0;
}