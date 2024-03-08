import mysql.connector
import tkinter as tk
from tkinter import messagebox, PhotoImage

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",  # replace with your mysql password
    database="your_database_name"  # replace with your database in mysql
)
cursor = db.cursor()

# Create the main application window
root = tk.Tk()
root.title("Movie Recommendation System")

background_image = PhotoImage(file="6cy5E8jEi.gif")  # Replace with your image file's name and path

# Create a label to display the background image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Set the label to cover the entire window


# Function to set style for widgets
def set_style(widget, white, blue):
    widget.configure(bg=white, fg=blue)


# Function to register a user
def register_user():
    user_window = tk.Toplevel(root)
    user_window.title("User Registration")
    user_window.geometry("400x300")
    user_window.configure(bg="darkblue")
    # # Create a label to display the background image
    # user_label = tk.Label(user_window, image=background_image)
    # user_label.place(relwidth=1, relheight=1)

    # label = tk.Label(root, text="Movie Recommendation System", font=("Helvetica", 16, "bold"), fg="darkblue",
    #                        bg="white")
    # label.pack(pady=20)
    title_label = tk.Label(user_window, text="Login Page", font=("Helvetica", 16, "bold"), fg="red", bg="white")
    title_label.pack(pady=20)

    tk.Label(user_window, text="USERID", font=("Helvetica", 10, "bold"), bg="darkblue", fg="white").pack()
    user_id_entry = tk.Entry(user_window)
    user_id_entry.pack()

    tk.Label(user_window, text="USER NAME", font=("Helvetica", 10, "bold"), bg="darkblue", fg="white").pack()
    username_entry = tk.Entry(user_window)
    username_entry.pack()

    tk.Label(user_window, text="EMAIL", font=("Helvetica", 10, "bold"), bg="darkblue", fg="white").pack()
    email_entry = tk.Entry(user_window)
    email_entry.pack()

    tk.Label(user_window, text="AGE", font=("Helvetica", 10, "bold"), bg="darkblue", fg="white").pack()
    age_entry = tk.Entry(user_window)
    age_entry.pack()

    tk.Label(user_window, text="GENDER", font=("Helvetica", 10, "bold"), bg="darkblue", fg="white").pack()
    gender_entry = tk.Entry(user_window)
    gender_entry.pack()

    def submit_registration():
        user_id = user_id_entry.get()
        username = username_entry.get()
        email = email_entry.get()
        age = age_entry.get()
        gender = gender_entry.get()

        sql = "INSERT INTO users (user_id, username, email, age, gender) VALUES (%s, %s, %s, %s, %s)"
        val = (user_id, username, email, age, gender)

        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Registration", "User registered successfully!")
        user_window.destroy()

    tk.Button(user_window, text="Register", command=submit_registration, font=("Helvetica", 12, "bold"), bg="green",
              fg="white").pack()


