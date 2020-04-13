// @TODO(proballstar): change to python
class Drone{
    //creating properties
    int batteryPercentage = 100;
    bool anonymous = false; 
    bool isFlying = true;
    String manufacturer;
    // @TODO(proballstar): add more properties
    Drone(this.batteryPercentage, this.anonymous,this.isFlying, this.manufacturer)
    String location(){
        //@TODO: make python/dart code to find location
        return location
    }
    String LowBattery(){
        if(batteryPercentage < 30){
           return 'Warning, the Battery Percentage is very low it is $batteryPercentage' 
        }else{
            return 'Battery is Fine'
        }
    }
    void safetyWhenAnonymous(){
        if(anonymous != false){
            //@TODO: Add code when drone is anonymous
        }else{
            print('All Good Just make sure the drone is doing fine')
        }
    }
    //@TODO: Add more functions for the drone
    
}

class firebolt extends Drone{
    //Add properties that only a Firebolt-ai Drone has
    //Add any different functions only that Firebolt-ai Drone has
    @override
    //Add any functions that a regular drone has that Firebolt-ai Drone does differently
    
}
Canary = firebolt()
