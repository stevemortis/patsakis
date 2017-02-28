import re
import tweepy
cons_key ="cXE4CnquXJnsC8joSJQCjzEq6"
cons_sec = "SpfSZ0D4fncvf996g8byWW0Tk21uvfUzwrz0JB9aR8k4yExche"
acc_tok = "932529565-OnUNgMcTKAuQpV238EjxA4NSUsSG0XDxFtveU541"
acc_tok_sec = "CTQVim4gEmJBjwbp2OrUoICL9d03Fpp4zHNUkna85GTAS"
auth = tweepy.OAuthHandler(cons_key,cons_sec)
auth.set_access_token(acc_tok,acc_tok_sec)
api = tweepy.API(auth)

names=[]
def TweetFetch():
    success=0
    while success==0:
        try:
                        data=""
                        print("Δώστε ένα username χρήστη")
                        userid = input()
                        for status in tweepy.Cursor(api.user_timeline, id=userid, include_rts=False).items(10):
                            data = data + status.text + "\n"
                        success=1
                        names.append(userid)
                        return data;
        except tweepy.error.TweepError:
                        print("Το username δεν υπάρχει. Ξαναπροσπαθήστε!")
users=[]
for user in range(0,2):
	users.append(TweetFetch());
	
#Το προγραμμα μετραει ως λεξεις οποιαδηποτε σειρα γραμματων χωρισμενες απο κενο...δηλαδη μετραει και τα URL ως πολλαπλες λεξεις!
counter = []
reWord = re.compile(r"\S+")
for i in range(0,2):
	counter.append(re.findall(reWord,users[i]))

words = [len(counter[0]),len(counter[1])]
if words[0] > words[1]:
	print("Ο χρήστης " + names[0] + " έχει τις περισσότερες λέξεις. Ο χρήστης " + names[0] + " εχει" + str(words[0]) + " ενώ ο χρήστης " + names[1] +" έχει "+ str(words[1]))
else:
	if words[1] > words[0]:
		print("Ο χρήστης " + names[1] + " έχει τις περισσότερες λέξεις. Ο χρήστης " + names[1] + " εχει" + str(words[1]) + " ενώ ο χρήστης " + names[0] +" έχει "+ str(words[0]))
	else:
		print("Και οι δύο χρήστες έχουν τον ίδιο αριθμό λέξεων. Συγκεκριμένα " + str(words[0]) + " λέξεις")
		
