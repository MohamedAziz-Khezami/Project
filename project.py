import csv
import pandas as pd
from tabulate import tabulate
import os
import matplotlib.pyplot as plt

def revenue():
    try:
        x = int(input("How much did you make? "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    t = input("What is the source of your revenue? ")
    file_path = "tracker.csv"


    df = pd.read_csv(file_path)


    if t in df['Type'].values:

        df.loc[df['Type'] == t, 'Revenues'] += x
    else:

        new_row = {'Revenues': x, 'Expenses': 0, 'Type': t}
        df = pd.concat([df, pd.DataFrame([new_row], columns=df.columns)], ignore_index=True)


    df.to_csv(file_path, index=False)

def expenses():
    try:
        x = int(input("How much did you spend? "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    t = input("What kind of expenses did you spend on? ")
    file_path = "tracker.csv"


    df = pd.read_csv(file_path)


    if t in df['Type'].values:

        df.loc[df['Type'] == t, 'Expenses'] += x
    else:

        new_row = {'Revenues': 0, 'Expenses': x, 'Type': t}
        df = pd.concat([df, pd.DataFrame([new_row], columns=df.columns)], ignore_index=True)


    df.to_csv(file_path, index=False)


def display_graphs():
    file_path = 'tracker.csv'
    df = pd.read_csv(file_path)

    print("Displaying multiple types of graphs:")
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 8))
    df.plot(kind='bar', x='Type', y=['Revenues', 'Expenses'], rot=0, ax=axes[0, 0])
    axes[0, 0].set_xlabel('Type')
    axes[0, 0].set_ylabel('Amount')
    axes[0, 0].set_title('Revenues and Expenses (Bar Chart)')
    axes[0, 0].legend(['Revenues', 'Expenses'])
    df.plot(x='Type', y=['Revenues', 'Expenses'], marker='o', ax=axes[0, 1])
    axes[0, 1].set_xlabel('Type')
    axes[0, 1].set_ylabel('Amount')
    axes[0, 1].set_title('Revenues and Expenses (Line Chart)')
    axes[0, 1].legend(['Revenues', 'Expenses'])
    axes[0, 1].grid(True)
    axes[1, 0].scatter(df['Revenues'], df['Expenses'])
    axes[1, 0].set_xlabel('Revenues')
    axes[1, 0].set_ylabel('Expenses')
    axes[1, 0].set_title('Revenues vs Expenses (Scatter Plot)')
    axes[1, 0].grid(True)
    total_revenues = df['Revenues'].sum()
    total_expenses = df['Expenses'].sum()
    labels = ['Revenues', 'Expenses']
    sizes = [total_revenues, total_expenses]
    axes[1, 1].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    axes[1, 1].axis('equal')
    axes[1, 1].set_title('Total Revenues vs Total Expenses (Pie Chart)')
    axes[2, 0].hist(df['Revenues'], bins=10, alpha=0.5, color='blue', label='Revenues')
    axes[2, 0].set_xlabel('Revenues')
    axes[2, 0].set_ylabel('Frequency')
    axes[2, 0].set_title('Distribution of Revenues (Histogram)')
    axes[2, 0].legend()
    axes[2, 0].grid(True)
    axes[2, 1].hist(df['Expenses'], bins=10, alpha=0.5, color='red', label='Expenses')
    axes[2, 1].set_xlabel('Expenses')
    axes[2, 1].set_ylabel('Frequency')
    axes[2, 1].set_title('Distribution of Expenses (Histogram)')
    axes[2, 1].legend()
    axes[2, 1].grid(True)
    plt.tight_layout()
    plt.show()
def delete_row():
    file_path = 'tracker.csv'
    df = pd.read_csv(file_path)
    print(tabulate( df,headers='keys', tablefmt='grid', showindex=False))
    try:
        row_to_delete = int(input("Enter the row number to delete: "))  -1
        if 0 <= row_to_delete <= len(df):
            df = df.drop(index=row_to_delete)
            df.to_csv(file_path, index=False)
            print("Row deleted successfully.")
        else:
            print("Invalid row number.")
    except ValueError:
        print("Invalid input. Please enter a valid row number.")




def delete_file():
    file_path = 'tracker.csv'
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"The file {file_path} has been deleted.")
    else:
        print(f"The file {file_path} does not exist.")





def main():
    file_path = "tracker.csv"
    if not os.path.isfile(file_path):
        with open("tracker.csv", 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Revenues', 'Expenses', 'Type'])
            writer.writeheader()
    while True:
        print("If you want to save a revenue type R.\nIf you want to save an expense type X.\nTo show the file, type F.\nTo delete a row in the table, type in D.\nTo show graphs of the your tracking so far, type G\n🚨To delete your entire file type: ⚠️ DELETE FILE⚠️.🚨")
        transaction = input().lower()

        if transaction == "r":
            revenue()

        elif transaction == "x":
            expenses()

        elif transaction == "f":
            file_path = 'tracker.csv'
            df = pd.read_csv(file_path)
            headers = df.columns.tolist()
            table = tabulate(df,headers=headers, tablefmt='pretty', showindex=False)
            print(table+"\n This table is saved in a file called tracker.csv.")
        elif transaction == "d":
            delete_row()
        elif transaction == "g":
            display_graphs()
        elif transaction == "delete file":
            delete_file()
        else:
            continue

if __name__ == "__main__":
    main()

