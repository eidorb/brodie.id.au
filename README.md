# Sphinx migration

- Take inspiration from these blog posts and GitHub issue:
  - https://predictablynoisy.com/posts/2020/sphinx-blogging/
  - https://ddanieltan.github.io/posts/2021/how_to_create_this_blog/
  - https://github.com/executablebooks/jupyter-book/issues/900
- Do the following things:
  - [x] Change automated build
    - [x] Try gcompat with Alpine Linux
    - [x] Use micromamba
  - [ ] Configure Sphinx and dependencies for automated bare-bones blog
  - [ ] Cut over old existing posts
  - [ ] Fill in minimal content in broader website

# Dependencies

- Conda
  - Defined in `environment.yml`.
  - Install/update with `conda env update --name "brodie.srht.site" --file environment.yml --prune`.
- Poetry
  - Defined in `pyproject.toml` and `poetry.lock`.
  - Install/update with `poetry install --remove-untracked`.


# Build

- Build with Nikola:

      cd site
      nikola build
- Serve locally: `nikola serve`
- Serve and automatically rebuild on changes: `nikola auto --browser`


# Write

- New post: `nikola new_post`
- New notebook (Nikola adds a bit of metadata to the end of the notebook): `nikola new_post --format ipynb`
