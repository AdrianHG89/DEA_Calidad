#!/bin/bash

rm -f .coverage

rm -rf htmlcov/
python manage.py syncdb --settings=`./raven/setting.py`
coverage run --omit=`ls */features/raven.py | tr "\n" ","` \
    --source=users,raven,post\
    manage.py harvest --settings=test_settings
echo "Cleaning test database..."

echo "Test completed!"
echo "Generating HTML report..."
coverage html
echo "Console report:"
coverage report
