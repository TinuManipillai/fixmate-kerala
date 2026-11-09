# FixMate site generator

Folders starting with `_` are not published by GitHub Pages.

- `data.py`: services and areas
- `articles2.py`: the first 12 home tips articles
- `articles_daily.py`: new articles go here, one tuple per article
- `build.py`: builds area pages, `/areas`, all blog articles, `/blog/` index and `sitemap.xml`

## Add an article

1. Append a tuple to `ARTICLES_DAILY` in `articles_daily.py`
2. Run `python3 _tools/build.py .` from the repo root
3. Commit and push to `main`

Do not hand edit the generated area pages, blog pages or sitemap. Edit the data and rebuild.
