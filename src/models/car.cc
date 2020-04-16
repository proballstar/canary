#include <iostream>
using namespace std;
class Drone {
   private:
    int height;
    string location;
    bool antonymous;
    string company;
    int lat;
    int long;
    string pilot;
    // add other Attributes
    Drone(int a,string b, bool c,string d, int e,int f, string g){
        height = a;
        location = b;
        antonymous = c;
        company = d;
        lat = e;
        long = f;
        pilot = g;
    }
   public:
    int findLocation(){
        return lat;
        return long;
        return height;
    }
    int goHigher(){
        height = height + 1;
        return height;
    }
    int goLower(){
        height = height - 1;
        return height;
    }
    int goSouth(){
        lat = lat  + 1;
        absLat()
        return lat;
        
    }
    int goNorth(){
        lat = lat - 1;
         absLat()
        return lat;
       
    }
    int goWest(){
        long = long - 1;
        absLong()
        return long;
        
    int goEast(){
        long = long + 1;
        absLong()
        return long;
     
    }
    string findLocation(){
        // make code to find location
        return location;
    }
    string goingAntonymous(){
        antonymous = true;
    }
    int absLat(){
        if(lat > 90){
            remainder = lat - 90;
            lat = -90 + remainder;
            return lat;
        }else if( lat < -90 ){
            remainder = lat + 90;
            lat = 90 + remainder ;
            return lat;
        }else{
            return lat;
        }
    }
    int absLong(){
        if(long>180){
            remainder = long-180;
            long = 0 + remainder;
            return long;
        }else if(long<0){
            long = 180 + long ;
            return long;
        }else{
            return long;
        }
  
    }
 };
/*
    Drone(int a,string b, bool c,string d, int e,int f, string g){
        height = a;
        location = b;
        antonymous = c;
        company = d;
        lat = e;
        long = f;
        pilot = g;
    }
  */
 int main(){
    Drone canary(0,"Some Where in the world :)",false,"firebolt space agency",0,0,"BOBOB BOBOB")
 }
  
