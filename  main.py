from diaries.DiarySample import DiarySample
from diaries.k21003Diary import k21003Diary
from diaries.AmanoDiary import AmanoDiary
from diaries.ZhengHaotianDiary import ZhengHaotianDiary
from diaries.ArakaDiary import ArakaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    k21003Diary(),
    AmanoDiary(),
    ZhengHaotianDiary(),
    ArakaDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()