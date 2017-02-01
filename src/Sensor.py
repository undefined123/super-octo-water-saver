#!/usr/bin/env python
import mraa
import time
import numpy

readTimeout=0.1
totalRead=10

def isrFunc(sensor):
    if sensor.echo.read()==1:
        sensor.echoStartTime=time.time()
    else:
        sensor.echoEndTime=time.time()

class Sensor:
    echoStartTime=None
    echoEndTime=None
    def __init__(self, triggerPin, echoPin):
        print("Trigger",triggerPin)
        print("Echo",echoPin)
        self.echo=mraa.Gpio(echoPin)
        self.trig=mraa.Gpio(triggerPin)
        self.echo.dir(mraa.DIR_IN)
        self.trig.dir(mraa.DIR_OUT)
        self.echo.isr(mraa.EDGE_BOTH, isrFunc, self) 
    
    def sendEcho(self):
        self.echoStartTime=None
        self.echoEndTime=None
        self.mesuring=True
        self.trig.write(1)
        time.sleep(0.003)
        self.trig.write(0)
       
    def measure(self):
        self.sendEcho()
        self.safe=False
        time.sleep(readTimeout)
        if self.echoStartTime==None or self.echoEndTime==None:
            return None
        else:
            deltaTime=self.echoEndTime-self.echoStartTime
            return deltaTime*1000000/58


    def measuremore(self,x=totalRead):
        measurements=[]
        for i in range(x):
            measurements.append(self.measure())
        return numpy.median(measurements)


    def __del__(self):
        self.echo.isrExit()
        
