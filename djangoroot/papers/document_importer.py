import os
import django

from HNGR.models import Document, Doc_theme


def insert_parsed_data(parsed_data):
    for file_name, data in parsed_data.items():
        year = data.get("Year", "Not mentioned")
        year = year if year.isnumeric() else None
        document = Document(
            city=data.get("City", "Not mentioned"),
            country=data.get("Country", "Not mentioned"),
            major_field=data.get("Major/Field", "Not mentioned"),
            author=data.get("Author", "Not mentioned"),
            advisor=data.get("Advisor", "Not mentioned"),
            year=year,
            file_path=file_name,
        )
        document.save()

        themes = data.get("Themes", "").split(", ")
        for theme in themes:
            if theme:
                doc_theme = Doc_theme(document=document, theme_name=theme)
                doc_theme.save()

        print(f"Inserted {file_name}")

