//
//  server.cpp
//  server
//
//  Created by Stephen Andrzejewski on 2/3/18.
//  Copyright © 2018 Stephen Andrzejewski. All rights reserved.
//

#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>


int main(int argc, const char * argv[]) {
    
    struct sockaddr_in sin, cin;
    
    memset(&sin, 0, sizeof(sin));
    socklen_t cin_len = sizeof(cin);

    sin.sin_port = htons(10000);
    sin.sin_addr.s_addr = htonl(INADDR_ANY);
    sin.sin_family = AF_INET;
    sin.sin_len = sizeof(sin);
    
    int server = socket(AF_INET, SOCK_STREAM, 0);
    int bind_stat = bind(server, (struct sockaddr *) &sin, sin.sin_len);
    
    listen(server, 5);

    int client = accept(server, (struct sockaddr *) &cin, &cin_len);
    std::cout << "Connection from: " << inet_ntoa(cin.sin_addr) << " " << ntohs(cin.sin_port) << "\n";
    close(server);
    return 0;
}
