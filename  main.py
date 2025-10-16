from diaries.DiarySample import DiarySample
from diaries.AmanoDiary import AmanoDiary
from diaries.ZhengHaotianDiary import ZhengHaotianDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    AmanoDiary(),
    ZhengHaotianDiary(),
    ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()