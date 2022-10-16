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


float saldo_medio;

printf("Digite o saldo medio: ");
scanf("%f", &saldo_medio);

sprintf(dados, "%.2f", saldo_medio);

send(c_socket, dados, strlen(dados), 0);

v_read = read(c_socket, buffer, 1024);

printf("O saldo medio e: %.2f\nO valor do credito e : %.2f\n" ,saldo_medio,atof(buffer));

close(status_c);
return 0;
}
