import tweepy
import time


#参照したコード"https://koleoblog.info/how_to_make_tweetbot/#%E3%80%90STEP%EF%BC%92%E3%80%91%E3%80%80API%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%97%E3%83%AA%E7%99%BB%E9%8C%B2"
auth = tweepy.OAuthHandler('VNAxQYwfb7Q28NDlP70DucIye',
                           'TMWLkacCL9IpGDVmebD7X4sbgtYoh121o03VlnFlzsxT6vfv1x')
auth.set_access_token('1566592926645628928-dejbAOkM4XTBJZM0FKUzoKIsErfVem',
                      'ooQjJrpXRlBicUkzNx8hnKaForLNiG4P7VuaTbfPdz7Fr')
api = tweepy.API(auth, wait_on_rate_limit=True) #"wait_on_rate_limit=True"は、大量のデータを処理するときに、「APIの利用制限に引っかかった時に、必要時間だけ待機してくれる」設定

#アカウントへのメンションを代入
public_tweets = api.mentions_timeline()

tweet_count = 5

for tweet in public_tweets:
    try:
        api.update_status("test_test")
    except StopIteration:
        break