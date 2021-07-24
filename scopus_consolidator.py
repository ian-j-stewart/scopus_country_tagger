import pandas as pd
from os import listdir
from os.path import isfile, join
import sys
import csv
import numpy as np




mypath="C:/Users/ian_j/Downloads/scopus quantum"
onlyfiles = [f for f in listdir(r"C:/Users/ian_j/Downloads/scopus quantum") if isfile(join(mypath, f))]


print (onlyfiles)
readdf = (pd.DataFrame())
subset = (pd.DataFrame)
terms = ["carbon fib", "hypersonic", "scram", "ram jet", "tensorflow", "pressur water reactor", "pytorch", "quantum comput", "Unsymmetrical", "explos"]
countries =     ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan",            "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana"
             , "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Republic", "Chad", "Chile",
             "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark",
             "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
             "Ethiopia", "Fiji", "Finland", "France", "Gabon",  "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea",
             "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy",
             "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "North Korea", "South Korea", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos",
             "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia", "Madagascar", "Malawi",
             "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco",
             "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Burma", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand",
             "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines",
             "Poland", "Portugal", "Qatar",  "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
             "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia",
             "Slovenia", "Solomon Islands", "Somalia", "South Africa", "Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Swaziland",
             "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia",
             "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay",
             "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]




for files in onlyfiles:
    if 'csv' in files:
        print (files)
        print ('next', files)
        readdf = pd.read_csv(r"C:\Users\ian_j\Downloads\scopus quantum\\/"+files, encoding="utf-8", delimiter=",", error_bad_lines=False)
                             #+ files, header=0, quotechar='"', escapechar='\\' )

        readdf = readdf.replace('\\', '')
        fileheaders = (readdf.columns.values.tolist())
        fileheaders = fileheaders+["filename"] +terms +countries


        print (fileheaders)
        readdf.reindex(columns=fileheaders)



        readdf["filename"]=files


        for c in countries:
            country = c


            readdf[c] = 'FALSE'
            #print (readdf)

            readdf.loc[(readdf['Authors with affiliations'].str.contains(c) == True), [country]] = 'True'

            #readdf[countery] = readdf[country].loc[readdf['Authors with affiliations'].str.contains(country) == True]

            print (c)
            #print (filtered)
            #readdf.loc[readdf['Authors with affiliations'].str.contains(country), "China"] = 'Yes'
            readdf.filter(fileheaders)
            readdf = readdf.replace('\\', '')

        fileheaders= readdf.columns.tolist()
            #print ("fileheaders written", fileheaders)

        readdf.to_csv(r"C:\Users\ian_j\Downloads\scopus quantum\\/" + files, columns=fileheaders)



            #print ("trying combine")

