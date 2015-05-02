
#!/usr/bin/python

# Jared Henry Oviatt
# Used RemindMeBot! on GitHub as a reference

import time
import sys

import praw # python reddit API wrapper

def main():

  USER = sys.argv[1]
  PASS = sys.argv[2]

  r = praw.Reddit(user_agent = 'Recursion Bot operating on /u/recursion_bot v0.01')
  r.login(USER, PASS)
  print "start"

  commented = []

  TEN_MINUTES = 600
  STOP = 'end'

  username = '/u/' + USER
  print 'username is: ' + username

  while True:
    try:
      # loop through all comments
      print 'looking...'
      for comment in praw.helpers.comment_stream(r, 'all', limit=None, verbosity=0):
        if username in comment.body and comment.id not in commented: # look for new calls to username
          print 'found something...'
          # wait until allowed to participate again
          print 'resting...'
          time.sleep( TEN_MINUTES )

          if commented:
            for reply in comment.replies:
              if STOP in reply.body:
                # stop recurring on current thread
                commented.append(comment.id)
                print 'thread ended...'
                print 'looking...'
                continue

          print 'commenting...'
          comment.reply('/u/recursion_bot')
          commented.append(comment.id)
          print 'looking...'
    except Exception as err:
      print err

if __name__ == '__main__':
  main()
