from setuptools import setup

setup(
    name = 'petrophysics',
    version = '0.1.3',
    author='Mihai',
    author_email='m_iorgandopol@yahoo.com',
    packages = ['petrophysics',
                'petrophysics.clayvolume',
                'petrophysics.conversions',
                'petrophysics.lithology',
                'petrophysics.permeability',
                'petrophysics.porosity',
                'petrophysics.reserves',
                'petrophysics.resistivity',
                'petrophysics.rockphysics',
                'petrophysics.salinity',
                'petrophysics.saturation',
                'petrophysics.temperature'],
    url='http://pypi.python.org/pypi/petrophysics/',
    license = ['MIT'],
    description = 'A package containing useful functions for well log interpretation',
    long_description=open('README.rst').read(),
    install_requires = ['numpy'],
)
