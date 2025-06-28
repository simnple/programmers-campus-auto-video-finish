import requests

URL = "https://campus.programmers.co.kr"

class ProgrammersAPI():
    def __init__(self, campus_id: int, token: str):
        self.campus_id = str(campus_id)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            "Cookie": token
        }
    
    def get_curriculum(self):
        response = requests.get(URL + f"/api/school/courses/{self.campus_id}/curriculum", headers=self.headers)
        return response.json()

    def get_part(self, part_id):
        response = requests.get(URL + f"/api/school/courses/{self.campus_id}/curriculum/parts/{part_id}", headers=self.headers)
        return response.json()

    def finish_video(self, lesson_id):
        data = {"courseFinished": False}
        response = requests.patch(URL + f"/api/v1/school/courses/{self.campus_id}/lessons/{lesson_id}/finish", headers=self.headers, json=data)
        return response.status_code
