# machinelearning_with_riotapi
What is this?
I created a Deep Learning model that generates random user names. 

On which dataset has the model been trained?

I used Riot's API to download more than 60000 League of Legends summoners names (ingame names), all across
their global servers. I filtered non-ascii names out and created a database which is 
basically a huge text file that contains 1 name per line.

Then I modified a tensorflow script from https://github.com/EliotAndres/char-rnn-tensorflow-js/blob/master/python/char-rnn-tensorflow-js.ipynb to train a model on my dataset. I changed the amount of epochs and a few other parameters. 


While generating the model tensorflow is printing out deep learning generated names, which I then saved in a new database (again, just a huge text file). I did some cleaning (I removed all names from this new database that have already been in the original database that the model has been trained on. I did this so that the model doesn't generate the username "A great success" when some human already had picked this username and it has been trained on this exact name).

Summary

I trained my model on more than 60000 summoner names from the popular MOBA game League of Legends to create this model. I then generated more than 6000 new names using Tensorflows deep learning techniques. You can find these generated names in /4 - summary/output.txt


I must say that my model created some hilarous usernames, I might make a Best-Of list soon!



