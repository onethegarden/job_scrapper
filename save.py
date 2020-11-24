import csv

def save_to_file(jobs):
    #open up file
    file = open("jobs.csv", mode= "w", encoding='utf-8-sig')
    # 파이썬 unicodeEncodeError 문제, python은 기본적으로 unicode를 사용 
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
         #dictionary => list 로 변환
    return