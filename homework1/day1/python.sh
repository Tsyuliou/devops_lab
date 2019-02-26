#!/bin/bash

ch1=$(pyenv versions | grep 3.7.2)
ch2=$(pyenv versions | grep 2.7.15)


if [[ $ch2 ]]
    then echo "Python v.2.7.15 already exist!"
    pip install virtualenv
    pyenv global 2.7.15
    pyenv virtualenv p2
    else pyenv install 2.7.15
    pip install virtualenv
    pyenv global 2.7.15
    pyenv virtualenv p2
fi

if [[ $ch1 ]]
    then echo "Python v.3.7.2 already exist!"    
    pyenv global 3.7.2
    pyenv virtualenv p3
    else pyenv install 3.7.2
    pyenv global 3.7.2
    pyenv virtualenv p3    
fi
