######################################################
# # # # # # #   WHATSAPP CHAT ANALYSER   # # # # # # #
######################################################
# PURPOSE OF SCRIPT                                  #
#1 Create an empty list for each user #DONE          #
#2 Remove punctuation using string module #DONE      #
#3 Remove punctutation #DONE                         #
#4 Assign words to users in a dictionary #DONE       #
#5 Remove common words: #DONE                        #
#6 Run Counter to count words #DONE                  #
#7 Put in descending order #DONE                     #
#8 Write each user's wordcount to CSV #DONE          #
######################################################
# Version 1.0 written by Sam Gandhi, 1 June 2018     #
######################################################

import csv, string, os
from collections import Counter
from collections import OrderedDict
from datetime import datetime

### PARAMETERS ###

txtfile = open(input("What is the filepath for your Whatsapp chat text file? (Remember to include .txt)"))
os.chdir(input("Where do you want the WordCount files saved?"))
usersWords = {} # new empty dictionary created

startTime = datetime.now()
print "Script started at "+str(datetime.now())

### PROCESSING TXT FILE ###

for line in txtfile:
    try:
        int(line[0]) # if first character can be made into an integer, continue with loop. If not it's a msg from the Whatsapp app so ignore
        if isinstance(line[0],str):
            date = line[:10]
        time = line[12:17]
        userafterdash = line.split("-")[1] # extracting characters after dash
        userbeforecolon = userafterdash.split(":")[0] # extracting remaining characters before colon
        user = userbeforecolon[1:]
        chat = line.split(": ")[1:] # HAVEN'T ACCOUNTED FOR IF USER PRESSES ENTER IN CHAT!        
        completechat = ""
        for c in chat:
            completechat += str(c) + " " # putting the list "chat" back into one string, with a space after each word
        chatOrig = completechat[:-1] # removing the uneccessary final space
        wordsNoS = chatOrig.replace("'s","") # remove all "'s"
        wordsNoPunc = wordsNoS.translate(None,string.punctuation) # remove all punctuation
        wordsLower = wordsNoPunc.lower() # make all characters lower case      
        words = wordsLower.split() # split line by space        
        wordsToRemove = ["and","is","it","a","at","to","of","get","they","still","as","set",
                         "his","her","he","she","going","go","you","was","then","though",
                         "but","so","think","do","i","me","theyre","there","we","when",
                         "their","along","with","anyway","today","tomorrow","got","them",
                         "leave","the","out","in","this","that","come","came","up","such",
                         "down","left","all","have","see","im","are","want","need","him",
                         "if","or","for","too","good","bad","soon","has","be","may","her",
                         "yesterday","add","put","in","now","what","where","which","who",
                         "your","on","my","did","dont","wont","know","day","watch","back",
                         "were","can","omitted","just","not","ill","like","from","how",
                         "ive","will","time","one","here","work","well","about","youre",
                         "why","had","us","cant","should","by","make","been","only","let",
                         "more","our","would","does","those","am","an","off","sure","could",
                         "its","maybe","take","probably","doesnt","lot","same","mins",
                         "keep","sort","getting","away","doing","other","into","onto","any"]
        wordsFiltered = []
        for word in words:
            if word not in wordsToRemove:
                wordsFiltered.append(word)
        usersWords.setdefault(user,[]).append(wordsFiltered) # append words to dictionary by user

    except:
        continue

print "Text file processed, now word-counting..."

### COUNTING WORDS ###

for user,words in usersWords.iteritems(): # for user:
    usersWordList = [] # empty list created per user to store each user's words
    print user.upper() # i.e. user
    for sublist in words: # lists within list
        for word in sublist: # words within lists
            usersWordList.append(word) # append words to empty user words list
    wordCount = Counter(usersWordList) # count occurances of each word
    count_descending = OrderedDict(reversed(sorted(wordCount.items(), 
                                  key=lambda kv: kv[1])))    
    for pair in count_descending.iteritems():
        #print pair
        with open(user+" WordCount.csv","ab") as fp:
            wr = csv.writer(fp)
            wr.writerow(pair) # write words and counts to CSV, in descending order
            fp.close()

print "Script finished at "+str(datetime.now())
print "Script took "+str((datetime.now()-startTime))
print "See folder for CSV files"



# -------------------------------------------------------------------------------------------- #

# THINGS TO ADVANCE THIS
# combine outputs for each user into one CSV (how to specify write to columns?)
# output a txt file with interesting metrics:
   # time tool took
   # number of users
   # most popular words in group and by who
# also output every word to a user key called "All", for counting every word in the chat
# highlight words of interest (swearwords etc!)
# create charts and graphs, turn into a dashboard?
# create wordclouds