# Function to recommend movies
def recommend_movies():
    movie_window = tk.Toplevel(root)
    movie_window.title("Movie Recommendation")
    movie_window.geometry("400x300")
    movie_window.configure(bg="lightblue")
    title_label = tk.Label(movie_window, text="Movie recommendation page", font=("Helvetica", 16, "bold"), fg="red",
                           bg="white")
    title_label.pack(pady=20)
    tk.Label(movie_window, text="MOVIE NAME", font=("Helvetica", 10, "bold"), bg="darkblue", fg="white").pack()
    title_entry = tk.Entry(movie_window)
    title_entry.pack()

    def get_movie_info():
        title = title_entry.get()
        query = "SELECT * FROM movies WHERE title=%s"
        cursor.execute(query, (title,))
        movie = cursor.fetchone()
        if movie:
            movie_info = f"Title: {movie[1]}\nGenre: {movie[2]}\nRelease Year: {movie[3]}\nDirector: {movie[4]}\nActors: {movie[5]}\nDescription: {movie[6]}"
            messagebox.showinfo("Movie Information", movie_info)
        else:
            messagebox.showinfo("Error", "Movie not found!")

    get_info_button = tk.Button(movie_window, text="Get Movie Information", command=get_movie_info,
                                font=("Helvetica", 12, "bold"), bg="green", fg="white")
    get_info_button.pack(pady=10)

    # tk.Button(movie_window, text="Get Movie Information", command=get_movie_info, font=("Helvetica", 12, "bold"), bg="green",
    #                         fg="white").pack()

    # title_entry = tk.Entry(get_movie_info, font=("Helvetica", 12))
    # title_entry.grid(row=0, column=1, padx=10)

    def get_related_movies_by_genre():

        # title_entry.pack()
        genre = genre_entry.get()
        query = "SELECT * FROM movies WHERE genre=%s"
        cursor.execute(query, (genre,))
        related_movies = cursor.fetchall()

        if related_movies:
            related_movie_info = "\n\n".join([
                f"Title: {movie[1]}\nRelease Year: {movie[3]}\nDirector: {movie[4]}\nActors: {movie[5]}\nDescription: {movie[6]}\n"
                for movie in related_movies])
            messagebox.showinfo("Related Movies", related_movie_info)
        else:
            messagebox.showinfo("No Movies Found")

    tk.Label(movie_window, text="GENRE", font=("Helvetica", 10, "bold"), bg="darkblue", fg="white").pack()
    genre_entry = tk.Entry(movie_window)
    genre_entry.pack()
    tk.Button(movie_window, text="GET RELATED MOVIES BY GENRE", command=get_related_movies_by_genre,
              font=("Helvetica", 12, "bold"), bg="green",
              fg="white").pack()

    genre_entry = tk.Entry(recommend_movies, font=("Helvetica", 12))
    genre_entry.grid(row=0, column=1, padx=10)

    # get_info_button = tk.Button(movie_window, text="Get Movie Information", command=recommend_movies,
    #                             font=("Helvetica", 12, "bold"), bg="darkblue", fg="white")
    # get_info_button.pack(pady=10)


# Function to rate movies
def rate_movies():
    rate_window = tk.Toplevel(root)
    rate_window.title("Movie Rating")
    rate_window.geometry("300x300")
    rate_window.configure(bg="lightblue")
    title_label = tk.Label(rate_window, text="Rating page", font=("Helvetica", 16, "bold"), fg="red", bg="white")
    title_label.pack(pady=20)
    tk.Label(rate_window, text="User ID", font=("Helvetica", 10, "bold"), bg="darkblue", fg="white").pack()
    id_entry = tk.Entry(rate_window)
    id_entry.pack()

    tk.Label(rate_window, text="Movie Name", font=("Helvetica", 10, "bold"), bg="darkblue", fg="white").pack()
    movie_name_entry = tk.Entry(rate_window)
    movie_name_entry.pack()

    tk.Label(rate_window, text="Rating", font=("Helvetica", 10, "bold"), bg="darkblue", fg="white").pack()
    rating_entry = tk.Entry(rate_window)
    rating_entry.pack()

    def submit_rating():
        rm_id = id_entry.get()
        movie_name = movie_name_entry.get()
        rating = rating_entry.get()

        sql = "INSERT INTO rating (rm_id, movie_name, rating) VALUES (%s, %s, %s)"
        val = (rm_id, movie_name, rating)

        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Review", "Thanks for your review!!")
        rate_window.destroy()

    tk.Button(rate_window, text="Submit Rating", font=("Helvetica", 12, "bold"), bg="green", fg="white",
              command=submit_rating).pack()


# Function to logout

