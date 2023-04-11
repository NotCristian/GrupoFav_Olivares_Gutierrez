#include <stdio.h>

int main(){

    int S;
    float FA,C;

    printf("Ingrese la cantidad de sonidos por minutos: ");
    scanf("%d",&S);

    FA = S/4 + 40;

    C = (FA - 32)*(5/9);

    printf("La temperatura en grados celsius es: %d",C);
    return 0;
}