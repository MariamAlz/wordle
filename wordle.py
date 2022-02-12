# importing csv module
import csv
import pandas as pd
import pyodbc
import numpy as np

# Import CSV
data = pd.read_csv (r'words.csv')   
df = pd.DataFrame(data)

# Connect to SQL Server
conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=MARIAM;'
                      'Database=master;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

#Server=localhost;Database=master;Trusted_Connection=True;

# Create Table
#cursor.execute('''
#		CREATE TABLE words (
#			words nvarchar(50),
#			);
 #              ''')

# Insert DataFrame to Table
#for row in df.itertuples():
 #   cursor.execute('''
  #              INSERT INTO master.dbo.words (words)
   #             VALUES (?)
    #            ''',
     #           row.words,
      #          )
#conn.commit()

def Wordle():
    global attempts, attempt, score, wordle_word
    attempts = 6
    attempt = 1
    score = ["" for x in range(attempts)]
    query = cursor.execute("SELECT TOP 1 words FROM words ORDER BY NEWID()")
    wordle_word = str(cursor.fetchall())[3:8]
    print(wordle_word)
    guessed_word = ["" for x in range(attempts)]
    while (attempt <= attempts):
        while (True):
            guessed_word[attempt - 1] = input(str(attempt) + ") Enter your word: ")
            if (len(guessed_word) != attempts):
                print ("Error! Only " + str(attempts) + " characters allowed!")
            else:
                break
        score[attempt - 1] = "xxxxx"
        i = 0
        while(i < 5):
            if (guessed_word[attempt - 1][i] == wordle_word[i]):
                    score[attempt - 1] = score[attempt - 1][:i] + 'o' + score[attempt - 1][i + 1:]
            i += 1
        j = 0
        freq_char = ""
        while (j < 5):
            if (wordle_word[j] in freq_char):
                j += 1
                continue
            freq_of_char = wordle_word.count(wordle_word[j])
            if (freq_of_char > 1):
                freq_char = wordle_word[j]
                lst_pos_of_char = []
                for pos, char in enumerate(wordle_word):
                    if(char == wordle_word[j]):
                        lst_pos_of_char.append(pos)
                k = 0
                for i in range(len(lst_pos_of_char)):
                    if (score[attempt - 1][lst_pos_of_char[i]] == 'o'):
                        k = k + 1
                if ((k == 0) and (wordle_word[j] in guessed_word[attempt - 1]) and ((guessed_word[attempt - 1].find(wordle_word[j]) in lst_pos_of_char))):
                    fst_pos_of_char = guessed_word[attempt - 1].find(guessed_word[attempt - 1][j])
                    score[attempt - 1] = score[attempt - 1][:fst_pos_of_char] + 'o' + score[attempt - 1][fst_pos_of_char + 1:]
                elif ((k == 0) and (wordle_word[j] in guessed_word[attempt - 1])):
                    fst_pos_of_char = guessed_word[attempt - 1].find(wordle_word[j])
                    print(fst_pos_of_char)
                    score[attempt - 1] = score[attempt - 1][:fst_pos_of_char] + 'z' + score[attempt - 1][fst_pos_of_char + 1:]
            else:
                if ((wordle_word[j] in guessed_word[attempt - 1]) and (wordle_word[j] != guessed_word[attempt - 1][j])):
                    fst_pos_of_char = guessed_word[attempt - 1].find(wordle_word[j])
                    score[attempt - 1] = score[attempt - 1][:fst_pos_of_char] + 'z' + score[attempt - 1][fst_pos_of_char + 1:]
            j += 1
        print(score[attempt - 1])
        if (score[attempt - 1] == "ooooo"):
            return()
        if (attempt == attempts):
            return()
        attempt = attempt + 1
Wordle()

def PrintScore():
    print("\nWordle " + str(attempt) + "/" + str(attempts))
    for i in range(attempts - 1):
        print(score[i])
    print("The Wordle word was " + wordle_word)
PrintScore()

cursor.close()
conn.close()