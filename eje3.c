#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void prBinario();

int main(){
    int var[256];
    srand(time(NULL));
        
    for(i=0;i<256;i++){
        var[i] = rand()%255;
        prBinario(var[i]);        
    }

    
}

void prBinario(int var){

int aux,bin[8];

for(i=7;i==0;i--){
    bin[i] = var%2;
    var = var/2;
}

for(i=0;i<8;i++){
    printf("%d",bin[i]);
}
}