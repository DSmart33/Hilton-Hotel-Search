import requests
import json
import aiohttp
from aiohttp_socks import ProxyConnector

async def get_accessToken():

    # Load the config file
    with open('properties/config.json') as f:
        configFile = json.load(f)

    cookies = {
        'rxVisitor': '165476836305182I69K1TDOIPL0987NLILTNSJK53IJ5E',
        'visitorId': '83631778-39fc-4648-be43-ed719a680048',
        's_ecid': 'MCMID%7C06546371573000418848610851545713009555',
        '_fbp': 'fb.1.1654768365673.1684450530',
        'notice_preferences': '0:',
        'notice_gdpr_prefs': '0:',
        'cmapi_gtm_bl': 'ga-ms-ua-ta-asp-bzi-sp-awct-cts-csm-img-flc-fls-mpm-mpr-m6d-tc-tdc',
        'cmapi_cookie_privacy': 'permit 1 required',
        'forterToken': 'a3cdbc8197b546dc9985859da1ce85db_1657657384862_355_UAL9_9ck',
        'akacd_ohw_prd_external': '3835298838~rv=30~id=1873aeee38fd2b0014a03c909f20ece1',
        'ak_bmsc': 'A268E10C27F5FD2E072D060F5F4FE315~000000000000000000000000000000~YAAQB/ferSBNZe+BAQAAqQRT/xBmJoj4VWPf9+pqzX08dEAJxXUW/Io7w3tPepyQaTK1mu5L8+EOVhozZyYUcMTyipdP7xWCvCcRP1M6n9M6vAVLzOMPLb6nZWmzroTVmvTyE7xxlWAqTscS9t9zvh0DMN2VyYoRn+5cf2+/49VCVze6ZuLllxUltAlL1rgF1RDbS62EEI3YockCEfBHvGhbHEvEG/6QDx9GGpyG2El6FhXPCtV5UVJHvggm91zMPrPiQeBrL5XUcZqy0rjdNCNSTUSysq2lIKjFRpgAqUSTOYaCTp6XsaJgUT5oWeKd0AVMWs7APN08y9JqhSUzFpxQi//KMFULBxSo/HWt8iiC5zDyxe8vkRB4nuWbALHtTLNl7UAlDL4f',
        'bm_sz': '1878C10D8E6C55ADEF7C94DBF3B8F8C0~YAAQB/ferSFNZe+BAQAAqQRT/xBNypNQ9d47jiVp71AVq/S+2NhqJrOJyAiK9Dm/XpZX6FRki1rmKgYKq1cZl8yQiZuQDWiwwGrf71erHrWIKwt6AEWtPxHEGEKnDjPvE5y/L88D6RkgFLmLalMh8KAByuraww+jMGVrlwt5mg4ItWzBud34fVvDgaXIJReumvDVtPl8zD/WXv6ZtuqNpZUYB2UR+ncJuoxNGnl4v8OS2/PgrxKNL33yqSbKHI9MTktWeeyzVG8z3exy7CKqbgrxmTGomzIrChN5hLrXddDHmMU=~3289414~3621939',
        'dtCookie': 'v_4_srv_1_sn_7FF7675D63A611C5D4E1E3A3C9419720_perc_100000_ol_0_mul_1_app-3A0da30f11c94bda74_1_rcs-3Acss_0',
        'AMCVS_F0C120B3534685700A490D45%40AdobeOrg': '1',
        'AMCV_F0C120B3534685700A490D45%40AdobeOrg': '1176715910%7CMCIDTS%7C19189%7CMCMID%7C06546371573000418848610851545713009555%7CMCAID%7CNONE%7CMCOPTOUT-1657856267s%7CNONE%7CvVersion%7C5.4.0',
        '_abck': 'CC1753C5298A29861C2EE7E1336EB885~0~YAAQB/fercUNeO+BAQAAt/iM/wh+dlIBGt/lln3QbnPCrAZ/xTjQlQkFvRAvdKfFhfy/SvUp0vZOUSOuYKeuJ7gIENb09uOs6Dw/Xe9bG27AidZ9BSdW2axFa89hfwSLh6L54ulUMiVXMMEfh0mbwQlk/Qumj5Mg8jlckKFX++wnEpWgHYBrI1cmaON+pBramWFV0bph3ChDF5ELKWWMon+RHIhZYQi/nv/NM3h7a4h/y5IYwWAaKMTRDVX38NgTY2GNwnwhSYZqkkbOUyqfTq6L8Pgje+Euba/g4r7syXZpAnTSoGPKiJPyEfHgSx3B7iLdFwa4W599X389vzU+1axg42vDvse8JgHXYygp6CEOLzMZiTFS0LjquqOXa1CUSlP9elAO7XwVwcgp7T6J8Q5orDGKDtshR9HA/rjZDalHxBrLhncz7eTypO5RFQAXqr8DbL5ARZeGnp4=~-1~-1~1657853407',
        'AKA_A2': 'A',
        'bm_sv': 'B6C524D8DF3F4030542D18DF0F9F736A~YAAQB/ferVQTeO+BAQAASAyN/xCrcJtPoTIHBclwP9NxGgXUCd+UxvnD3qxXxQHdsFf8UvyZjT4C8M8e1s9GZVVq+oQet0F2zS/dT1CQRHnEuEPbeHKZQAT8SZpYtqBTT3vqs02y96wXlO9gW+EIImCDJcgNNpCc3pRcgYXO1NdXNGiaWOVIPvEyJ2jLnKEO7W2FP9AkAWQoG+oEG2o3g/zpyE72Jruj16Pu/Es68wG+cjfgL7BBqHxuNr3xaJksxw==~1',
    }

    headers = {
        'authority': 'www.hilton.com',
        'accept': 'application/json; charset=utf-8',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/json; charset=utf-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'rxVisitor=165476836305182I69K1TDOIPL0987NLILTNSJK53IJ5E; visitorId=83631778-39fc-4648-be43-ed719a680048; s_ecid=MCMID%7C06546371573000418848610851545713009555; _fbp=fb.1.1654768365673.1684450530; notice_preferences=0:; notice_gdpr_prefs=0:; cmapi_gtm_bl=ga-ms-ua-ta-asp-bzi-sp-awct-cts-csm-img-flc-fls-mpm-mpr-m6d-tc-tdc; cmapi_cookie_privacy=permit 1 required; forterToken=a3cdbc8197b546dc9985859da1ce85db_1657657384862_355_UAL9_9ck; akacd_ohw_prd_external=3835298838~rv=30~id=1873aeee38fd2b0014a03c909f20ece1; ak_bmsc=A268E10C27F5FD2E072D060F5F4FE315~000000000000000000000000000000~YAAQB/ferSBNZe+BAQAAqQRT/xBmJoj4VWPf9+pqzX08dEAJxXUW/Io7w3tPepyQaTK1mu5L8+EOVhozZyYUcMTyipdP7xWCvCcRP1M6n9M6vAVLzOMPLb6nZWmzroTVmvTyE7xxlWAqTscS9t9zvh0DMN2VyYoRn+5cf2+/49VCVze6ZuLllxUltAlL1rgF1RDbS62EEI3YockCEfBHvGhbHEvEG/6QDx9GGpyG2El6FhXPCtV5UVJHvggm91zMPrPiQeBrL5XUcZqy0rjdNCNSTUSysq2lIKjFRpgAqUSTOYaCTp6XsaJgUT5oWeKd0AVMWs7APN08y9JqhSUzFpxQi//KMFULBxSo/HWt8iiC5zDyxe8vkRB4nuWbALHtTLNl7UAlDL4f; bm_sz=1878C10D8E6C55ADEF7C94DBF3B8F8C0~YAAQB/ferSFNZe+BAQAAqQRT/xBNypNQ9d47jiVp71AVq/S+2NhqJrOJyAiK9Dm/XpZX6FRki1rmKgYKq1cZl8yQiZuQDWiwwGrf71erHrWIKwt6AEWtPxHEGEKnDjPvE5y/L88D6RkgFLmLalMh8KAByuraww+jMGVrlwt5mg4ItWzBud34fVvDgaXIJReumvDVtPl8zD/WXv6ZtuqNpZUYB2UR+ncJuoxNGnl4v8OS2/PgrxKNL33yqSbKHI9MTktWeeyzVG8z3exy7CKqbgrxmTGomzIrChN5hLrXddDHmMU=~3289414~3621939; dtCookie=v_4_srv_1_sn_7FF7675D63A611C5D4E1E3A3C9419720_perc_100000_ol_0_mul_1_app-3A0da30f11c94bda74_1_rcs-3Acss_0; AMCVS_F0C120B3534685700A490D45%40AdobeOrg=1; AMCV_F0C120B3534685700A490D45%40AdobeOrg=1176715910%7CMCIDTS%7C19189%7CMCMID%7C06546371573000418848610851545713009555%7CMCAID%7CNONE%7CMCOPTOUT-1657856267s%7CNONE%7CvVersion%7C5.4.0; _abck=CC1753C5298A29861C2EE7E1336EB885~0~YAAQB/fercUNeO+BAQAAt/iM/wh+dlIBGt/lln3QbnPCrAZ/xTjQlQkFvRAvdKfFhfy/SvUp0vZOUSOuYKeuJ7gIENb09uOs6Dw/Xe9bG27AidZ9BSdW2axFa89hfwSLh6L54ulUMiVXMMEfh0mbwQlk/Qumj5Mg8jlckKFX++wnEpWgHYBrI1cmaON+pBramWFV0bph3ChDF5ELKWWMon+RHIhZYQi/nv/NM3h7a4h/y5IYwWAaKMTRDVX38NgTY2GNwnwhSYZqkkbOUyqfTq6L8Pgje+Euba/g4r7syXZpAnTSoGPKiJPyEfHgSx3B7iLdFwa4W599X389vzU+1axg42vDvse8JgHXYygp6CEOLzMZiTFS0LjquqOXa1CUSlP9elAO7XwVwcgp7T6J8Q5orDGKDtshR9HA/rjZDalHxBrLhncz7eTypO5RFQAXqr8DbL5ARZeGnp4=~-1~-1~1657853407; AKA_A2=A; bm_sv=B6C524D8DF3F4030542D18DF0F9F736A~YAAQB/ferVQTeO+BAQAASAyN/xCrcJtPoTIHBclwP9NxGgXUCd+UxvnD3qxXxQHdsFf8UvyZjT4C8M8e1s9GZVVq+oQet0F2zS/dT1CQRHnEuEPbeHKZQAT8SZpYtqBTT3vqs02y96wXlO9gW+EIImCDJcgNNpCc3pRcgYXO1NdXNGiaWOVIPvEyJ2jLnKEO7W2FP9AkAWQoG+oEG2o3g/zpyE72Jruj16Pu/Es68wG+cjfgL7BBqHxuNr3xaJksxw==~1',
        'origin': 'https://www.hilton.com',
        'referer': 'https://www.hilton.com/en/book/reservation/flexibledates/?ctyhocn=MLEONWA&arrivalDate=2022-10-01&departureDate=2022-10-02&room1NumAdults=2&displayCurrency=USD&brandCode=HH&inputModule=HOTEL_SEARCH&ohwDeepLinking=true&srpName=',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
    }

    json_data = {
        'app_id': '6173cfff-cc35-42b0-8272-50766956f4ea',
    }

    accessToken = ''
    
    #
    # TOR with Hilton returns 502 Bad Gateway
    #
    # Tor ProxyConnector
    #connector = ProxyConnector.from_url(configFile['tor']['proxy'], rdns=True)
    
    async with aiohttp.ClientSession() as session:
        async with session.post('https://www.hilton.com/dx-customer/auth/applications/token', cookies=cookies, headers=headers, json=json_data) as response:
            responseData = await response.json()
            accessToken = responseData['access_token']
            response.close()
        await session.close()

    # Write the accessToken to the accessToken file
    f = open("tokens/accessToken", "w")
    f.write(accessToken)
    f.close()

    return(accessToken)