call plug#begin()

" List your plugins here
Plug 'lervag/vimtex'
let g:tex_flavor='latex'
let g:vimtex_compiler_method = 'latexmk'

" Use latexmk as the default compiler
let g:vimtex_compiler_method = 'latexmk'

" Set the compile to use the current buffer's filename
let g:vimtex_compiler_latexmk = {
  \ 'build_dir' : '',
  \ 'callback'  : 1,
  \ 'options'   : [
  \   '-pdf',
  \   '-interaction=nonstopmode',
  \   '-synctex=1',
  \ ],
  \}

let g:vimtex_view_method='zathura'
let g:vimtex_quickfix_mode=0
set conceallevel=1
let g:tex_conceal='abdmg'

Plug 'sirver/ultisnips'
let g:UltiSnipsSnippetDirectories=["UltiSnips"]
let g:UltiSnipsExpandTrigger = '<tab>'
let g:UltiSnipsJumpForwardTrigger = '<tab>'
let g:UltiSnipsJumpBackwardTrigger = '<s-tab>'
 
"Plug 'KeitaNakamura/tex-conceal.vim'
"    set conceallevel=1
"    let g:tex_conceal='abdmg'
"    hi Conceal ctermbg=none

call plug#end()
