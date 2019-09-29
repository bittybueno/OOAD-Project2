# OOAD-Project2
The OO language we chose was Python 
We utilized the following patterns:

**Strategy Pattern**
* having at least one Animal behavior delegated and referenced by Animals rather than being inherited and overridden.
>>* Here our **PerformRoamBehavior** in Animals delegates the objects tasks to  **RoamBehavior**. 
>>* Similarly, **PerformSpeakBehavior** and **PerformEatBehavior** delegated the objects tasks to **SpeakBehavior** and **EatBehavior**. 