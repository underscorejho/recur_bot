
#!/usr/bin/python

# Jared Henry Oviatt
# Used RemindMeBot! on GitHub as a reference

import time # sleep()
import os   # environment vars (config vars)

import praw # python reddit API wrapper

def main():

  USER = os.environ.get('USER')
  PASS = os.environ.get('PASS')

  r = praw.Reddit(user_agent = 'Recursion Bot operating on /u/recursion_bot v0.01')
  r.login(USER, PASS)
  print "start"

  commented = []

  TEN_MINUTES = 600
  STOP = 'end'
  ENDED = False
  ERR = False

  username = '/u/' + USER
  print 'username is: ' + username

  while True:
    try:
      # loop through all comments
      print 'looking...'
      for comment in praw.helpers.comment_stream(r, 'all', limit=None, verbosity=0):
        if ERR: # retry error comment *
          comment = COMMENT
          ERR = False 
        COMMENT = comment

        if username in comment.body and comment.id not in commented: # look for new calls to username
          print 'found something...'
          # wait until allowed to participate again
          print 'resting...'
          time.sleep( TEN_MINUTES )

          if commented: # check if it's been ended
            for reply in comment.replies:
              if STOP in reply.body:
                # stop recurring on current thread
                commented.append(comment.id)
                print 'thread ended...'
                ENDED = True
                print 'looking...'
                break
          
          if ENDED:
            ENDED = False
            continue

          print 'commenting...'
          comment.reply('/u/recursion_bot')
          commented.append(comment.id)
          print 'looking...'
    except Exception as err:
      print err
      ERR = True
      

if __name__ == '__main__':
  main()

# *
# PRAW automatically retries requests, but comment_stream will have a new comment (i think)
# this method retries the comment it was on, but will ignore the current comment
