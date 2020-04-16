import json
from instapy import InstaPy
from instapy.util import smart_run

#login credentials

insta_username = 'shoey_98'
insta_password = 'manthila@1A'

#get followers list and read json file
folfile = "/home/manthila/InstaPy/logs/manthi_b1997/relationship_data/manthi_b1997/followers/14-04-2020~full~995.json"
with open(folfile) as f:
    data = json.load(f)

#split the jason file into sizable chunks
n=160 #number of followers to engage in one run
fdata = [data[i:i + n] for i in range(0, len(data), n)]
#print([len(f) for f in fdata])
fdata = fdata[1] ### runs the first chunk; REMEMBER TO CHANGE THE INDEX FOR EVERY RUN
nposts = 2 #posts to like
pertcom = 20 #percent to comment; comment 1 in 5 likes

print(fdata)

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  multi_logs=True)

with smart_run(session):
    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "comments_h"],
                                 sleepyhead=False, stochastic_flow=True, notify_me=True,
                                 peak_likes_hourly=100,
                                 peak_comments_hourly=80)

    print('Going to like ' + str(nposts) + ' posts each of these ' + str(n) +' followers:')
    print(fdata)
    print('Commenting percentage : ' + str(pertcom))
    session.set_comments(['Cool', 'Nice'])
    session.set_do_comment(enabled=True, percentage=pertcom)
    session.set_do_like(True, percentage=100)
    session.interact_by_users(fdata, amount=nposts, randomize=False)