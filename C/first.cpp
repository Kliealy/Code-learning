#include<cstdio>
//定义一个宏 建议大写 和普通变量区分开
#define PI 3.1415926

int main(int argc,char *argv[])
{
    float r=0.0f;//定义一个r变量 系统给r开辟4字节空间
    float area = 0.0f;//定义一个面积变量

    //获得半径 从键盘获得scan
    printf("请输入圆的半径r:");
    scanf("%f", &r);//带阻塞

    //算法:计算面积area = 3.14 * r * r
    area = PI*r*r;

    //将面积输出%.2f中的.2表示小数部分保留两位
    printf("area = %.2f\n",area);

    return 0;
}