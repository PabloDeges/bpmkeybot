import tweepy
import time
import random
from datetime import datetime
from datetime import date

#keys removed for security reasons ;)

#stores keys in useable variables
CONSUMER_KEY = 'insert cons key'
CONSUMER_SECRET = 'insert secret'
ACCESS_KEY = 'insert access key'
ACCESS_SECRET = 'insert acc secret'

#tech
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def generate_tweet():


    #time dingsbums
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")

    #console 1
    print("request started" + " " + current_time + " " + current_date)

    # generates a random int/bpm value between 80 and 160
    # converts it to a string to enable string concatenation
    bpmvar = random.randint(80, 160)
    bpm = str(bpmvar)

    # creates the list of all possible notes
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    notevar = random.randint(0, 11)

    # chooses minor or major
    mood = ["Minor", "Major"]
    moodvar = random.randint(0, 1)
    # tweet
    api.update_status("most recent bpmkey is: " + bpm + "BPM" + " " + notes[notevar] + " " + mood[moodvar])
    #console 2
    print("request finished... " + " " + current_time + " " + current_date)


while True:
    generate_tweet()
    time.sleep(21600)


#@p_deges
#@222virus
#python > teachingscript














