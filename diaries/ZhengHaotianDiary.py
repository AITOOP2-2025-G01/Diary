from diaries.AbstractDiary import AbstractDiary

class ZhengHaotianDiary(AbstractDiary):

    def get_date(self):
        return "2025-10-16"
    
    def get_summary(self):
        return "Git<strike>難しすぎる</strike><ins>簡単</ins>"
    
    def get_author(self):
        return "ZhengHaotian"