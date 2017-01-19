Introduction
============
 survivalPredictor predicts the survival for glioblastoma patients from mRNA gene expression data.

survivalPredictor comes with six state-of-the-art machine learning models including Random Forest (RF), Support Vector Machines (SVM), K-Nearest Neighbor (kNN), AdaBoost (AB), Decision Tree (DT) and Naive Bayes (NB).

Naive Bayes is our optimal and default model but user can select any of the models and further test it using cross-validation, independent test data or use it to make predictions. 

Installation
============

Prerequisites
-------------
survivalPredictor requires:

	* Python (>= 2.6 or >= 3.3)
	* NumPy (>= 1.6.1): http://www.numpy.org/
	* SciPy (>= 0.9): http://www.scipy.org/
	* Scikit-learn (>= 0.17): http://scikit-learn.org/
	* Pandas (>= 0.16.0): http://pandas.pydata.org/

If you already have a working installation of numpy and scipy, the easiest way to install scikit-learn and pandas is using pip::

	pip install -U scikit-learn

	pip install -U pandas

or using conda::

	conda install scikit-learn

	conda install pandas


If you don’t already have a python installation with numpy, scipy and pandas, we recommend to install either via your package manager or via a python bundles (Canopy, Anaconda). These come with numpy, scipy, scikit-learn, pandas and many other helpful scientific and data processing libraries and available for platforms including Windows, Mac OSX and Linux.


Install survivalPredictor
-------------------------
You can install survivalPredictor either from PyPi using pip and install it from the source. Please make sure you have already installed the above mentioned python libraries required to run survivalPredictor.

Install from PyPi::

	pip install survivalPredictor

Install from the source::
	
	git clone https://github.com/asntech/survivalPredictor.git
	cd survivalPredictor
	python setup.py install --user

How to use survivalPredictor
============================
Once you have installed survivalPredictor, you can type:

	survivalPredictor --help

to find the available commands and required parameters to run survivalPredictor. 

survivalPredictor demo
----------------------

To run a demo using Random Forest model and validate it using 10-fold cross-validation, you can type::

	survivalPredictor --demo

This will save the results in the current working directory with a folder named ``survivalPredictor_results``. If you wish to save the results in a specific folder, you can type::

	survivalPredictor --demo --output ~/path/to/your/folder

Select model
------------
survivalPredictor comes with six state-of-the-art machine learning models including Random Forest (RF), Support Vector Machines (SVM), K-Nearest Neighbor (kNN), AdaBoost (AB), Decision Tree (DT) and Naive Bayes (NB). Random Forest is the default model.

To select model you need to type::

	survivalPredictor --model MODEL_NAME

MODEL_NAME can be ``rf``, ``svm``, ``knn``, ``ab``, ``dt``, ``nb`` or use ``all`` if you want use all models one by one.

Define features and feature subsets
-----------------------------------
To tell the model to use specific features you need to type::

	survivalPredictor --model svm --feature "Top 10", "Top 100", "Top 200"

Make sure the features names are comma separated. 

If you want to compare the individual predictive power or combinatorial predictive power of different features, you need to pass the argument ``--compare`` with ``--features``::

	survivalPredictor --model nb --feature "Top 10", "Top 100", "Top 200" --compare


Run model with cross-validation
-------------------------------
By default all models use 3-fold cross-validation. If you want to set different fold lets say 5, set ``--cv`` parameter as::

	survivalPredictor --model rf --feature "Top 200" --cv 5


Make predictions
------------------
To make predictions should have computed available features and saved a CSV file. Next, you need to tell the model the features you have to make prediction with using ``--feature`` and also provide the Tab delimetd file to ``--input`` and next type ``--pred`` to make predictions::

	survivalPredictor --model rf --feature "Top 200" --input ~/path/to/CSV/file.txt --pred

This will save the predictions results as CSV file ``survivalPredictor_[MODEL_NAME]_predictions.csv``. In the CSV file the field Class is 1=alive and 0=dead. We also report  probability score for each prediction to tell the user how good and bad a prediction is. This will help to decide which candidates to select for further analysis.

Feedback
========
If you have questions, or found any bug in the program, please write to us at ``aziz.khan[at]ncmm.uio.no``

