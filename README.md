# OOAD-Project2
The OO language we chose was Python 

We utilized the following patterns:

**Strategy Pattern**
* Having at least one Animal behavior delegated and referenced by Animals rather than being inherited and overridden.
>>* Here our **PerformRoamBehavior** in Animals delegates the objects tasks to  **RoamBehavior**. 
>>* Similarly, **PerformSpeakBehavior** and **PerformEatBehavior** delegated the objects tasks to **SpeakBehavior** and **EatBehavior**.
* The zookeeper's methods to command the animals is also being delegated
>* The zookeeper's method to put the animals to bed is handled bu the function goToSleep(). (wakeEm()-> wakeUp(), feedEm()->feed(), exerciseEm()->exercise(), callEm()->rollCall())

**Observer Pattern**
*  Create a ZooAnnouncer class, ZooAnnouncer will observe the ZooKeeper (modified to be **obervable**. Before the ZooKeeper starts to perform tasks, they will create an observable event for the ZooAnnouncer. ZooAnnouncer responds by talking to the Zoo on what will happen. Once Zookeeper is done with tasks, ZooAnnouncer should cease observing and deconstruct.

* To implement this pattern, two classes were created, a Subscriber (that has an update function that takes in a message) and a Publisher (that can register, unregister and dispatch subscribers.)
>* To replicate the functionality of a ZooKeeper, the Publisher class has methods that will command the animals. When one of these methods are called by a type Publisher, any subscribers registed to the Publisher will recieve a message/cue.
>* When the cue is recieved, the subscriber will say it "outloud" via a print statement. After announcing the message/cue, the method called will complete the remaining execution of commanding the animals to wake, sleep, eat etc...


Sources

https://www.protechtraining.com/blog/post/tutorial-the-observer-pattern-in-python-879