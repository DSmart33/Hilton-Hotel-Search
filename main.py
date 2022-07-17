import requests
import asyncio

from request.get.get_token import get_accessToken
from request.get.get_dates import get_dates

async def main():

    hotels = {
        'Waldorf Astoria Maldives Ithaafushi': 'MLEONWA',
        'Conrad Maldives Rangali Island': 'MLEHICI',
        'Grand Wailea, A Waldorf Astoria Resort': 'JHMGWWA',
        'Ho\'olei at Grand Wailea': 'OGGHOWA',
        'Conrad Bora Bora Nui': 'PPTBNCI',
        'Hilton Moorea Lagoon Resort and Spa': 'PPTMLHH',
        'Waldorf Astoria Los Cabos Pedregal': 'SJDWAWA',
        'Conrad Koh Samui': 'USMKSCI',
        'Sea Breeze Santorini Beach Resort, Curio Collection by Hilton': 'JTRSBQQ',
        'The Royal Senses Resort & Spa Crete, Curio Collection by Hilton': 'HERRSQQ'
        
    }

    #
    # Hotel IDs
    #
    # hotel_name = 'Maldives WA'
    # hotel = 'MLEONWA'
    #
    # hotel_name = 'Maldives Conrad'
    # hotel = 'MLEHICI'
    #
    # hotel_name = 'Grand Wailea'
    # hotel = 'JHMGWWA'
    #
    # hotel_name = ''
    # hotel = ''

    for hotel in hotels:

        print('---------------------------------------------------------------------')
        print('                          '+hotel+'                              ')
        print('---------------------------------------------------------------------')

        #
        #   November
        #
        arrivalDate = '2022-11-01'
        month = 'November'
        year = '2022'

        # Get a new token
        accessToken = await get_accessToken()

        await asyncio.sleep(5)

        # Request Dates
        await get_dates(accessToken, hotels[hotel], arrivalDate, month, year)

        await asyncio.sleep(5)

        #
        #   December
        #
        arrivalDate = '2022-12-01'
        month = 'December'
        year = '2022'

        # Get a new token
        accessToken = await get_accessToken()

        await asyncio.sleep(5)

        # Request Dates
        await get_dates(accessToken, hotels[hotel], arrivalDate, month, year)

        await asyncio.sleep(5)

        #
        #   January
        #
        arrivalDate = '2023-01-01'
        month = 'January'
        year = '2023'

        # Get a new token
        accessToken = await get_accessToken()

        await asyncio.sleep(5)

        # Request Dates
        await get_dates(accessToken, hotels[hotel], arrivalDate, month, year)

        await asyncio.sleep(5)

        #
        #   February
        #
        arrivalDate = '2023-02-01'
        month = 'February'
        year = '2023'

        # Get a new token
        accessToken = await get_accessToken()

        await asyncio.sleep(5)

        # Request Dates
        await get_dates(accessToken, hotels[hotel], arrivalDate, month, year)

        await asyncio.sleep(5)

        #
        #   March
        #
        arrivalDate = '2023-03-01'
        month = 'March'
        year = '2023'

        # Get a new token
        accessToken = await get_accessToken()

        await asyncio.sleep(5)

        # Request Dates
        await get_dates(accessToken, hotels[hotel], arrivalDate, month, year)

        await asyncio.sleep(5)

        #
        #   April
        #
        arrivalDate = '2023-04-01'
        month = 'April'
        year = '2023'

        # Get a new token
        accessToken = await get_accessToken()

        await asyncio.sleep(5)

        # Request Dates
        await get_dates(accessToken, hotels[hotel], arrivalDate, month, year)

        await asyncio.sleep(5)

        print('\n\n')


if __name__ == '__main__':
    # set another loop implementation:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())