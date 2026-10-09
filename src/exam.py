class Exam:
    def __init__(self, exam_id, course, title, date):
        self.exam_id = exam_id
        self.course = course
        self.title = title
        self.date = date

    def get_date(self):
        return self.date

    def get_details(self):
        return {
            "exam_id": self.exam_id,
            "course": self.course,
            "title": self.title,
            "date": self.date
        }