def logout_user():
    logout_window = tk.Toplevel(root)
    logout_window.title("User Logout")
    logout_window.configure(bg="lightblue")
    title_label = tk.Label(logout_window, text="Logout page", font=("Helvetica", 16, "bold"), fg="red", bg="white")
    title_label.pack(pady=20)
    tk.Label(logout_window, text="USERID", font=("Helvetica", 10, "bold"), bg="darkblue", fg="white").pack()
    user_id_entry = tk.Entry(logout_window)
    user_id_entry.pack()

    def logout():
        user_id = user_id_entry.get()
        query = "SELECT * FROM users WHERE user_id=%s"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()

        if user:
            delete_query = "DELETE FROM users WHERE user_id=%s"
            cursor.execute(delete_query, (user_id,))
            db.commit()
            messagebox.showinfo("Logout", "User logged out and data deleted successfully!")
            logout_window.destroy()
        else:
            messagebox.showinfo("Error", "User not found!")

    tk.Button(logout_window, text="Logout", command=logout).pack()


title_label = tk.Label(root, text="Menu", font=("Helvetica", 16, "bold"), fg="darkblue", bg="white")
title_label.pack(pady=20)


# Function to update user details
def update_user_details():
    update_window = tk.Toplevel(root)
    update_window.title("Update User Details")
    update_window.geometry("300x300")
    update_window.configure(bg="lightblue")
    title_label = tk.Label(update_window, text="Update User Details", font=("Helvetica", 16, "bold"), fg="red",
                           bg="white")
    title_label.pack(pady=20)

    tk.Label(update_window, text="USER ID", font=("Helvetica", 10, "bold"), bg="darkblue", fg="white").pack()
    user_id_entry = tk.Entry(update_window)
    user_id_entry.pack()

    tk.Label(update_window, text="New USER NAME", font=("Helvetica", 10, "bold"), bg="darkblue", fg="white").pack()
    new_username_entry = tk.Entry(update_window)
    new_username_entry.pack()

    tk.Label(update_window, text="New EMAIL", font=("Helvetica", 10, "bold"), bg="darkblue", fg="white").pack()
    new_email_entry = tk.Entry(update_window)
    new_email_entry.pack()

    tk.Label(update_window, text="New AGE", font=("Helvetica", 10, "bold"), bg="darkblue", fg="white").pack()
    new_age_entry = tk.Entry(update_window)
    new_age_entry.pack()

    tk.Label(update_window, text="New GENDER", font=("Helvetica", 10, "bold"), bg="darkblue", fg="white").pack()
    new_gender_entry = tk.Entry(update_window)
    new_gender_entry.pack()

    def submit_update():
        user_id = user_id_entry.get()
        new_username = new_username_entry.get()
        new_email = new_email_entry.get()
        new_age = new_age_entry.get()
        new_gender = new_gender_entry.get()

        update_query = "UPDATE users SET username = %s, email = %s, age = %s, gender = %s WHERE user_id = %s"
        update_values = (new_username, new_email, new_age, new_gender, user_id)

        cursor.execute(update_query, update_values)
        db.commit()
        messagebox.showinfo("Update", "User details updated successfully!")
        update_window.destroy()

    tk.Button(update_window, text="Update Details", command=submit_update, font=("Helvetica", 12, "bold"), bg="green",
              fg="white").pack()


# Buttons to access different functionalities
root.geometry("400x400")
tk.Button(root, text="Register User", command=register_user, font=("Helvetica", 12, "bold"), bg="green",
          fg="white").pack(pady=10)
tk.Button(root, text="Recommend Movies", command=recommend_movies, font=("Helvetica", 12, "bold"), bg="green",
          fg="white").pack(pady=10)
tk.Button(root, text="Rate Movies", command=rate_movies, font=("Helvetica", 12, "bold"), bg="green", fg="white").pack(
    pady=10)
tk.Button(root, text="Update User Details", command=update_user_details, font=("Helvetica", 12, "bold"), bg="green",
          fg="white").pack(pady=10)
tk.Button(root, text="Logout User", command=logout_user, font=("Helvetica", 12, "bold"), bg="green", fg="white").pack(
    pady=10)

root.configure(bg='white')
root.mainloop()
