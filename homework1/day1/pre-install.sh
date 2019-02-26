#!/bin/bash

yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel \
openssl-devel xz xz-devel libffi-devel vim git -y

curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

cat << EOF >> $HOME/.bashrc
PATH="\$HOME/.pyenv/bin:\$PATH"
eval "\$(pyenv init -)"
eval "\$(pyenv virtualenv-init -)"
EOF

cd $HOME
source .bashrc
