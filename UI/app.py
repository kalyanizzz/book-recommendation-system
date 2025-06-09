from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load datasets
pbr_df = pickle.load(open("C:/Users/nimee/Bigdata/PopularBookRecommendation.pkl", 'rb'))
pcb_df = pickle.load(open("C:/Users/nimee/Bigdata/PopularChristmasBooks.pkl", 'rb'))
pkl_file_path = "C:/Users/nimee/Bigdata/Collab_model.pkl" 
data = pd.read_pickle(pkl_file_path)
# Path to your pickle file
PKL_FILE_PATH = "C:/Users/nimee/Bigdata/Content_model.pkl"

# Load the data
data1 = pd.read_pickle(PKL_FILE_PATH)
# Load the books data from CSV into a DataFrame and ensure IDs are integers
books_data = pd.read_csv("C:/Users/nimee/Bigdata/books_data.csv")

@app.route('/')
def index():
    # Prepare "Popular Books" data
    popular_books = [
        {
            "title": title,
            "review_count": review_count,
            "average_score": avg_score,
            "image": image
        }
        for title, review_count, avg_score, image in zip(
            pbr_df['Title'], pbr_df['review_count'],
            pbr_df['average_review_score'], pbr_df['image']
        )
    ]

    # Prepare "Christmas Season Popular Books" data
    christmas_books = [
        {
            "title": title,
            "average_score": avg_score,
            "image": image,
            "author": author
        }
        for title, avg_score, image, author in zip(
            pcb_df['Title'], pcb_df['average_review_score'],
            pcb_df['image'], pcb_df['authors']
        )
    ]

    return render_template('index.html', popular_books=popular_books, christmas_books=christmas_books, is_search=False)

@app.route('/book/<string:title>')
def book_details(title):
    # Locate the book by its title
    book = books_data[books_data['Title'].str.lower() == title.lower()]

    if book.empty:
        return "Book not found", 404

    # Prepare book details
    book_details = {
        "title": book['Title'].values[0],
        "author": book['authors'].values[0],
        "description": book['description'].values[0],
        "image": book['image'].values[0]
    }

    return render_template('book_details.html', book=book_details)
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip()

    if query:
        # Filter only by Title column
        search_results = books_data[books_data['Title'].str.contains(query, case=False, na=False)]
    else:
        search_results = pd.DataFrame()  # No results if query is empty

    # Convert search results into a list of dictionaries
    books = search_results[['Title', 'description', 'authors', 'image', 'publisher']].to_dict(orient='records')

    return render_template('index.html', books=books, is_search=True)

@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    """Retrieve recommended titles for a given user_id and fetch book details."""
    user_id = request.form.get('user_id')
    if user_id is None or user_id.strip() == "":
        return "Error: user_id is required", 400

    # Filter the data for the user_id
    user_data = data[data['user_id'] == user_id]

    if user_data.empty:
        return f"No recommendations found for user_id: {user_id}", 404

    # Get the list of recommended titles
    titles = user_data['titles'].values[0]  # Assuming titles is a list

    # Match titles with details from books_data
    recommendations = [
        {
            "title": title,
            "description": books_data.loc[books_data['Title'] == title, 'description'].values[0],
            "author": books_data.loc[books_data['Title'] == title, 'authors'].values[0],
            "image": books_data.loc[books_data['Title'] == title, 'image'].values[0],
            "infoLink": books_data.loc[books_data['Title'] == title, 'infoLink'].values[0],
            "categories": books_data.loc[books_data['Title'] == title, 'categories'].values[0]
        }
        for title in titles if title in books_data['Title'].values
    ]

    # Render results in a template
    return render_template('recommendations.html', recommendations=recommendations, user_id=user_id)

@app.route('/get_book', methods=['POST'])
def get_book():
    """Retrieve book details for a given book_id and provide recommendations."""
    book_id = request.form.get('book_id')
    if not book_id or book_id.strip() == "":
        return "Error: book_id is required", 400

    # Filter the PKL file data for the entered book_id
    book_data = data1[data1['Id'] == book_id]
    if book_data.empty:
        return f"No book found for Id: {book_id}", 404

    # Debugging: Print the retrieved book data
    print("Book Data:", book_data)

    # Retrieve the list of recommended titles
    recommended_titles = book_data['Recommended_Titles'].values[0]
    print("Recommended Titles:", recommended_titles)

    # Ensure recommended_titles is a valid list
    if isinstance(recommended_titles, str):
        import ast
        recommended_titles = ast.literal_eval(recommended_titles)

    # Fetch book details from books_data
    recommendations = []
    for title in recommended_titles:
        # Find the book details in books_data
        book_details = books_data[books_data['Title'] == title]
        if not book_details.empty:
            recommendations.append({
                "title": title,
                "description": book_details['description'].values[0] if 'description' in books_data.columns else "Description not available",
                "author": book_details['authors'].values[0] if 'authors' in books_data.columns else "Author not available",
                "image": book_details['image'].values[0] if 'image' in books_data.columns else "Image not available",
                "infoLink": book_details['infoLink'].values[0] if 'infoLink' in books_data.columns else "#",
                "categories": book_details['categories'].values[0] if 'categories' in books_data.columns else "Category not available"
            })
        else:
            print(f"Title '{title}' not found in books_data")

    # Check if recommendations are available
    if not recommendations:
        return f"No valid recommendations found for Id: {book_id}", 404

    # Render the recommendations template
    return render_template('recommendations.html', recommendations=recommendations, book_id=book_id)

if __name__ == '__main__':
    app.run(debug=True)
