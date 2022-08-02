# -- coding: utf-8 --
"""

Created on: 30/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import csv

with open('staff.csv', 'w') as csvfile:
    fieldnames = ['name', 'city', 'date_of_birth', 'start_date', 'salary',
                  'departament']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'name': 'John Doe',
                     'city': 'Houston, TX',
                     'date_of_birth': '1998-11-04',
                     'start_date': '2018-08-11',
                     'salary': '$65000',
                     'departament': 'Accounting'})
    writer.writerow({'name': 'Jane Doe',
                     'city': 'San Jose, CA',
                     'date_of_birth': '1995-08-05',
                     'start_date': '2017-08-24',
                     'salary': '$70000',
                     'departament': 'Field Quality'})
    writer.writerow({'name': 'Matt smith',
                     'city': 'Dallas, TX',
                     'date_of_birth': '1996-11-25',
                     'start_date': '2020-04-16',
                     'salary': '$58000',
                     'departament': 'human resources'})
    writer.writerow({'name': 'Ashley Harris',
                     'city': 'Miami, FL',
                     'date_of_birth': '1995-01-08',
                     'start_date': '2021-02-11',
                     'salary': '$49500',
                     'departament': 'accounting'})
    writer.writerow({'name': 'Jonathan target',
                     'city': 'Santa Clara, CA',
                     'date_of_birth': '1998-08-14',
                     'start_date': '2020-09-01',
                     'salary': '$62000',
                     'departament': 'field quality'})
    writer.writerow({'name': 'Hale Cole',
                     'city': 'Atlanta, GA',
                     'date_of_birth': '2000-10-24',
                     'start_date': '2021-10-20',
                     'salary': '$54500',
                     'departament': 'engineering'})

    print("datos insertados")
