The CMU Arctic dataset contains .wav files of seven speakers, along with computer generated mnemonic labelling. 
Pindrop.py is a general module responsible for: 

1. Entering the name of the speaker we wish to download 
2. Requesting and downloading the entire data of that speaker into a "data" directory 
3. Unzipping the data zip file
4. Using the wav2vec library to convert the .wav files to .csv files and storing them into a new directory
5. Making a new directory for storing the output data

