from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import string
import random


def createRandomDateTimestamp():
    start_date = datetime.date(1990, 1, 1)
    end_date = datetime.date(2022, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    # generate timestamp
    return random_date.strftime('%s')


@csrf_exempt
def eventAPI(request):
    # msg match id
    matchid = random.randint(1, 10000)

    # generate alphanumeric string
    S = 25  # number of char
    msgId = ''.join(random.choices(string.ascii_lowercase + string.digits, k=S))

    # generate random timestamp
    timestamp = createRandomDateTimestamp()
    custom_msg = {}
    if request.method == 'POST':
        msgType = request.POST['type']

        # custom
        metadata = {
            "message_id": msgId
        }

        custom_msg = {
            "date": timestamp,
            "type": msgType,
            "metadata": metadata
        }

        if msgType == "message.created":
            metadata['match_id'] = matchid
        elif msgType == "message.replied":
            metadata['match_id'] = matchid
        else:   # message.bounced
            pass

    return JsonResponse({"message": custom_msg})
