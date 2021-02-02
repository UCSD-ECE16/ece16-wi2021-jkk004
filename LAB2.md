I made a folder with all the videos due to my gifs being too short when optimized and too large if they arent https://drive.google.com/drive/folders/1yH_9qMzIOthvwkxRodfma5dTTTnqHjkb?usp=sharing 

Challenge 1:

In my code, I used the reading of 2000 because I noticed that that was about where the graph peaked when it got tapped. This way may be unconventional, but it got the job done. I added a delay of 1100 whenever it was tapped because if I didn't, every tap would add like 10 to the number of taps. 1100 ms or 1.1 second was just the perfect amount of time for the thing to stop shaking after it got a reading of 2000.

![image](https://user-images.githubusercontent.com/62976976/106346183-02534880-626a-11eb-99fe-98aa9b899244.png)


![ezgif com-gif-maker (10)](https://user-images.githubusercontent.com/62976976/106347318-6843ce00-6272-11eb-8153-a1af1856c7bc.gif)



![image](https://user-images.githubusercontent.com/62976976/106346496-7c84cc80-626c-11eb-9450-bbbdd31dce6a.png)


I found it to implement the buzz motor because I wasn't sure on the wiring, so I didn't implement it. If I did, I would have set the buzz motor off whenever numTaps == 0

This is my code for Challenge 2
![image](https://user-images.githubusercontent.com/62976976/106562359-0b008480-64df-11eb-8e96-79b092289919.png)



This here is challenge 2 where I show the countdown in effect
![ezgif com-gif-maker (11)](https://user-images.githubusercontent.com/62976976/106562029-90376980-64de-11eb-80b0-118350854aa1.gif)


This is the number of taps resetting after being held down for 2 seconds. You can see it goes from 5 to zero
![ezgif com-gif-maker (12)](https://user-images.githubusercontent.com/62976976/106564575-40f33800-64e2-11eb-9af8-32adc4865699.gif)

This is my state machine drawing, but Im not too sure if it is correct. I tried my best :)
![statemachine](https://user-images.githubusercontent.com/62976976/106565050-0047ee80-64e3-11eb-9733-839e0a4928e7.jpg)


