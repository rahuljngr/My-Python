import mysql.connector
from difflib import get_close_matches
 
a = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)
 
cursor=a.cursor()
 
word = input("Enter a word:  ")
query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()
 
if results:
    for result in results:
        print(result[0])
elif len(get_close_matches(word ,results.Expression)) > 0:
    k = input("Did you mean %s instead . Enter Y if yes and N if no : " % get_close_matches(word , results.Expression()))
    if k =='Y':
        print(results[get_close_matches( word ,results.Expression())])
    elif k =='N':
        print("The word doesnt exist.")
    else:
        print("Error!!")
else:
    print("The word doesnt exist")