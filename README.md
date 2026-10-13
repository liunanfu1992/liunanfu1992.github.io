# Jiayang Lyu — Academic Homepage

Personal academic homepage based on the supplied static Academic Homepage
template, with a warm ivory / charcoal palette and locally served fonts.
The previous Jekyll implementation is preserved in Git history at `c245ee7`.

## Local preview

Requires Python 3.9 or later. No Ruby or npm installation is needed.

```bash
./run_server.sh
# Open http://127.0.0.1:8000
```

To use another port: `PREVIEW_PORT=8001 ./run_server.sh`.
Refresh your browser after saving edits. The server reads the current source
and disables browser caching; automatic refresh is not enabled. Only public site
files are served. Local materials such as `Coder_Tech_Report/` and Git metadata
are excluded from the preview.

## Editing the new design

- `index.html`: profile, contact links, About, News, publications, awards,
  education, experience, and footer date.
- `assets/css/style.css`: light/dark colors, typography, spacing, responsive layout.
- `assets/js/main.js`: theme toggle and active section navigation.
- `images/`: existing portrait, institution logos, and publication diagrams.
- `assets/img/favicon.svg`: JL monogram.
- `assets/fonts/homepage/`: local Inter/Newsreader fonts and their SIL OFL licenses.
- `about.html` and `about/index.html`: compatibility redirects preserving old hashes.
- `404.html`, `robots.txt`, `sitemap.xml`: error page and search metadata.

All three papers are shown by default; `*` means equal contribution. The original
diagram proportions are preserved, and clicking a thumbnail opens the full image.
The theme defaults to light and remembers the visitor's manual selection. Content and
links work with JavaScript disabled.

## Publishing

GitHub Pages serves the HTML/CSS/JS directly; `.nojekyll` bypasses Jekyll.
Commit the intended changes and push to `main` to trigger Pages deployment.
`Coder_Tech_Report/`, `_site/`, and local Ruby dependencies are ignored and must
not be published. The existing Pages source remains `main` / repository root.
The old Jekyll runtime and unused citation crawler have been removed.

## Credits

Design adapted from the supplied Academic Homepage template, under the MIT license
in `licenses/academic-homepage-MIT.txt`. Original repository licensing remains in
`LICENSE`. Font licenses are in `assets/fonts/homepage/*-OFL.txt`.

<details>
<summary>Previous Jekyll template documentation (reference only)</summary>

The instructions below describe the historical version at `c245ee7`. They do not
apply to the current static homepage or its preview script.

<h1 align="center">
AcadHomepage
</h1>

<div align="center">

[![](https://img.shields.io/github/stars/RayeRen/acad-homepage.github.io)](https://github.com/RayeRen/acad-homepage.github.io)
[![](https://img.shields.io/github/forks/RayeRen/acad-homepage.github.io)](https://github.com/RayeRen/acad-homepage.github.io)
[![](https://img.shields.io/github/issues/RayeRen/acad-homepage.github.io)](https://github.com/RayeRen/acad-homepage.github.io)
[![](https://img.shields.io/github/license/RayeRen/acad-homepage.github.io)](https://github.com/RayeRen/acad-homepage.github.io/blob/main/LICENSE)  | [中文文档](./docs/README-zh.md) 
</div>

<p align="center">A Modern and Responsive Academic Personal Homepage</p>

<p align="center">
    <br>
    <img src="docs/screenshot.png" width="100%"/>
    <br>
</p>

Some examples:
- [Demo Page](https://rayeren.github.io/acad-homepage.github.io/)
- [Personal Homepage of the author](https://rayeren.github.io/)

## Key Features
- **Automatically update google scholar citations**: using the google scholar crawler and github action, this REPO can update the author citations and publication citations automatically.
- **Support Google analytics**: you can trace the traffics of your homepage by easy configuration.
- **Responsive**: this homepage automatically adjust for different screen sizes and viewports.
- **Beautiful and Simple Design**: this homepage is beautiful and simple, which is very suitable for academic personal homepage.
- **SEO**: search Engine Optimization (SEO) helps search engines find the information you publish on your homepage easily, then rank it against similar websites.

## Quick Start

1. Fork this REPO and rename to `USERNAME.github.io`, where `USERNAME` is your github USERNAME.
1. Configure the google scholar citation crawler:
    1. Find your google scholar ID in the url of your google scholar page (e.g., https://scholar.google.com/citations?user=SCHOLAR_ID), where `SCHOLAR_ID` is your google scholar ID.
    1. Set GOOGLE_SCHOLAR_ID variable to your google scholar ID in `Settings -> Secrets -> Actions -> New repository secret` of the REPO website with `name=GOOGLE_SCHOLAR_ID` and `value=SCHOLAR_ID`.
    1. Click the `Action` of the REPO website and enable the workflows by clicking *"I understand my workflows, go ahead and enable them"*. This github action will generate google scholar citation stats data `gs_data.json` in `google-scholar-stats` branch of your REPO. When you update your main branch, this action will be triggered. This action will also be trigger 08:00 UTC everyday.
1. Generate favicon using [favicon-generator](https://redketchup.io/favicon-generator) and download all generated files to `REPO/images`.
1. Modify the configuration of your homepage `_config.yml`:
    1. `title`: the title of your homepage
    1. `description`: the description of your homepage
    1. `repository`: USER_NAME/REPO_NAME  
    1. `google_analytics_id` (optional): google analytics ID
    1. SEO Related keys (optional): get these keys from search engine consoles (e.g. Google, Bing and Baidu) and paste here.
    1. `author`: the author information of this homepage, including some other websites, emails, city and univeristy.
    1. More configuration details are described in the comments.
1. Add your homepage content in `_pages/about.md`.
    1. You can use html+markdown syntax just same as jekyll.
    1. You can use a `<span>` tag with class `show_paper_citations` and attribute `data` to display the citations of your paper. Set the data to the google scholar paper ID. For
        ```html
        <span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span>
        ``` 
        > Q: How to get the google scholar paper ID?   
        > A: Enter your google scholar homepage and click the paper name. Then you can see the paper ID from `citation_for_view=XXXX`, where `XXXX` is the required paper ID.
1. Your page will be published at `https://USERNAME.github.io`.

## Debug Locally

1. Clone your REPO to local using `git clone`.
1. Install Jekyll building environment, including `Ruby`, `RubyGems`, `GCC` and `Make` following [the installation guide](https://jekyllrb.com/docs/installation/#requirements).
1. Run `./run_server.sh` to start the Jekyll LiveReload server. Missing project dependencies are installed automatically on the first run.
1. Open http://127.0.0.1:4000 in your browser.
1. If you change the source code of the website, the livereload server will automatically refresh.
1. If port 4000 is busy, run `JEKYLL_PORT=4001 ./run_server.sh` to use another port.
1. If the LiveReload port is busy, run `JEKYLL_LIVERELOAD_PORT=35731 ./run_server.sh`.
1. When you finish the modification of your homepage, `commit` your changings and `push` to your remote REPO using `git` command.

# Acknowledges

- AcadHomepage incorporates Font Awesome, which is distributed under the terms of the SIL OFL 1.1 and MIT License.
- AcadHomepage is influenced by the github repo [mmistakes/minimal-mistakes](https://github.com/mmistakes/minimal-mistakes), which is distributed under the MIT License.
- AcadHomepage is influenced by the github repo [academicpages/academicpages.github.io](https://github.com/academicpages/academicpages.github.io), which is distributed under the MIT License.

</details>
