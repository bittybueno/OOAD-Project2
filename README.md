# OOAD-Project2
Team Contributers: Nimra Sharnez and Marissa Bueno 

We utilized the following patterns:

**Strategy Pattern**
* Having at least one Animal behavior delegated and referenced by Animals rather than being inherited and overridden.
>>* Here our **PerformRoamBehavior** in Animals delegates the objects tasks to  **RoamBehavior**. 
>>* Similarly, **PerformSpeakBehavior** and **PerformEatBehavior** delegated the objects tasks to **SpeakBehavior** and **EatBehavior**.
* The zookeeper's methods to command the animals is also being delegated
>* The zookeeper's method to put the animals to bed is handled by the function sleep() in the Animal Class. Similarly, wakeEm() -> wake(), feedEm()->PerformEatBehavior(), exerciseEm()->PerformRoamBehavior(), callEm()->PerformSpeakBehavior().

**Observer Pattern**
*  Create an Announcer class, Announcer will observe the Keeper. Before the Keeper commands the animals to do a tasks, the Keeper will create an observable event for the observer, the Announcer. Announcer recieves a signal from the Keeper which triggers an update method.
Once the Keeper is done with their tasks and sending messages to the Announcer, the Keeper will unregisted the Announcer as a subscriber and the Announder ceases observing the Keeper and deconstructs.

* To implement this pattern, four classes were created:
>* **Subscriber**
>>* Has an update function that takes in a message
>* **Publisher**
>>* Can register, unregister and dispatch subscribers
>* **Announcer** 
>>* A subclass of the Abstract Class Subscriber, which customizes the update method to repeat what the Publisher dispatched to their subscribers
>* **Keeper** 
>>* A subclass of the Abstract Publisher Class. This subclass inherits the behaviors of a Publisher while also holding the methods command the animals to wake, talk, eat, exercise, and sleep

**Instructions**
* This project was created using VS Code in Python 3.6. To "visit the zoo" run the Humans.py file! 


Sources

https://www.protechtraining.com/blog/post/tutorial-the-observer-pattern-in-python-879
