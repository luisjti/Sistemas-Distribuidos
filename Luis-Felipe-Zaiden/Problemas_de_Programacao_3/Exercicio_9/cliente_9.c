# include <arpa/inet.h>
# include <stdio.h>
# include <string.h>
# include <sys/socket.h>
# include <unistd.h>
# include <stdlib.h>
# define PORT 5000

int main(int argc, char const * argv[]) {
int c_socket = 0, v_read, status_c;
struct sockaddr_in server_address;
char buffer[1024] = {0};
char dados[100] = {0};

c_socket = socket(AF_INET, SOCK_STREAM, 0);

server_address.sin_family = AF_INET;
server_address.sin_port = htons(PORT);
server_address.sin_addr.s_addr = INADDR_ANY;

status_c = connect(c_socket, (struct sockaddr *) & server_address, sizeof(server_address));
if (status_c == -1)
{
    printf("\nConexao falhou\n");
return -1;
}


int valor,naipe; 

printf("Digite o valor da carta: ");
scanf("%d", &valor);
printf("Digite o naipe da carta: ");
scanf("%d", &naipe);

sprintf(dados, "%d %d", valor,naipe);

send(c_socket, dados, strlen(dados), 0);

v_read = read(c_socket, buffer, 1024);

printf("%s" ,buffer);

close(status_c);
return 0;

}
