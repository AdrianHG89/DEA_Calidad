#!/bin/bash

# Cleaning existing reports and creating the folder
rm -rf pymetrics/
mkdir pymetrics
rm -rf pylint/
mkdir pylint



# Metrics for users module
echo "Generating metrics for User module..."
pymetrics -i simple:SimpleMetric,mccabe:McCabeMetric users/views.py users/models.py > pymetrics/Users.txt
pylint -d C0103,E1101 -f html users/ > pylint/user.html

# Metrics for raven module
echo "Generating metrics for raven module..."
pymetrics -i simple:SimpleMetric,mccabe:McCabeMetric raven/views.py raven/models.py > pymetrics/raven.txt
pylint -d C0103,E1101 -f html raven/ > pylint/raven.html

# Metrics for post module
echo "Generating metrics for post module..."
pymetrics -i simple:SimpleMetric,mccabe:McCabeMetric post/views.py post/models.py > pymetrics/post.txt
pylint -d C0103,E1101 -f html post/ > pylint/post.html

# Cleaning temp files...
echo "Cleaning temp files..."
rm -f metricData.*
