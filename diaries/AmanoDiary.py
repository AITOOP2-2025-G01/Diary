from diaries.AbstractDiary import AbstractDiary

class AmanoDiary(AbstractDiary):

    def get_date(self):
        return "2025-10-16"
    
    def get_summary(self):
        return "オブジェクト難しすぎー この先やっていけるのかな？"
    
    def get_author(self):
        return "Amano"