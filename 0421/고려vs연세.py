import random

x = random.randint(0,1)
string = "Korea" if x > 0.5 else "Yonsei"
print(string)




##############################################################

# C


#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // 1. 실행할 때마다 다른 난수가 나오도록 시드 설정
    srand(time(NULL));

    const int minVal = 0;
    const int maxVal = 1;
    
    // 2. 0 또는 1의 난수 생성
    // rand() % (max - min + 1) + min 공식 사용
    int myTime = rand() % (maxVal - minVal + 1) + minVal;

    // 3. 결과 결정 및 출력
    // C언어에서는 문자열을 다룰 때 char 포인터를 사용합니다.
    char* result = "Korea";

    if (myTime % 2 == 0) {
        result = "Yonsei";
    }

    printf("%s", result);

    return 0;
}

###############################################################################


#JAVA11

public class Main {
    public static void main(String[] args) throws Exception {

        final int minVal = 0;
        final int maxVal = 1;
        int myTime = minVal + (int) (Math.random() * ((maxVal - minVal) + 1));

        String result = "Korea";
        if (myTime % 2 == 0) {
            result = "Yonsei";
        }
        System.out.print(result);
    }
}