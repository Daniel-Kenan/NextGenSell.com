import os
import sqlite3
import psycopg2
from urllib.parse import urlparse
import tkinter as tk
from tkinter import messagebox, scrolledtext

class DataTransferApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Transfer")
        self.root.geometry("500x400")

        self.label_from = tk.Label(root, text="Transfer From:")
        self.label_from.pack()
        self.from_var = tk.StringVar(root)
        self.from_var.set("SQLite")  # Default value
        self.dropdown_from = tk.OptionMenu(root, self.from_var, "SQLite", "PostgreSQL")
        self.dropdown_from.pack()

        self.label_to = tk.Label(root, text="Transfer To:")
        self.label_to.pack()
        self.to_var = tk.StringVar(root)
        self.to_var.set("PostgreSQL")  # Default value
        self.dropdown_to = tk.OptionMenu(root, self.to_var, "SQLite", "PostgreSQL")
        self.dropdown_to.pack()

        self.label_sqlite = tk.Label(root, text="SQLite Database Path:")
        self.label_sqlite.pack()
        self.entry_sqlite = tk.Entry(root)
        self.entry_sqlite.pack()

        self.label_postgres_url = tk.Label(root, text="PostgreSQL Database URL:")
        self.label_postgres_url.pack()
        self.entry_postgres_url = tk.Entry(root)
        self.entry_postgres_url.pack()

        self.log_text = scrolledtext.ScrolledText(root, width=60, height=10)
        self.log_text.pack()

        self.transfer_button = tk.Button(root, text="Transfer Data", command=self.transfer_data)
        self.transfer_button.pack()

    def log_message(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update()

    def transfer_data(self):
        transfer_from = self.from_var.get()
        transfer_to = self.to_var.get()

        if transfer_from == "SQLite":
            source = "SQLite"
            source_path = self.entry_sqlite.get()
            if not os.path.exists(source_path):
                messagebox.showerror("Error", "SQLite database path does not exist.")
                return
        else:
            source = "PostgreSQL"
            source_url = self.entry_postgres_url.get()
            if not source_url:
                messagebox.showerror("Error", "PostgreSQL database URL is empty.")
                return

        if transfer_to == "SQLite":
            destination = "SQLite"
            destination_path = self.entry_sqlite.get()
            if not os.path.exists(destination_path):
                messagebox.showerror("Error", "SQLite database path does not exist.")
                return
        else:
            destination = "PostgreSQL"
            destination_url = self.entry_postgres_url.get()
            if not destination_url:
                messagebox.showerror("Error", "PostgreSQL database URL is empty.")
                return

        try:
            self.log_message("Starting data transfer...")
            if source == "SQLite":
                source_conn = sqlite3.connect(source_path)
                source_cursor = source_conn.cursor()
            else:
                url_parts = urlparse(source_url)
                source_host = url_parts.hostname
                source_port = url_parts.port
                source_dbname = url_parts.path[1:]
                source_user = url_parts.username
                source_password = url_parts.password

                source_conn = psycopg2.connect(
                    host=source_host,
                    port=source_port,
                    dbname=source_dbname,
                    user=source_user,
                    password=source_password
                )
                source_cursor = source_conn.cursor()

            if destination == "SQLite":
                destination_conn = sqlite3.connect(destination_path)
                destination_cursor = destination_conn.cursor()
            else:
                url_parts = urlparse(destination_url)
                destination_host = url_parts.hostname
                destination_port = url_parts.port
                destination_dbname = url_parts.path[1:]
                destination_user = url_parts.username
                destination_password = url_parts.password

                destination_conn = psycopg2.connect(
                    host=destination_host,
                    port=destination_port,
                    dbname=destination_dbname,
                    user=destination_user,
                    password=destination_password
                )
                destination_cursor = destination_conn.cursor()

            source_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = source_cursor.fetchall()

            for table in tables:
                table_name = table[0]
                source_cursor.execute(f"SELECT * FROM {table_name};")
                rows = source_cursor.fetchall()

                if destination == "PostgreSQL":
                    destination_cursor.execute(f"SELECT * FROM {table_name};")
                    existing_records = destination_cursor.fetchall()
                    existing_records_set = set(existing_records)

                self.log_message(f"Transferring data from {source} to {destination} for table: {table_name}...")
                for row in rows:
                    if destination == "PostgreSQL" and tuple(row) not in existing_records_set:
                        placeholders = ','.join(['%s'] * len(row))
                        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
                        destination_cursor.execute(insert_query, row)
                    elif destination == "SQLite":
                        placeholders = ','.join(['?'] * len(row))
                        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
                        destination_cursor.execute(insert_query, row)

            if destination == "PostgreSQL":
                destination_conn.commit()
            else:
                destination_conn.commit()
            self.log_message("Data transfer completed successfully.")
        except Exception as e:
            self.log_message(f"Error: {str(e)}")
        finally:
            if source_conn:
                source_conn.close()
            if destination_conn:
                destination_conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = DataTransferApp(root)
    root.mainloop()
