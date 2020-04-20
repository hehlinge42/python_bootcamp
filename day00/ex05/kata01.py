import sys
import argparse

languages = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
}

for item in languages.items():
	print("% s was created by % s" %(item[0], item[1]))
