#!/bin/bash
echo "Install: fzf"
# Add installation commands here

create_deb() {
	TMP_DIR="fzf_deb"
	rm -rf $TMP_DIR
	mkdir -p $TMP_DIR
	(cd $TMP_DIR && apt-get download fzf)
	deb_name=$(find $TMP_DIR -type f -name 'fzf_*_amd64.deb')
	dpkg-deb -R $deb_name $TMP_DIR
	rm -f $deb_name

	echo "OK"
	fzf/install --bin
	PACKAGE_VERSION=$(awk -F= '/^version=/{print $2; exit}' fzf/install)
	echo "fzf version: $PACKAGE_VERSION"
	echo "copy files to $TMP_DIR"
	rm -rf $TMP_DIR/usr/bin/*
	cp fzf/bin/* $TMP_DIR/usr/bin
	rm -rf $TMP_DIR/usr/share/man
	cp -r fzf/man $TMP_DIR/usr/share/man
	cp fzf/shell/completion.bash $TMP_DIR/usr/share/bash-completion/completions/fzf
	cp fzf/shell/completion.zsh $TMP_DIR/usr/share/doc/fzf/examples/
	cp fzf/shell/key-bindings.fish $TMP_DIR/usr/share/fish/vendor_functions.d/fzf_key_bindings.fish
	cp fzf/shell/key-bindings* $TMP_DIR/usr/share/doc/fzf/examples/
	cp fzf/plugin/fzf.vim $TMP_DIR/usr/share/doc/fzf/examples/
	cp -r fzf/plugin/ $TMP_DIR/usr/share/doc/fzf/examples/

	echo "setup control file"
	file="$TMP_DIR/DEBIAN/control"
	sed -i 's/^Version:.*/Version: 0.43/' "$file"
	sed -i 's/^Maintainer:.*/Maintainer: FallMaple <tony53517230@gmail.com>/' "$file"

	dpkg-deb -b $TMP_DIR fzf_self_amd64.deb
}

git clone https://github.com/junegunn/fzf.git
create_deb
sudo apt-get -y install ./fzf_self_amd64.deb
# set fzf key bindings
cp fzf/shell/key-bindings.zsh ~/.config/.zsh/fzf-key-bindings.zsh
rm -rf $TMP_DIR
rm -rf fzf
rm -f fzf_self_amd64.deb