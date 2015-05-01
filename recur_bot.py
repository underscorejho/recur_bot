
#!/usr/bin/python

# Jared Henry Oviatt
# Used RemindMeBot! on GitHub as a reference

import time

import praw # python reddit API wrapper

def main():

  USER = raw_input("USER= ")
  PASS = raw_input("PASS= ")  

  r = praw.Reddit(user_agent = 'Recursion Bot operating on /u/recursion_bot v0.01')
  r.login(USER, PASS)
  print "start"

  commented = []
  TEN_MINUTES = 600000

  while True:
    try:
      # loop through all comments
      for comment in praw.helpers.comment_stream(r, 'all', limit=None, verbosity=0):
        if ("/u/recursion_bot" in comment.body and comment.id not in commented):
          comment.reply('/u/recursion_bot')
          commented.append(comment.id)
          # wait until allowed to participate again
          time.sleep( TEN_MINUTES )
    except Exception as err:
      print err

if __name__ == '__main__':
  main()
