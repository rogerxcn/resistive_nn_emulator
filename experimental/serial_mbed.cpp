#include "mbed.h"

Serial pc(USBTX, USBRX); // tx, rx

int main() {
    int j = 0;
    
    char arr[28*28*10];
    
    while(1) {
        if (j >= 28*28*10) break;
        
        char c = pc.getc();
        
        if (c == 'A') break;
        
        arr[j] = c;
        j++;
    }
    
    arr[++j] = '\0';
    
    j = 0;
    
    while(arr[j] != '\0') {
        pc.putc(arr[j]);
        j++;
    }
    
    pc.putc('F');
    
}