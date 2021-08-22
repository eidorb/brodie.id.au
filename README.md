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
