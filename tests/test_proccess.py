from app import process
from app import models

def test_calculate_ecgs():
    ecg = models.Ecg(
        id = "test",
        date = "1 september 2023",
        leads = [
            models.Lead(
                name = "lead1",
                signal = [-1, 1, -2, 2, 2, -1]
            )
        ]
    )

    res = process.calculate_ecg(ecg)

    assert len(res) == 1
    assert res['lead1'] == 4

