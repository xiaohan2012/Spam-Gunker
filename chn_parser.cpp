#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string.h>
#include "ICTCLAS50.h"


int main(int argc, char* argv[])
{
    if(!ICTCLAS_Init()) 
	{
		printf("Init fails\n");
		return -1;
	}
	unsigned int len_max = 128;
    unsigned int current_size = 0;
 
    char * sSentence = (char *)malloc(len_max);
    current_size = len_max;    


    if(sSentence != NULL){
        int c = EOF;
        unsigned int i =0;
            //accept user input until hit enter or end of file
        while (( c = getchar() ) != '\n' && c != EOF)
        {
            sSentence[i++]=(char)c;
     
            //if i reached maximize size then realloc size
            if(i == current_size)
            {
                            current_size = i+len_max;
                sSentence = (char *)realloc(sSentence, current_size);
            }
        }
     
        sSentence[i] = '\0';
     
    }
	int nPaLen=strlen(sSentence);
	char* sRst=0;//用户自行分配空间，用于保存结果；
	sRst=(char *)malloc(nPaLen*6);//建议长度为字符串长度的6倍。
	int nRstLen=0;		
	nRstLen=ICTCLAS_ParagraphProcess(sSentence,nPaLen, sRst,CODE_TYPE_UTF8,1);
	printf("%s",sRst);
	ICTCLAS_Exit();
	return 0;  
 }
