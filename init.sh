answer=""
read -r -p "Please Input name of git: " answer
if ! [ "$answer" = "" ]; then
	git config --replace-all --global user.name $answer
else
	echo "Skip"
fi

answer=""
read -r -p "Please Input email of git: " answer
if ! [ "$answer" = "" ]; then
	git config --replace-all --global user.email $answer
else
	echo "Skip"
fi

answer=""
read -r -p "Please Input editor of git: " answer
if ! [ "$answer" = "" ]; then
	git config --replace-all --global core.editor $answer
else
	echo "Skip"
fi
