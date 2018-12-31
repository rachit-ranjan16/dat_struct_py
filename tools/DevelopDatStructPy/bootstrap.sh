echo "----------------------------"
echo "Updating"
echo "----------------------------"
sudo apt-get -y -q update
echo "----------------------------"
echo "Install and Configture vim for Python Development"
echo "----------------------------"
sudo apt-get -y -q install vim
sudo cp /vagrant_data/.vimrc /home/ubuntu
sudo cp /vagrant_data/.vimrc /root/
echo "----------------------------"
echo "Install pip"
echo "----------------------------"
sudo apt-get -y -q install python3-pip
echo "----------------------------"
echo "Install pyenv"
echo "----------------------------"
sudo apt-get -y -q install python3-venv
echo "----------------------------"
echo "Install and configure git"
echo "----------------------------"
sudo apt-get -y -q install git
git config --global user.name "" #Add Git Username here
git config --global user.email "" #Add Git Email here
echo "----------------------------"
echo "Setup Code Repo"
echo "----------------------------"
mkdir Development
cd Development
mkdir Repos
cd Repos
sudo git clone https://github.com/rachit-ranjan16/dat_struct_py.git
echo "----------------------------"
echo "Create and Activate Virtual Environment"
echo "----------------------------"
cd ..
pyvenv developEnv
source developEnv/bin/activate
pip install --upgrade pip
echo "----------------------------"
echo "Install Coverage and Wheel"
echo "----------------------------"
pip install wheel
pip install coverage
echo "----------------------------"
echo "All set"
echo "----------------------------"
