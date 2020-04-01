# What is this?
I created a Deep Learning model that generates random user names. 

# On which dataset has the model been trained?

I used Riot's API to download more than 60000 League of Legends summoners names (ingame names), all across
their global servers. I filtered non-ascii names out and created a database which is 
basically a huge text file that contains 1 name per line.

Then I modified a tensorflow script from https://github.com/EliotAndres/char-rnn-tensorflow-js/blob/master/python/char-rnn-tensorflow-js.ipynb to train a model on my dataset. I changed the amount of epochs and a few other parameters. 


While generating the model tensorflow is printing out deep learning generated names, which I then saved in a new database (again, just a huge text file). I did some cleaning (I removed all names from this new database that have already been in the original database that the model has been trained on. I did this so that the model doesn't generate the username "A great success" when some human already had picked this username and it has been trained on this exact name).

# Summary

I trained my model on more than 60000 summoner names from the popular MOBA game League of Legends to create this model. While training it generated more than 6000 new names using Tensorflows deep learning techniques. You can find these generated names in /4 - summary/output.txt. Keep in mind that while training the model Tensorflow varies parameters like the diversity (which is 0.4, 0.6, 0.8, 1.0, 1.2 or 1.4). So the higher the diversity the more random (and non-human like) the names usually are. In the list output.txt I sorted all generated names alphabetically, which means that names that have been generated with different parameters are mixed. That's why some names appear pretty random meanwhile others are pretty human-like.


I already found some hilarious usernames in output.txt


A Best-Of list might come soon! :)



Oh and one more thing: If tensorflow keeps spitting warnings at you for using deprecated methods, you should downgrade your numpy version to 1.16.4



