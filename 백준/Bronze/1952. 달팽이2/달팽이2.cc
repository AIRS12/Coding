//
//  BOJ1952_달팽이2.cpp
//  Coding_Test_Practice
//
//  Created by greena on 2023/06/23
//  

#include <iostream>

using namespace std;

int M, N;
int x, y, dir, cnt = 0;
bool visited[100][100];

int dy[4] = {1,0,-1,0};
int dx[4] = {0,1,0,-1};

int main(){
    cin >> M >> N;
    visited[0][0] = 1;
    while(1){
        int next_x = x + dx[dir];
        int next_y = y + dy[dir];

        if (next_x < 0 || next_y < 0 || next_x >= M || next_y >= N || visited[next_x][next_y] ){
            dir = (dir + 1) % 4;
            next_x = x + dx[dir];
            next_y = y + dy[dir];
            if(visited[next_x][next_y])   break;
            cnt++;
        }
        visited[next_x][next_y] = 1;
        x = next_x;
        y = next_y;
    }
    cout << cnt;
    return 0;
}
