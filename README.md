# nvim-LaTeX-config
An nvim setup for writing, compiling, and displaying LaTeX

A huge shoutout to Gilles Castel - castel.dev, phd, this is his snippets file with some extras (greek letters, lorentz matrices, e.t.c.) and some edits.
castel.dev has a setup on how to do extra things like switching layouts, even doing so based on a timetable. It's fantastic, and you should look there first.

This setup requires two plugins as-is:

Ultisnips : https://github.com/SirVer/ultisnips for the snippets file

VimTeX : https://github.com/lervag/vimtex for the LaTeX compilation

Thanks to the many developers of both plugins, for making lecture notes massively easier to write.

You can use whatever plugin manager you like. I use vim-plug : https://github.com/junegunn/vim-plug which is what the vim.tex config is for.

package-wise, on a linux system, you will need: \
neovim, duh \
python-pynvim, needed by ultisnips (or some way of getting pynvim in your global python install, pip complains if you try doing it with pip) \
LaTeX of some form, I recommend TeXlive \
a PDF viewer, I use zathura, but anything will work, I recommend something not too heavy.

install instructions are provided, but are for Arch linux, and related distros with the pacman manager. Currently, no provided packages are from the AUR, and can be sourced straight from the package repository from the verified maintainers, so low risk of sccaaaaryy AUR malware.

steps:

install nvim. For arch:
```
pacman -S nvim
```

make an nvim config. For linux:

```
mkdir ~/.config/nvim
```

To install vim-plug:
```
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```

Put the init.vim file in the .config/nvim folder

I suggest running PlugInstall to install the packages, this will give a "waah you don't have pynvim" error through Ultisnips but we remedy this later:
within nvim:
```
:PlugInstall
```

now install pynvim, the texlive group, and zathura and zathura-pdf-poppler, or your PDF viewer and LaTeX system of choice. \
NOTE: if you change to use something instead of zathura for PDF rendering or latexmk for compiling, you HAVE to modify init.vim to call the new program instead

```
pacman -S python-pynvim, texlive, zathura, zathura-pdf-poppler
```

installing texlive ```pacman -S texlive``` will ask if you want just a subset of packages or  the whole group. If you can afford the space (a few gigabytes), get the whole thing. It's easier

Now, in your .config/nvim folder (or whatever your system has), makd a folder called UltiSnips, and move tex.snippets there, and a folder called pythonx, and move matrix.py there
```
mkdir ~/.config/nvim/UltiSnips
mkdir ~/.config/nvim/pythonx
```

Ideally, that's everything :D

Edit the keybinds to your taste, they're a mix of castel.dev's snippets, the Latex Suite plugin for obsidian notes, and whatever I needed for maths/physics courses I took. I preferred to keep everything in one big file, so there's probably some stuff you don't need. Latex Suite was fantastic and if you use Obsidian, I highly recommend using that.
