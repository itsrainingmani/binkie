# Binkie

- Randomly insert noise samples into a Zoom meeting
- Randomize the duration of the sample (capped at 10 seconds)
- Dynamic recovery time based on how long the previous sample was

## Things we want to do

[x] Identify that there is a Zoom meeting going
-> check the process table and see if Zoom is present

[ ] Identify the audio input device?
How do we access the zoom sound input ? Zoom local API? Zoom extension?

Re-creating a soundboard in python

Directory of sounds -> That are available to the program
Get a handle to a sound input
randomly select one of the sounds from the directory

ps aux | grep 'CptHost.app/Contents/MacOS/CptHost' which returns two rows if we are in a meeting. Also for some weird reason shows the actual grep command as a process so we can just ignore any rows with the word grep
