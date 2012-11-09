from setuptools import setup, find_packages
import os

version = '1.1.dev0'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='policy.slrb',
      version=version,
      description="'policy of SLRB site'",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['policy', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
	  'collective.easyslider',
          'Solgema.fullcalendar',
          'Products.Collage',
          'collective.collage.innerfade',
          'collective.collage.maps',
#          'publication.interfaces',
          'collective.collage.easyslider',
          'collective.gallery',
          'quintagroup.analytics',
          'collective.recaptcha',
          'qi.portlet.TagClouds',
          'Products.PloneFormGen',
          'collective.collage.innerfade',
          'collective.quickupload',
          'collective.contentstats',
          'quintagroup.analytics',
          'GChartWrapper',
          'Products.PressRoom',
          'products.geoloc',
          'Products.contentmigration',
          'Products.Maps',
          'webcouturier.dropdownmenu',
	  'collective.anysurfer',
          'plonetheme.slrb'
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["templer.localcommands"],
      )
