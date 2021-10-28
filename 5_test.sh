
# pytest -s
# pytest

dirs="venv/*"
dirs="${dirs},tests/*"

coverage run -m pytest -s -W ignore::DeprecationWarning
coverage report --omit ${dirs}
coverage html --omit ${dirs}

# open htmlcov/index.html
# 然後看 htmlcov
# 可以看看哪邊沒有 覆蓋
echo "open htmlcov/index.html"