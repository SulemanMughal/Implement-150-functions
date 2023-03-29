# Exercise No. 109

A file called *hashtags.txt* containing hashtags related to sport is attached to the exercise:


    #sport #fitness #training #motivation #gym #sports #workout #fit #football #love #instagood #fitnessmotivation
    #lifestyle #running #like #bodybuilding #healthy #instagram #health #soccer #follow #crossfit #photography #bhfyp #run
    #nature #fun #healthylifestyle #muscle #bhfyp #fashion #fitfam #gymlife #photooftheday #team #personaltrainer #nike
    #picoftheday #exercise #mma #sportlife #boxing #athlete #bike #basketball #happy #deporte #gymmotivation #strong
    #cycling #yoga #style #ufc #sportmotivation #fitnessgirl #calcio #instafit


Implement a function called `clean_hashtags()` that loads the included *hashtags.txt* file and does some cleanup. Extract hashtags up to 4 characters long. The `'#'` sign is not included in the length of the hashtag. For example, the hashtag `'#gym'` has a length of 3.

Also take care to remove duplicates, if any. Then return the alphabetically sorted hashtags as a list.


In response, call `clean_hashtags()` function and print the result to the console.


**Expected result:**


    ['#bike', '#fit', '#fun', '#gym', '#like', '#love', '#mma', '#nike', '#run', '#team', '#ufc', '#yoga']