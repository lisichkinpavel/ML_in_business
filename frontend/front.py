import tkinter as tk
from tkinter import messagebox as mb
import requests


def get_entry():
    post_dict = {"CreditScore": float(credit_score.get()),
                 "Geography": str(geography.get()),
                 "Gender": str(gender.get()),
                 "Age": int(age.get()),
                 "Tenure": float(tenure.get()),
                 "Balance": float(balance.get()),
                 "NumOfProducts": int(num_of_products.get()),
                 "HasCrCard": int(has_cr_card.get()),
                 "IsActiveMember": int(is_active_member.get()),
                 "EstimatedSalary": float(estimated_salary.get())}

    print(post_dict)
    myurl = server_url.get() + '/predict'
    headers = {'content-type': 'application/json; charset=utf-8'}
    response = requests.post(myurl, json=post_dict, headers=headers)
    print(response.json()['predictions'])
    mb.showinfo(title='Prediction', message=f"Prediction {response.json()['predictions']}")


features = ['CreditScore',
            'Geography',
            'Gender',
            'Age',
            'Tenure',
            'Balance',
            'NumOfProducts',
            'HasCrCard',
            'IsActiveMember',
            'EstimatedSalary']

win = tk.Tk()
win.geometry(f'300x370+100+200')
win.title('Predictor')

for idx, name in enumerate(features):
    tk.Label(win, text=name).grid(row=idx, column=0, stick='w')

credit_score = tk.Entry(win, textvariable='0')
credit_score.insert(0, '0')
credit_score.grid(row=0, column=1)

geography = tk.Entry(win)
geography.grid(row=1, column=1)
geography.insert(0, 'None')

gender = tk.Entry(win)
gender.grid(row=2, column=1)
gender.insert(0, 'None')

age = tk.Entry(win)
age.grid(row=3, column=1)
age.insert(0, '0')

tenure = tk.Entry(win)
tenure.grid(row=4, column=1)
tenure.insert(0, '0')

balance = tk.Entry(win)
balance.grid(row=5, column=1)
balance.insert(0, '0')

num_of_products = tk.Entry(win)
num_of_products.grid(row=6, column=1)
num_of_products.insert(0, '0')

has_cr_card = tk.Entry(win)
has_cr_card.grid(row=7, column=1)
has_cr_card.insert(0, '0')

is_active_member = tk.Entry(win)
is_active_member.grid(row=8, column=1)
is_active_member.insert(0, '0')

estimated_salary = tk.Entry(win)
estimated_salary.grid(row=9, column=1)
estimated_salary.insert(0, '0')

tk.Label(win, text='Server url:').grid(row=12, column=0, columnspan=2, stick='we')
server_url = tk.Entry(win, justify='center')
server_url.grid(row=13, column=0, columnspan=2, stick='we')
server_url.insert(0, '-> Paste server url here <-')


def some_callback(event):  # note that you must include the event as an arg, even if you don't use it.
    server_url.delete(0, "end")
    return None


server_url.bind("<Button-1>", some_callback)

tk.Button(win, text='Get prediction', command=get_entry).grid(row=11, column=0, columnspan=2, stick='we')

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(0, minsize=100)

win.mainloop()
