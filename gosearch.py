import requests
import csv
import random
result = requests.get(
        'http://hp-api.herokuapp.com/api/characters')
print(result)
data = result.json()
length_data= len(data)-1
print('there are {} people in total'.format(length_data))
print(data)


def choose_house(students):
    random_house = ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']
    students = students

    chosen_house = random.choice(random_house)
    chosen_student = random.choice(students)

    print('Who sits under the sorting hat next? {}'.format(chosen_student))
    print('Which house are they in? {}'.format(chosen_house))
def read_data(file_name):
    data = []

    with open(file_name, 'r') as file_csv:
        spreadsheet = csv.DictReader(file_csv)
        for row in spreadsheet:
            data.append(row)
    return data
def run(position):
    data = read_data(file_name)
    age = []
    for row in data:
        row['yearOfBirth']=2019-int(row['yearOfBirth'])
        newage = int(row['yearOfBirth'])
        age.append(newage)
        average = sum(age)/len(data)
        average=int(average)
    for row in data:
        if row['yearOfBirth']==min(age):
             print('{} is the youngest'.format(row['name']))
        if row['yearOfBirth']==max(age):
             print('{} is the oldest'.format(row['name']))
    print('There are {} {} in total,average age of student is {} the smallest one is {},the oldest one is {}'.format(len(data),position,average,min(age),max(age)), )
data_to_file = open('Teacher_file.csv', 'w')
csv_writer = csv.writer(data_to_file)
csv_writer.writerow(['name', 'species', 'gender',  'yearOfBirth', 'eyeColour', 'hairColour'])
# teacher write row
sdata_to_file = open('Student_file.csv', 'w')
csv_writers = csv.writer(sdata_to_file)
csv_writers.writerow(['name', 'species', 'gender',  'yearOfBirth', 'eyeColour', 'hairColour'])
# student writew head row
for i in range(0, length_data):
        meetup = data[i]
        if meetup['yearOfBirth'] != '':
                name = meetup['name']
                species = meetup['species']
                gender = meetup['gender']
                yearOfBirth = meetup['yearOfBirth']
                eyeColour = meetup['eyeColour']
                hairColour = meetup['hairColour']
                if meetup['hogwartsStudent'] == True:
                        csv_writers.writerow([name, species,gender,yearOfBirth,eyeColour,hairColour])
                else:
                        csv_writer.writerow([name, species, gender, yearOfBirth, eyeColour, hairColour])
data_to_file.close()
sdata_to_file.close()
#read data and find the students
Data_show = input('which data do you want to check')
if Data_show=='student':
        file_name='Student_file.csv'
        run(position="student")
        data = read_data(file_name)
        students = []

        for row in data:
            student = row['name']
            students.append(student)
        print(students)
        choose_house(students)
else:
    file_name = 'Teacher_file.csv'
    run(position='teacher')