#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

struct Edge_data{
    uint16_t m;
    uint16_t r; //target vertice
};

struct Edge{
    uint16_t l;
    uint16_t m;
    uint16_t r;
};

const uint16_t VERTICES = 10001; 


bool DFS(vector<Edge_data *> *graph, uint16_t vertice, bool *visited, uint32_t depth, vector<Edge*> *result){
    visited[vertice] = true;
    for (auto edge : graph[vertice]){
        if(edge->r == 0){
            printf("%u\n", depth);
            Edge *n_edge = new Edge;
            n_edge->l = vertice;
            n_edge->m = edge->m;
            n_edge->r = edge->r;
            result->push_back(n_edge);
            return true;
        }
        if(!visited[edge->r] && DFS(graph, edge->r, visited, depth+1, result)){
            Edge *n_edge = new Edge;
            n_edge->l = vertice;
            n_edge->m = edge->m;
            n_edge->r = edge->r;
            result->push_back(n_edge);
            return true;
        }
        
    }
    return false;
}

int main(){

    vector<Edge_data *> vertices[VERTICES];
    vector<Edge*> result;    
    bool visited[VERTICES] = {0};
    //
    //READ N
    //
    uint32_t n;
    int sc_catch = scanf("%u", &n);
    
    if(sc_catch == 0){
        return 0;
    }
    //
    //READ INPUT
    //
    bool exist_edge_to_zero = false;
    bool exist_edge_from_zero = false;
    for(uint32_t i = 0; i < n; i++){
        uint16_t l,m,r;
        sc_catch = scanf("%hu %hu %hu", &l, &m, &r);
        if (sc_catch == 0){
            return 0;
        }

        if(r == 0) exist_edge_to_zero = true;
        if(l == 0) exist_edge_from_zero = true;
        
        Edge_data *data = new Edge_data;
        data->m = m;
        data->r = r;
        vertices[l].push_back(data);
    }
    if(exist_edge_from_zero && exist_edge_to_zero){
        if(DFS(vertices, 0, visited, 1, &result)){
            while(!result.empty()){
                Edge * e = result.back();
                result.pop_back();
                printf("%hu %hu %hu\n", e->l, e->m, e->r);
            }
        }
        else{
            printf("BRAK");
        }
    }
    else{
        printf("BRAK");
    }


    //CLEAN MEMORY
    for(auto p : result){
        delete p;
    }
    result.clear();

    for(uint16_t i = 0; i < VERTICES; i++){
        
        for (auto p : vertices[i]){
            delete p;    
        }
        vertices[i].clear();
    }
    

    return 0;
}