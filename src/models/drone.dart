class Drone {
    int batteryPercentage = 100;
    int Longitude;
    int Latitude
    bool isFlying = true;
    String manufacturer = 'Firebolt Space Agency';
    String location
        // @TODO(proballstar): add more properties
    String findLocation() {
        // Rohan, where is location defined???
        return location
    }
    String location(){
        
        //@TODO: make python/dart code to find location
        return location
    }
    String LowBattery(){
        if(batteryPercentage < 30){
           return 'Warning, the Battery Percentage is very low it is $batteryPercentage'; 
        }else{
            return 'Battery is Fine';
        }
    }
    int Battery(){
        // return the battery percentage
        return batteryPercentage
    }
    void Anymous(){
        anonymous = true; 
    }
    void Waiting(){
        isFlying = false;
    }
    //add  more functions for the car
    
    
}

class firebolt extends Car{
    //Add properties that only a Firebolt-ai Drone has
    //Add any different functions only that Firebolt-ai Drone has
    @override
    //Add any functions that a regular drone has that Firebolt-ai Drone does differently
    
}
Canary = firebolt()
