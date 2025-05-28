#include <stdio.h>
#include <string.h>
#include <wiringPi.h>
#include <linux/socket.h>
#include <linux/types.h>
#include <linux/unistd.h>
#include <arpa/inet.h>

#define PORT 9000

int main()
{
    struct sockaddr_in saddr;
    memset(&saddr, 0, sizeof(saddr));
    saddr.sin_family = AF_INET;
    saddr.sin_port = htons(PORT);
    saddr.sin_addr.s_addr = htons(INADDR_ANY); // 0 0 0 0

    int sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    int red_bind = bind(sock, (struct sockaddr *)&saddr, sizeof(saddr));

    listen(sock, 2);


    return 0;
}