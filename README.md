# OOAD-Project2
The OO language we chose was Python 
We utilized the following patterns:

**Strategy Pattern**
* Having at least one Animal behavior delegated and referenced by Animals rather than being inherited and overridden.
>>* Here our **PerformRoamBehavior** in Animals delegates the objects tasks to  **RoamBehavior**. 
>>* Similarly, **PerformSpeakBehavior** and **PerformEatBehavior** delegated the objects tasks to **SpeakBehavior** and **EatBehavior**.

**Observer Pattern**
*  Create a ZooAnnouncer class, ZooAnnouncer will observe the ZooKeeper (modified to be **obervable**. Before the ZooKeeper starts to perform tasks, they will create an observable event for the ZooAnnouncer. ZooAnnouncer responds by talking to the Zoo on what will happen. Once Zookeeper is done with tasks, ZooAnnouncer should cease observing and deconstruct.