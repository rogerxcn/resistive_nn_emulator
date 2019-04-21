#include "mbed.h"

DigitalOut out1(PA_3);
DigitalOut out2(PC_0);
DigitalOut out3(PC_3);
DigitalOut out4(PF_3);
DigitalOut out5(PF_5);
DigitalOut out6(PF_10);
DigitalOut out7(PF_2);
//DigitalOut out8();

DigitalOut out9(PH_1);
DigitalOut out10(PH_0);
DigitalOut out11(PD_0);
DigitalOut out12(PD_1);
DigitalOut out13(PG_0);
//DigitalOut out14();
DigitalOut out15(PD_7);
//DigitalOut out16();

//DigitalOut out17();
DigitalOut out18(PD_6);
DigitalOut out19(PD_5);
DigitalOut out20(PD_4);
DigitalOut out21(PD_3);
DigitalOut out22(PE_2);
DigitalOut out23(PE_4);
DigitalOut out24(PE_5);

DigitalOut out25(PE_6);
//DigitalOut out26();
DigitalOut out27(PE_3);
DigitalOut out28(PF_8);
DigitalOut out29(PF_7);
DigitalOut out30(PF_9);
//DigitalOut out31();
DigitalOut out32(PG_1);

DigitalOut out33(PB_1);
DigitalOut out34(PC_2);
DigitalOut out35(PF_4);
//DigitalOut out36();
//DigitalOut out37();
//DigitalOut out38();
DigitalOut out39(PB_6);
DigitalOut out40(PB_2);

//DigitalOut out41();
DigitalOut out42(PD_13);
DigitalOut out43(PD_12);
DigitalOut out44(PD_11);
DigitalOut out45(PE_2);
DigitalOut out46(PA_0);
DigitalOut out47(PE_0);
//DigitalOut out48();

DigitalOut out49(PF_13);
//DigitalOut out50();
DigitalOut out51(PE_9);
DigitalOut out52(PE_11);
DigitalOut out53(PF_14);
DigitalOut out54(PE_13);
//DigitalOut out55();
DigitalOut out56(PF_15);

//DigitalOut out57();
DigitalOut out58(PG_14);
DigitalOut out59(PG_9);
DigitalOut out60(PE_8);
//DigitalOut out61();
DigitalOut out62(PE_7);
//DigitalOut out63();
DigitalOut out64(PE_10);

int main() {
    while(1) {
        out1 = 0;
        out2 = 0;
        out3 = 0;
        out4 = 1;
        out5 = 0;
        out6 = 0;
        out7 = 1;
        //out8 = 0; // skip

        out9 = 0;
        out10 = 0;
        out11 = 0;
        out12 = 0;
        out13 = 0;
        //out14 = 0; // skip
        out15 = 0;
        //out16 = 0; // skip

        //out17 = 0; // skip
        out18 = 0;
        out19 = 0;
        out20 = 0;
        out21 = 1;
        out22 = 0;
        out23 = 0;
        out24 = 0;

        out25 = 0;
        //out26 = 0; // skip
        out27 = 0;
        out28 = 0;
        out29 = 0;
        out30 = 0;
        //out31 = 0; // skip
        out32 = 1;

        out33 = 0;
        out34 = 0;
        out35 = 0;
        //out36 = 0; // skip
        //out37 = 1; // skip
        //out38 = 0; // skip
        out39 = 1;
        out40 = 0;

        //out41 = 1; // skip
        out42 = 0;
        out43 = 0;
        out44 = 1;
        out45 = 1;
        out46 = 0;
        out47 = 1;
        //out48 = 1; // skip

        out49 = 0;
        //out50 = 0; // skip
        out51 = 0;
        out52 = 1;
        out53 = 1;
        out54 = 0;
        //out55 = 1; // skip
        out56 = 1;

        //out57 = 0; // skip
        out58 = 0;
        out59 = 0;
        out60 = 0;
        //out61 = 0; // skip
        out62 = 0;
        //out63 = 1; // skip
        out64 = 0;
    }
}
