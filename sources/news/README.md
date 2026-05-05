# News Sources

Use this folder for article/RSS/news inputs that are not naturally organized as
video channels.

Recommended layout:

```text
sources/news/
  wall-street/
    manifests/
    articles/
    runs/
```

For every news source, keep the raw capture separate from interpreted notes:

- Raw article metadata and URLs stay in `sources/news/...`.
- Daily or thematic interpretation goes into `macro/`, `sectors/`, `companies/`,
  or `theses/`.
