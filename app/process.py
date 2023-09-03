from . import models

def calculate_ecg(ecg: models.Ecg) -> dict:
    res = {}

    for lead in ecg.leads:
        for i in range(len(lead.signal) -1):
            if not lead.name in res:
                res[lead.name] = 0
            if lead.signal[i] > 0 and lead.signal[i+1] < 0:
                res[lead.name] += 1
            if lead.signal[i] < 0 and lead.signal[i+1] > 0:
                res[lead.name] += 1

    return res

