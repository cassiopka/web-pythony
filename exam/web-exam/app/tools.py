from models import Book, Cover
import hashlib
import os
from werkzeug.utils import secure_filename
from app import db, app
from models import Genre, Book, Books_has_Genres, Cover, Review


class BooksFilter:
    def __init__(self):
        self.query = Book.query

    def perform(
        self,
        title="",
        genres_list="",
        years_list="",
        amount_from="",
        amount_to="",
        author="",
    ):
        self.query = Book.query

        if title:
            self.query = self.query.filter(Book.title.ilike(f"%{title}%"))
        if genres_list:
            # Convert strings to integers:
            genres_list = [int(g) for g in genres_list]
            self.query = self.query.join(Books_has_Genres).filter(
                Books_has_Genres.genres_id.in_(genres_list)
            )
        if years_list:
            years_list = [int(y) for y in years_list]  # Convert to integers
            self.query = self.query.filter(Book.year.in_(years_list))
        if amount_from:
            self.query = self.query.filter(Book.amount >= int(amount_from))
        if amount_to:
            self.query = self.query.filter(Book.amount <= int(amount_to))
        if author:
            self.query = self.query.filter(Book.author.ilike(f"%{author}%"))

        return self.query.order_by(Book.year.desc())


class ImageSaver:
    def __init__(self, file):
        self.file = file

    def save(self):
        self.img = self.__find_by_md5_hash()
        if self.img is not None:
            return self.__find_by_md5_hash().id
        file_name = secure_filename(self.file.filename)
        last_id = Cover.query.order_by(Cover.id.desc()).first()
        if last_id is None:
            last_id = 0
        else:
            last_id = last_id.id
        self.img = Cover(
            id=last_id + 1,
            file_name=str(last_id + 1) + file_name,
            mime_type=self.file.mimetype,
            md5_hash=self.md5_hash,
        )
        print(os.path.join(app.config["UPLOAD_FOLDER"], self.img.storage_filename))
        self.file.save(
            os.path.join(app.config["UPLOAD_FOLDER"], self.img.storage_filename)
        )
        db.session.add(self.img)
        db.session.commit()
        return self.img.id

    def __find_by_md5_hash(self):
        self.md5_hash = hashlib.md5(self.file.read()).hexdigest()
        self.file.seek(0)
        return Cover.query.filter(Cover.md5_hash == self.md5_hash).first()
