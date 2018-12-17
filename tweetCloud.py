import sys
import subprocess
from random import randint
import twython
from twython import Twython
from collections import Counter



TWITTER_APP_KEY = '####' #supply the appropriate values for all of these
TWITTER_APP_KEY_SECRET = '####' 
TWITTER_ACCESS_TOKEN = '####'
TWITTER_ACCESS_TOKEN_SECRET = '####'

t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

query = raw_input("What are you searching for?: ")

search = t.search(q= query,   #What we are looking for, use hashtag or not
                  count=100) #count=number of most recent tweets, twitter api results per request only goes up to 100? LOOK IN TO PAGINATION AND RETRIEVING TWEETS NUMBER PER PAGE

tweets = search['statuses']

wordList = []             ### every single word in top 100 tweets, this is the master list        ### FIND OUT HOW TO REMOVE CERTAIN WORDS FROM THIS LIST, ex. 'HTTP', 'RT', things like that
wordFreq = []             ### a count of every corresponding word from tweets, the number list for the master list

####### MAKE THIS A METHOD #######

numberOfTweets = 1

for tweet in tweets:
  
  #print str(numberOfTweets) + ')   ' + tweet['text'], '\n\n\n'    ### prints latest x number of tweets with given search term
  wordVar = tweet['text'].split()                                 ### splits words in the tweets in to a list of strings named wordVar
  #numberOfTweets += 1

  
  for x in wordVar:                                               ### appends every string (aka every word) to a master list named wordList (change the variable x in to something meaningful)
    wordList.append(x)


RTcount = 0
HTTPScount = 0

for i in wordList:
  if i == "RT":
    print i
    wordList.remove(i)
    print 'deleted a RT!'
    RTcount += 1
    
  elif i.startswith("RT"):
    print i
    wordList.remove(i)
    print 'deleted another RT'
    RTcount += 1
    
  elif i.startswith("rt"):
    print i
    wordList.remove(i)
    print 'deleted an rt'
    RTcount += 1

  elif i.startswith("Rt"):
    print i
    wordList.remove(i)
    print 'deleted an Rt'
    RTcount += 1
    
  elif i.startswith("https"):
    print i
    wordList.remove(i)
    HTTPScount += 1
    print 'deleted an https!'
    
  elif i.startswith("HTTPS"):
    print i
    wordList.remove(i)
    HTTPScount += 1
    print 'deleted an HTTPS!'

  elif i.startswith("Https"):
      print i
      wordList.remove(i)
      HTTPScount += 1
      print 'deleted an Https!'
print wordList

print RTcount
print HTTPScount
    
#print wordList                                                   ### wow that's a lot of words


###################################

#for tweet in tweets:
  #wordList.append(tweet['text'])         ### THIS APPENDS EVERY SINGLE PIECE OF TWEET DATA RETRIEVED FROM THE SEARCH STATUSES, User, tweet id, ETC ETC ETC


#for word in wordList:               ### prints the frequency OF EVERY SINGLE WORD IN ALL OF THE TWEETS, useful for debugging and live viewing of counting
  #print wordList.count(word), word

for word in wordList:             ### populates wordFreq, the number list
  wordFreq.append(wordList.count(word))


pairList = zip(wordFreq, wordList)
pairList.sort()


print '\n\n\n'

#########


def interface():        ### THIS IS AN INCOMPLETE METHOD, maybe use it as an interface for idle or command line or w/e
  print "Twitter Hashtag Wordcloud Generator v1.0, 2017 Copyright Nathan Roane"
  

#########


def remove_duplicates(x):
    a = []
    hashtag = search

    
    for i in x:
        if i not in a:    ### THIS POPULATES BLANK LIST WITH EVERY SINGLE WORD, but JUST ONCE, only if the list does not already contain that word
            a.append(i)
    print 'THIS IS YOUR A-LIST'
    print '\n\n\n'
    
    print a
    print '\n\n\n'
    pairList2 = a
    print 'THIS IS YOUR NEW PAIR LIST'
    print '\n\n\n'
    
    print pairList2
    print '\n\n\n'
    
    print "The 50 most common words found when searching for your hashtag are: \n'"
    z = 1
    for i in range (0,65):
      print str(z) + ": '" +  pairList2[len(pairList2) - z][1] + "' with " + str(pairList2[len(pairList2) - z][0]) + " occurences."   ###ACCESS THE TUPLES BY INDEX, second elements of tuple is the WORD
      z = z + 1

    
    print '\n\n\n'
    #print len(a)                                 ### number of unique words      ### DEBUG STUFFF
    #print len(wordList)                          ### number of total words


#########


#print wordFreq         ####THIS IS ALL DEBUG STUFF, KEEP IT, print them when you want to see what words and their frequenices are being collected!!!!
#print '\n\n\n'
#print wordList
#print '\n\n\n'


#########


def randImgName():
  imgName = randint(0,99999999999999)
  return imgName
  
  
#########


def OKwrite(THELISTYOUNEED, randImgName):



  
    print('Exporting words to text file')
    newImg = str(randImgName()) + '.png'
    print('Your new image is named ' + newImg) #### THIS RETURNS A MEMORY ADDRESS...? Find out how to access the value at said memory address.FIXED!!!!! (Call the function instead and return the value you want in the function)
    
    

    name = open("next2.txt", 'w') ### currently next2.txt is the only text file that the words go in to ##### FIND OUT HOW TO CREATE DYNAMIC NEW TEXT FILES TO SAVE THE WORDLIST IN TO

    for item in THELISTYOUNEED:
      name.write("%s\n" % item.encode('utf-8'))

    subprocess.call(['wordcloud_cli.py', '--text', 'next2.txt', '--imagefile', newImg, '--width', '1000', '--height',  '500'])  ### We are calling the variable newImg as an argument for our wordcloud_cli.py command!!


#########



OKwrite(wordList, randImgName)
