# FixMate site generator

Folders starting with `_` are not published by GitHub Pages.

- `data.py`: services and areas
- `articles2.py`: the first 12 home tips articles
- `articles_daily.py`: new English articles go here, one tuple per article
- `articles_ml.py`: Malayalam versions of the first 15 articles, keyed by English slug
- `articles_daily_ml.py`: Malayalam versions of daily articles, `ARTICLES_DAILY_ML = { slug: (title, description, html) }`
- `build.py`: builds area pages, `/areas`, English articles at `/blog/`, Malayalam articles at `/blog/ml/`, both indexes and `sitemap.xml`

## Add an article

1. Append a tuple to `ARTICLES_DAILY` in `articles_daily.py`
2. Add the Malayalam version with the same slug to `ARTICLES_DAILY_ML` in `articles_daily_ml.py`
3. Run `python3 _tools/build.py .` from the repo root
4. Commit and push to `main`

Do not hand edit the generated area pages, blog pages or sitemap. Edit the data and rebuild.
