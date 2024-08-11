from os import system
from json import dumps

"""
men bu matnni yozishimdan maqsad , bu narsa git hubda ham o'zgarishini ko'rish uchun 
"""
system("cls")


fayl = open("ishga_kirgan.txt", "r", encoding="utf-8")
odamlar = []


datalar = fayl.read().strip().split("\n")


natija_file = open("employes1.txt", 'w', encoding='utf-8')

for person in datalar:
    person = person.split(",")

    
    person_data_birth = [int(date) for date in person[3].split("-")]
    person_data_work = [int(date) for date in person[4].split("-")]

    
    person_data = {
        "fullname": person[0],   
        "gender": person[1],
        "country": person[2],
        "birth date": person_data_birth, 
        "work date": person_data_work     
    }

   
    odamlar.append(person_data)

    
    work_year = person_data["work date"][2]
    birth_year=person_data["birth date"][2]
    if work_year-birth_year > 18:
        natija_file.write(dumps(person_data, ensure_ascii=False) + "\n")


print(dumps(odamlar, indent=4, ensure_ascii=False))


fayl.close()
natija_file.close()



"men bu o'zgarishni globlani qildim . bundan asosiy maqsad => bu o'zgarishni local ko'rmoqchiman "
