from tkinter import *
from tkinter import ttk
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String, nullable=False)
    year = Column(Integer)
    director = Column(String)
    writer = Column(String)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def submit_new_movie(*args):
    new_movie = Movie(title=title_var.get(), year=year_var.get(), director=director_var.get(), writer=writer_var.get())
    session = Session()
    session.add(new_movie)
    session.commit()
    clear_form()
    tree.insert("", 'end', text=new_movie.id, values=(new_movie.title, new_movie.year, new_movie.director, new_movie.writer))


def edit_movie(*args):
    session = Session()
    print(tree.item(tree.selection())['text'])
    movie = session.query(Movie).filter_by(id=tree.item(tree.selection())['text']).first()
    movie.title = title_var.get()
    movie.year = year_var.get()
    movie.director = director_var.get()
    movie.writer = writer_var.get()
    session.add(movie)
    session.commit()
    clear_form()
    tree.item(tree.selection(), text=movie.id, values=(movie.title, movie.year, movie.director, movie.writer))


def clear_form():
    title_var.set("")
    year_var.set("")
    director_var.set("")
    writer_var.set("")


def open_new_movie_window(*args):
    t = Toplevel(root)
    t.title("Add new movie")

    content = ttk.Frame(t)
    title_lbl = ttk.Label(content, text="Title")
    year_lbl = ttk.Label(content, text="Year of production")
    director_lbl = ttk.Label(content, text="Director")
    writer_lbl = ttk.Label(content, text="Writer")

    title = ttk.Entry(content, textvariable=title_var)
    year = ttk.Entry(content, textvariable=year_var)
    director = ttk.Entry(content, textvariable=director_var)
    writer = ttk.Entry(content, textvariable=writer_var)

    submit_btn = ttk.Button(content, command=submit_new_movie, text="Submit")
    cancel_btn = ttk.Button(content, command=t.destroy, text="Cancel")

    content.grid(column=0, row=0, padx=5, pady=5)
    title_lbl.grid(column=0, row=0, padx=5, pady=5)
    title.grid(column=1, row=0, padx=5, pady=5)
    year_lbl.grid(column=0, row=1, padx=5, pady=5)
    year.grid(column=1, row=1, padx=5, pady=5)
    director_lbl.grid(column=0, row=2, padx=5, pady=5)
    director.grid(column=1, row=2, padx=5, pady=5)
    writer_lbl.grid(column=0, row=3, padx=5, pady=5)
    writer.grid(column=1, row=3, padx=5, pady=5)

    submit_btn.grid(column=0, row=4, padx=5, pady=5)
    cancel_btn.grid(column=1, row=4, padx=5, pady=5)


def on_select(event):
    t = Toplevel(root)
    t.title("Edit movie")

    content = ttk.Frame(t)
    title_lbl = ttk.Label(content, text="Title")
    year_lbl = ttk.Label(content, text="Year of production")
    director_lbl = ttk.Label(content, text="Director")
    writer_lbl = ttk.Label(content, text="Writer")

    title = ttk.Entry(content, textvariable=title_var)
    year = ttk.Entry(content, textvariable=year_var)
    director = ttk.Entry(content, textvariable=director_var)
    writer = ttk.Entry(content, textvariable=writer_var)
    item = tree.selection()
    vals = tree.item(item)['values']
    title_var.set(vals[0])
    year_var.set(vals[1])
    director_var.set(vals[2])
    writer_var.set(vals[3])

    submit_btn = ttk.Button(content, command=edit_movie, text="Submit")
    cancel_btn = ttk.Button(content, command=t.destroy, text="Cancel")

    content.grid(column=0, row=0, padx=5, pady=5)
    title_lbl.grid(column=0, row=0, padx=5, pady=5)
    title.grid(column=1, row=0, padx=5, pady=5)
    year_lbl.grid(column=0, row=1, padx=5, pady=5)
    year.grid(column=1, row=1, padx=5, pady=5)
    director_lbl.grid(column=0, row=2, padx=5, pady=5)
    director.grid(column=1, row=2, padx=5, pady=5)
    writer_lbl.grid(column=0, row=3, padx=5, pady=5)
    writer.grid(column=1, row=3, padx=5, pady=5)

    submit_btn.grid(column=0, row=4, padx=5, pady=5)
    cancel_btn.grid(column=1, row=4, padx=5, pady=5)


if __name__ == '__main__':

    root = Tk()
    root.title("Movies database")
    root.geometry("710x710")

    title_var = StringVar()
    year_var = StringVar()
    director_var = StringVar()
    writer_var = StringVar()

    content = ttk.Frame(root)
    content.grid(row=0, column=0)
    add_new_movie_btn = ttk.Button(content, text="Add new movie", command=open_new_movie_window)
    add_new_movie_btn.grid(row=0, column=0, padx=10, pady=10)

    tree = ttk.Treeview(root)
    tree["columns"] = ("title", "year", "director", "writer")
    tree.column("#0", width=40)
    tree.column("title", width=270)
    tree.column("year", width=60)
    tree.column("director", width=170)
    tree.column("writer", width=170)

    tree.heading("#0", text="No.", anchor=W)
    tree.heading("title", text="Title", anchor=W)
    tree.heading("year", text="Year", anchor=W)
    tree.heading("director", text="Director", anchor=W)
    tree.heading("writer", text="Writer", anchor=W)

    session = Session()
    for instance in session.query(Movie).order_by(Movie.id):
        tree.insert("", 'end', text=instance.id,
                    values=(instance.title, instance.year, instance.director, instance.writer))

    tree.bind("<<TreeviewSelect>>", on_select)
    tree.grid(column=0, row=1)

    root.mainloop()


