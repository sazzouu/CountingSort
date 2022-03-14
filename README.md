# Countingsort
### Problem
###### Overview
Sorting elements topologically is a problem that we are facing in many different
situations. A popular example would be sorting contestants in a leaderboard.
Depending on the application we want to - and sometimes even must - aim
for the best runtime complexity. We do not want to wait another season to
determine the winner of a football-match, do we? Since we have to touch every
element at least once we can already tell that we have ***Ω(n)*** as our lower
boundary in sorting. One way to reach that runtime is an implementation of
**Countingsort**
###### Input
Since we are literaly talking about *counting* something we obvously need some sort of numerical values. Optionally we could also pass the maximum value among our elements since we will need it later on.
This however can easily be determined at runtime in linear time so we take this as given. Given the nature of how **Countingsort** actually sorts all values passed must be (ideally positive) integers. So the input boils down to:
- ***A*** = *A list of integers*
- ***k*** = *The maximum value an input element can have* (optional)
- ***n*** = *The number of elements in our array* (optional)
###### Output
The output obviously is the input elements in a topological order.
### Solution
