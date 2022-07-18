import requests
import json
import aiohttp
import backoff
from aiohttp_socks import ProxyConnector

async def get_dates(accessToken, hotel, arrivalDate, month, year):

    # cookies = {
    #     'rxVisitor': '165476836305182I69K1TDOIPL0987NLILTNSJK53IJ5E',
    #     'visitorId': '83631778-39fc-4648-be43-ed719a680048',
    #     's_ecid': 'MCMID%7C06546371573000418848610851545713009555',
    #     '_fbp': 'fb.1.1654768365673.1684450530',
    #     'notice_preferences': '0:',
    #     'notice_gdpr_prefs': '0:',
    #     'cmapi_gtm_bl': 'ga-ms-ua-ta-asp-bzi-sp-awct-cts-csm-img-flc-fls-mpm-mpr-m6d-tc-tdc',
    #     'cmapi_cookie_privacy': 'permit 1 required',
    #     'forterToken': 'a3cdbc8197b546dc9985859da1ce85db_1657657384862_355_UAL9_9ck',
    #     'AKA_A2': 'A',
    #     'akacd_ohw_prd_external': '3835298838~rv=30~id=1873aeee38fd2b0014a03c909f20ece1',
    #     'ak_bmsc': 'A268E10C27F5FD2E072D060F5F4FE315~000000000000000000000000000000~YAAQB/ferSBNZe+BAQAAqQRT/xBmJoj4VWPf9+pqzX08dEAJxXUW/Io7w3tPepyQaTK1mu5L8+EOVhozZyYUcMTyipdP7xWCvCcRP1M6n9M6vAVLzOMPLb6nZWmzroTVmvTyE7xxlWAqTscS9t9zvh0DMN2VyYoRn+5cf2+/49VCVze6ZuLllxUltAlL1rgF1RDbS62EEI3YockCEfBHvGhbHEvEG/6QDx9GGpyG2El6FhXPCtV5UVJHvggm91zMPrPiQeBrL5XUcZqy0rjdNCNSTUSysq2lIKjFRpgAqUSTOYaCTp6XsaJgUT5oWeKd0AVMWs7APN08y9JqhSUzFpxQi//KMFULBxSo/HWt8iiC5zDyxe8vkRB4nuWbALHtTLNl7UAlDL4f',
    #     'bm_sz': '1878C10D8E6C55ADEF7C94DBF3B8F8C0~YAAQB/ferSFNZe+BAQAAqQRT/xBNypNQ9d47jiVp71AVq/S+2NhqJrOJyAiK9Dm/XpZX6FRki1rmKgYKq1cZl8yQiZuQDWiwwGrf71erHrWIKwt6AEWtPxHEGEKnDjPvE5y/L88D6RkgFLmLalMh8KAByuraww+jMGVrlwt5mg4ItWzBud34fVvDgaXIJReumvDVtPl8zD/WXv6ZtuqNpZUYB2UR+ncJuoxNGnl4v8OS2/PgrxKNL33yqSbKHI9MTktWeeyzVG8z3exy7CKqbgrxmTGomzIrChN5hLrXddDHmMU=~3289414~3621939',
    #     'dtCookie': 'v_4_srv_1_sn_7FF7675D63A611C5D4E1E3A3C9419720_perc_100000_ol_0_mul_1_app-3A0da30f11c94bda74_1_rcs-3Acss_0',
    #     'AMCVS_F0C120B3534685700A490D45%40AdobeOrg': '1',
    #     'AMCV_F0C120B3534685700A490D45%40AdobeOrg': '1176715910%7CMCIDTS%7C19189%7CMCMID%7C06546371573000418848610851545713009555%7CMCAID%7CNONE%7CMCOPTOUT-1657853194s%7CNONE%7CvVersion%7C5.4.0',
    #     '_abck': 'CC1753C5298A29861C2EE7E1336EB885~-1~YAAQB/ferSNfZe+BAQAAGDJT/wgKNIxMy8m2Vv0oK6GHUFVdjvNy18lGvGzzkhn/mcTOTDAjTfH510JBD+6N9/vazpg3qLwjh2bADhwMj2HSGAWvO7bPo6nctkL+C91heU68/aMEsepPARSYlaolfRXmMh1AV+sTofbpZqRw5uIGWF87FXnp5r8/eLm5NCF6Hev0+3wYsiNZsLhBcNie74DXpPV9y8ERPsiB0EedSU5GdrMzsUVEocz94jQwsqngnZbmcsfoOni+yUkQgN+bCA6S07M7cyCSIIkIerR+QEHoFtFVH4Txb+J+34nxjS2h2gwpY8jEz5xJ2XLZOx0h7Y+c74bjlIwnqkGeIT/jzY0frxRj5Fgj/4FkUxL1IVJEYUXBf5GywfYAoFpi3AG+YQDk7z50FeTqWawNRsA2k06s/PYRGWHgEZuS5ub1JAGUMjP2yjwXb5CmG6D7~-1~-1~1657849619',
    #     'bm_sv': 'B6C524D8DF3F4030542D18DF0F9F736A~YAAQB/ferSRfZe+BAQAAGDJT/xBQujR0kTxCCl0mQyl6r58gTtGlcuBKjmpT7yfuamC6X6wLIVwQi5De8Mjkd9y6RHXi62zl3DWC9GUFcEGwBsefqN7QpYL+552BmuSvitotWJ9l+cqXesCrJGYX1VbwEiJJm1ZDq0/PmPZMtj10SUZPfRePNaKcg5GbQqGHes/8r5o5RWOSN9At7ehLxDDYAeMOqFxrnR8kOvXCW96A76Vvw4xNH7Y+ZOvgcK4j~1',
    # }

    headers = {
        'authority': 'www.hilton.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer ' + accessToken,
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'rxVisitor=165476836305182I69K1TDOIPL0987NLILTNSJK53IJ5E; visitorId=83631778-39fc-4648-be43-ed719a680048; s_ecid=MCMID%7C06546371573000418848610851545713009555; _fbp=fb.1.1654768365673.1684450530; notice_preferences=0:; notice_gdpr_prefs=0:; cmapi_gtm_bl=ga-ms-ua-ta-asp-bzi-sp-awct-cts-csm-img-flc-fls-mpm-mpr-m6d-tc-tdc; cmapi_cookie_privacy=permit 1 required; forterToken=a3cdbc8197b546dc9985859da1ce85db_1657657384862_355_UAL9_9ck; AKA_A2=A; akacd_ohw_prd_external=3835298838~rv=30~id=1873aeee38fd2b0014a03c909f20ece1; ak_bmsc=A268E10C27F5FD2E072D060F5F4FE315~000000000000000000000000000000~YAAQB/ferSBNZe+BAQAAqQRT/xBmJoj4VWPf9+pqzX08dEAJxXUW/Io7w3tPepyQaTK1mu5L8+EOVhozZyYUcMTyipdP7xWCvCcRP1M6n9M6vAVLzOMPLb6nZWmzroTVmvTyE7xxlWAqTscS9t9zvh0DMN2VyYoRn+5cf2+/49VCVze6ZuLllxUltAlL1rgF1RDbS62EEI3YockCEfBHvGhbHEvEG/6QDx9GGpyG2El6FhXPCtV5UVJHvggm91zMPrPiQeBrL5XUcZqy0rjdNCNSTUSysq2lIKjFRpgAqUSTOYaCTp6XsaJgUT5oWeKd0AVMWs7APN08y9JqhSUzFpxQi//KMFULBxSo/HWt8iiC5zDyxe8vkRB4nuWbALHtTLNl7UAlDL4f; bm_sz=1878C10D8E6C55ADEF7C94DBF3B8F8C0~YAAQB/ferSFNZe+BAQAAqQRT/xBNypNQ9d47jiVp71AVq/S+2NhqJrOJyAiK9Dm/XpZX6FRki1rmKgYKq1cZl8yQiZuQDWiwwGrf71erHrWIKwt6AEWtPxHEGEKnDjPvE5y/L88D6RkgFLmLalMh8KAByuraww+jMGVrlwt5mg4ItWzBud34fVvDgaXIJReumvDVtPl8zD/WXv6ZtuqNpZUYB2UR+ncJuoxNGnl4v8OS2/PgrxKNL33yqSbKHI9MTktWeeyzVG8z3exy7CKqbgrxmTGomzIrChN5hLrXddDHmMU=~3289414~3621939; dtCookie=v_4_srv_1_sn_7FF7675D63A611C5D4E1E3A3C9419720_perc_100000_ol_0_mul_1_app-3A0da30f11c94bda74_1_rcs-3Acss_0; AMCVS_F0C120B3534685700A490D45%40AdobeOrg=1; AMCV_F0C120B3534685700A490D45%40AdobeOrg=1176715910%7CMCIDTS%7C19189%7CMCMID%7C06546371573000418848610851545713009555%7CMCAID%7CNONE%7CMCOPTOUT-1657853194s%7CNONE%7CvVersion%7C5.4.0; _abck=CC1753C5298A29861C2EE7E1336EB885~-1~YAAQB/ferSNfZe+BAQAAGDJT/wgKNIxMy8m2Vv0oK6GHUFVdjvNy18lGvGzzkhn/mcTOTDAjTfH510JBD+6N9/vazpg3qLwjh2bADhwMj2HSGAWvO7bPo6nctkL+C91heU68/aMEsepPARSYlaolfRXmMh1AV+sTofbpZqRw5uIGWF87FXnp5r8/eLm5NCF6Hev0+3wYsiNZsLhBcNie74DXpPV9y8ERPsiB0EedSU5GdrMzsUVEocz94jQwsqngnZbmcsfoOni+yUkQgN+bCA6S07M7cyCSIIkIerR+QEHoFtFVH4Txb+J+34nxjS2h2gwpY8jEz5xJ2XLZOx0h7Y+c74bjlIwnqkGeIT/jzY0frxRj5Fgj/4FkUxL1IVJEYUXBf5GywfYAoFpi3AG+YQDk7z50FeTqWawNRsA2k06s/PYRGWHgEZuS5ub1JAGUMjP2yjwXb5CmG6D7~-1~-1~1657849619; bm_sv=B6C524D8DF3F4030542D18DF0F9F736A~YAAQB/ferSRfZe+BAQAAGDJT/xBQujR0kTxCCl0mQyl6r58gTtGlcuBKjmpT7yfuamC6X6wLIVwQi5De8Mjkd9y6RHXi62zl3DWC9GUFcEGwBsefqN7QpYL+552BmuSvitotWJ9l+cqXesCrJGYX1VbwEiJJm1ZDq0/PmPZMtj10SUZPfRePNaKcg5GbQqGHes/8r5o5RWOSN9At7ehLxDDYAeMOqFxrnR8kOvXCW96A76Vvw4xNH7Y+ZOvgcK4j~1',
        'dx-platform': 'web',
        'hltclientmessageid': '83631778-39fc-4648-be43-ed719a680048-0fc037958dff4061b10b7ee24c8c845d',
        'origin': 'https://www.hilton.com',
        'referer': 'https://www.hilton.com/en/book/reservation/flexibledates/?ctyhocn=MLEONWA&arrivalDate=2022-10-01&departureDate=2022-10-02&room1NumAdults=2&brandCode=HH&inputModule=HOTEL_SEARCH&ohwDeepLinking=true&spec_plan=&specialRateTokens=&srpName=&displayCurrency=LOCAL&flexibleDates=true',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
        'visitorid': '83631778-39fc-4648-be43-ed719a680048',
    }

    params = {
        'appName': 'dx-reservations-ui',
        'ctyhocn': hotel,
        'language': 'en',
        'operationName': 'hotel_shopAvailOptions_shopCalendarPropAvail',
    }



    json_data = {
        'operationName': 'hotel_shopAvailOptions_shopCalendarPropAvail',
        'variables': {
            'arrivalDate': arrivalDate,
            'ctyhocn': hotel,
            'guestLocationCountry': 'US',
            'lengthOfStay': 1,
            'numAdults': 2,
            'numChildren': 0,
            'numRooms': 1,
            'language': 'en',
            'specialRates': {
                'hhonors': True,
                'aaa': False,
                'aarp': False,
                'corporateId': None,
                'familyAndFriends': False,
                'senior': False,
                'governmentMilitary': False,
                'groupCode': None,
                'offerId': None,
                'owner': False,
                'ownerHGV': False,
                'pnd': None,
                'promoCode': None,
                'teamMember': False,
                'travelAgent': False,
                'specialOffer': False,
                'specialOfferName': None,
            },
            'guestId': None,
            'offerId': None,
            'pnd': None,
            'displayCurrency': 'USD',
            'modifyingReservation': False,
            'childAges': [],
        },
        'query': 'query hotel_shopAvailOptions_shopCalendarPropAvail($arrivalDate: String!, $ctyhocn: String!, $language: String!, $guestLocationCountry: String, $numAdults: Int!, $numChildren: Int!, $numRooms: Int!, $displayCurrency: String, $lengthOfStay: Int!, $guestId: BigInt, $specialRates: ShopSpecialRateInput, $rateCategoryTokens: [String], $ratePlanCodes: [String], $offerId: BigInt, $pnd: String, $childAges: [Int], $modifyingReservation: Boolean) {\n  hotel(ctyhocn: $ctyhocn, language: $language) {\n    ctyhocn\n    shopAvailOptions(input: {offerId: $offerId, pnd: $pnd}) {\n      maxNumChildren\n      altCorporateAccount {\n        name\n        __typename\n      }\n      contentOffer {\n        name\n        __typename\n      }\n      __typename\n    }\n    shopCalendarAvail(\n      input: {guestLocationCountry: $guestLocationCountry, arrivalDate: $arrivalDate, displayCurrency: $displayCurrency, numAdults: $numAdults, numChildren: $numChildren, numRooms: $numRooms, lengthOfStay: $lengthOfStay, displayRateType: average, guestId: $guestId, specialRates: $specialRates, rateCategoryTokens: $rateCategoryTokens, ratePlanCodes: $ratePlanCodes, childAges: $childAges, modifyingReservation: $modifyingReservation}\n    ) {\n      statusCode\n      currencyCode\n      notifications {\n        subText\n        subType\n        title\n        text\n        __typename\n      }\n      calendars {\n        arrivalDate\n        arrivalDateFmt\n        departureDate\n        departureDateFmt\n        roomRate {\n          dailyRmPointsRate\n          dailyRmPointsRateFmt\n          depositAmount\n          depositAmountFmt\n          numRoomsAvail\n          rateAmount\n          rateAmountFmt(decimal: 0, strategy: trunc)\n          rateChangeIndicator\n          feeTransparencyIndicator\n          cmaTotalPriceIndicator\n          ratePlan {\n            confidentialRates\n            ratePlanName\n            ratePlanDesc\n            specialRateType\n            serviceChargesAndTaxesIncluded\n            __typename\n          }\n          ratePlanCode\n          roomTypeCode\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
    }

    json_result = ''
    
    #
    # TOR with Hilton returns 502 Bad Gateway
    #
    # Tor ProxyConnector
    #connector = ProxyConnector.from_url(configFile['tor']['proxy'], rdns=True)

    async with aiohttp.ClientSession(raise_for_status=True) as session:
        json_result = await req(session, 'https://www.hilton.com/graphql/customer', params, headers, json_data)
        # If the request returns an error repeat the request
        while 'errors' in str(json_result):
            json_result = await req(session, 'https://www.hilton.com/graphql/customer', params, headers, json_data)
        await session.close()
        
    print('----------------')
    print(''+month+' '+year)
    print('----------------')

    try:
        # Loop the the results
        for calendar in json_result['data']['hotel']['shopCalendarAvail']['calendars']:
            
            # Standard Room
            if calendar['roomRate']['ratePlan']['ratePlanName'] == 'Standard Room Reward':
                print('\n' + calendar['arrivalDate'] + ' - '  + calendar['roomRate']['ratePlan']['ratePlanName'])
            
            # Premium Room
            #if calendar['roomRate']['ratePlan']['ratePlanName'] == 'Premium Room Rewards':
            #    print('\n' + calendar['arrivalDate'] + ' - '  + calendar['roomRate']['ratePlan']['ratePlanName'])
    except:
        print("Error Occured: \n\n")
        print(str(json_result) + '\n\n')
        pass

    print('\n')

@backoff.on_exception(backoff.expo, aiohttp.ClientError, max_tries=20)
async def req(session, url, params, headers, json_data):
    async with session.post(url, params=params, headers=headers, json=json_data) as response:
        return await response.json()