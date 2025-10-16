from diaries.AbstractDiary import AbstractDiary

class ArakaDiary(AbstractDiary):

    def get_date(self):
        return "2025-10-16"
    
    def get_summary(self):
        return "素晴らしい1日だった"
    
    def get_author(self):
        return "Araka"