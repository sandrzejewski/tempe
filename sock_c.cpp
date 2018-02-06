//
//  main.cpp
//  client
//
//  Created by Stephen Andrzejewski on 2/4/18.
//  Copyright © 2018 Stephen Andrzejewski. All rights reserved.
//

#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>


int main(int argc, const char * argv[]) {
    // insert code here...
    int port = 10000;

    struct sockaddr_in sin;

    memset(&sin, 0, sizeof(sin));
    
    sin.sin_family = AF_INET;
    sin.sin_port = htons(port);
    sin.sin_addr.s_addr = inet_addr("127.0.0.1");

    int server = socket(AF_INET, SOCK_STREAM, 0);
    int client = connect(server, (struct sockaddr *) &sin, sizeof(sin));

    std::string buffer;
    
    std::cout << client << "\n";
    
    recv(server, (void *) &buffer, 1024, 0);
    std::cout << buffer << "\n";
    
    return 0;
}
