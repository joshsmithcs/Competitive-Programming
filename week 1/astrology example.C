/*
  Solution to astrologicalsigns
  https://ualberta.kattis.com/problems/astrologicalsign

  Copyright: Zac Friggstad 2021
*/

#include <iostream>
#include <string>

using namespace std;

// converts the date to an integer, earlier dates convert to smaller integers
int convert(string mon, int day) {
  string months[] = {
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
  };

  // get the month as a value from 0 to 11
  int m;
  for (m = 0; months[m] != mon; ++m);

  return m*31 + day;
}

int main() {
  // capricorn appears twice because it is "split" by the New Year
  string signs[] = {
      "Capricorn", "Aquarius", "Pisces",
      "Aries", "Taurus", "Gemini",
      "Cancer", "Leo", "Virgo",
      "Libra", "Scorpio", "Sagittarius",
      "Capricorn"
  };

  // store the converted end date of each astrological sign
  // (with Capricorn broken into 2 signs)
  int end_dates[] = {
      convert("Jan", 20), convert("Feb", 19), convert("Mar", 20),
      convert("Apr", 20), convert("May", 20), convert("Jun", 21),
      convert("Jul", 22), convert("Aug", 22), convert("Sep", 21),
      convert("Oct", 22), convert("Nov", 22), convert("Dec", 21),
      convert("Dec", 31)
  };

  int cases;
  cin >> cases;

  for (int i = 0; i < cases; ++i) {
    int day;
    string mon;
    cin >> day >> mon;

    int converted = convert(mon, day);

    // find the first astrological sign whose end date is >= the input date
    for (int j = 0; j < 13; ++j)
      if (converted <= end_dates[j]) {
        // we can print the answer to this test case before reading the next
        // case, the online judge simply waits until your program terminates
        // and then checks ALL output it produced against the expected answer
        cout << signs[j] << endl;
        break;
      }
  }

  return 0;
}