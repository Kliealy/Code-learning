#include<cstdio>
//����һ���� �����д ����ͨ�������ֿ�
#define PI 3.1415926

int main(int argc,char *argv[])
{
    float r=0.0f;//����һ��r���� ϵͳ��r����4�ֽڿռ�
    float area = 0.0f;//����һ���������

    //��ð뾶 �Ӽ��̻��scan
    printf("������Բ�İ뾶r:");
    scanf("%f", &r);//������

    //�㷨:�������area = 3.14 * r * r
    area = PI*r*r;

    //��������%.2f�е�.2��ʾС�����ֱ�����λ
    printf("area = %.2f\n",area);

    return 0;
}