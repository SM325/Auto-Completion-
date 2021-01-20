# project with google - 
Program that enable completion of sentences from articles, documentation and information files on various technological issues.

The program ran in two stages:
First stage (offline)- The system reads the text files from a pre-determined place and prepares them for the service stage (serving)

Second stage (online) - The system waits for user's input.
The user types characters and presses Enter. The system displays the five best completions. To finish typing the sentence, press #

Quick start
-----------
a. First put all the files you want to run on them in Archive directory

b. Run the offline stage
 ```
python data_initiator.py
 ```
c. Run the online stage
```
python controller.py
 ```

Example
-----------
![Demo](https://user-images.githubusercontent.com/70665664/105208287-34212c80-5b51-11eb-99a5-381d51b7aa41.mp4)
