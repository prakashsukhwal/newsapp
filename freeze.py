from flask_frozen import Freezer
from app import app
from model import get_csv
freezer = Freezer(app)

@freezer.register_generator
def detail():
    for row in get_csv():
        yield {'row_id': row['id']}

if __name__ == '__main__':
    freezer.freeze()