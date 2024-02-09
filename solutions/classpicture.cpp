/*
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://eclass.srv.ualberta.ca/pluginfile.php/7925875/mod_resource/content/2/paintings.cpp

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
*/

#include <bits/stdc++.h>

using namespace std;
int perm[10], output[10], n, m, o, S;
bool used[10], conflict[10][10];


int search(int plen) {
  if (plen == n) {
    // if this is our first valid permutation, save it
    if (output[0] == -1) memcpy(output, perm, sizeof(perm));
    return 1;
  }

  // it is important that we iterate from 0 to n-1 since
  // the problem requires us to output the "most preferred" ordering,
  // so that should be the first one we generate
  int tot = 0;
  for (int i = 0; i < n; ++i)
    // if the number is not yet used and it does not conflict
    // with the previous number in the permutation (if any),
    // try using it at the end of the permutation we are building
    if (!used[i] && (plen == 0 || !conflict[perm[plen-1]][i])) {
      used[i] = true;
      perm[plen] = i;
      tot = search(plen+1);
      if (tot == 1) {
          return 1;
      }
      used[i] = false;
    }
  return 0;
}


int main() {
  while (cin >> n) {
    memset(used, false, sizeof(used));
    string students[10];
    for (int i = 0; i < n; ++i) cin >> students[i];
    S = n;
    std::sort(students, students+S);
    memset(conflict, 0, sizeof(conflict));
    cin >> m;
    for (int j = 0; j < m; ++j) {
      string a, b;
      cin >> a >> b;
      int ia = find(students, students+n, a)-students;
      int ib = find(students, students+n, b)-students;
      conflict[ia][ib] = conflict[ib][ia] = true;
    }
    output[0] = -1;
    o = search(0);
    if (o == 0){
      cout << "You all need therapy." << endl;
    } else {
      for (int i = 0; i < n; ++i) cout << students[output[i]] << (i+1==n?'\n':' ');
    }
  }
  return 0;
}
