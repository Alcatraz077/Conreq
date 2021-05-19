from platform import platform
from conreq.utils import log

from django.template import loader
from django.views.decorators.cache import cache_page
from django.http import HttpResponse

# This function generates the AuthURL, openes a web browser to that URL. It then retrives the token and saves it to a file, once the user signs into their Plex account.
# Then, it renders the plex_oauth.html page directing the user to go to "Manage Users" page to import Plex users.

async def plex_oauth(request):
    # Plex OAuth Imports
    import asyncio
    from plexauth import PlexAuth
    import webbrowser
    import requests
    
    

    PAYLOAD = {
    'X-Plex-Product': 'Conreq',
    'X-Plex-Version': '0.18.6',
    'X-Plex-Device': 'Conreq',
    'X-Plex-Platform': 'Conreq',
    'X-Plex-Device-Name': 'Conreq',
    'X-Plex-Device-Vendor': 'Conreq',
    'X-Plex-Model': 'Conreq',
    'X-Plex-Client-Platform': 'Conreq'
    }
    
    async with PlexAuth(PAYLOAD) as plexauth:
        await plexauth.initiate_auth()
        AuthURL = plexauth.auth_url()
        webbrowser.open(AuthURL,new=1, autoraise=True)
        PlexToken = await plexauth.token()
    
    if PlexToken:
        #Print Statement used for debugging, will be removed in final commit to PR
        print("Plex Token: {}".format(PlexToken)) 

        # Removed cookie method and replaced with saving token to file.    
        TokenFile = open('data/plex.token', 'w+')

        with open('data/plex.token', 'w+'):
            TokenFile.write(PlexToken)
            TokenFile.close()
            response()

    else:
        print("No token returned.")
        #return HttpResponse("404 No Token Returned")

    #return template.render(request, "plex_oauth.html")
    #return HttpResponse(template)
    #return HttpResponse(template.render) 
    #return HttpResponse(template.render(plex_oauth))
    #return HttpResponse("")
    #return template.render(request,"viewport/plex_oauth.html")
    
    template = loader.get_template("viewport/plex_oauth.html")
    #context = {request}
    #return HttpResponse(template.render(context, request))
    #return render(request,'viewport/plex_oauth.html',{'plex':request})
    #return HttpResponse(template.render(context, request))
      
def response():
    from django.shortcuts import render
    request = ""


    template = loader.get_template("viewport/plex_oauth.html")
    return render(response,'viewport/plex_oauth.html',{'plex':request}) 