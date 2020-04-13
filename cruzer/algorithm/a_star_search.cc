// Copyright 2020 - Present Aaron Ma.
// All Rights Reserved.
// This file is part of Canary, an open-source flying car for everyone!
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
// #include "spec/test_a_star_search.h"
// TODO(aaronhma): Can we make this in general for all compilers?
#include <math> // NOTE: In some compilers, this might differ, this currently works on Mac and Linux, but not all Windows

using namespace std;

enum States {
  kStart,
  kPath,
  kEmpty,
  kObstacle,
  kGoal
};

void PrintBoard(vector<vector<int>> board) {
  for (auto outer : board) { // Outer board
    for (int i : outer) { // Inner loop
      cout << i << " ";
    }
    cout << "\n" << endl;
  }
}

void ReadBoard(string file) {
  int num;
  char comma;
  // while(cin >> num >> comma) {}
}

void PrintState(vector<vector<int>> board) {
  auto state;
  switch (board):
    case 0:
      state = States::kEmpty;
      break;
    case 1:
      state = States::kObstacle;
      break;
    case 2:
      state = States::kPath;
      break;
    case 3:
      state = States::kStart;
    case 4:
      state = States::kGoal;
    default:
      state = nullptr;
}

vector<vector<int>> AddNeighbors() {
  vector<vector<int>> open_list = {};
  return open_list;
}

void AStarSearch() {
  AddNeighbors();
  
  // while (parent -> node) {}
}

int main() {
  string sep = "======================================================================";
  cout << sep << endl;
  // Test()
  cout << sep << endl;
}
