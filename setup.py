from setuptools import find_packages,setup
from typing import List
hypen_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this func will retrn list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n"," ")for req in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='pardhu',
    author_email='nagireddipardhasaradhi123@gmail.com',
    packages=find_packages(),
    #install_requires=['pandas','numpy','seaborn'],
    install_requires=get_requirements('requirements.txt')
)