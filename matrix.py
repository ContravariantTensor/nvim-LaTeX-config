#this code sits in the pythonx folder on my system, but i cannot remember where it's from, if you're the creator of this PLEASE lmk
#this program deals with creating matrices. it works but if you do not tab through the matrix in its entirety anything that tries to add tabstops after will break the pynvim API

def create_row_placeholders(snip):
    # retrieving single line from current string and treat it like tabstops
    # count
    placeholders_amount = int(snip.buffer[snip.line].strip())

    # erase current line
    snip.buffer[snip.line] = ''

    # create anonymous snippet with expected content and number of tabstops
    anon_snippet_body = ' & '.join(['$' + str(i+1)
                                    for i in range(placeholders_amount)])

    # expand anonymous snippet
    snip.expand_anon(anon_snippet_body)
def create_matrix_placeholders(snip):
	# Create anonymous snippet body
	anon_snippet_body = ""

	# Get start and end line number of expanded snippet
	start = snip.snippet_start[0]
	end = snip.snippet_end[0]

  # Append current line into anonymous snippet
	for i in range(start, end + 1):
		anon_snippet_body += snip.buffer[i]
		anon_snippet_body += "" if i == end else "\n"

	# Delete expanded snippet line till second to last line
	for i in range(start, end):
		del snip.buffer[start]

	# Empty last expanded snippet line while preserving the line
	snip.buffer[start] = ''

	# Expand anonymous snippet
	snip.expand_anon(anon_snippet_body)

def create_matrix(cols, rows, sep, start, end):
	res = ""
	placeholder = 1
	for _ in range(0, int(rows)):
		res += start + f"${placeholder} "
		placeholder += 1
		for _ in range(0, int(cols) - 1):
			res += sep + f" ${placeholder} "
			placeholder += 1
		res += end
	return res[:-1]

# if matrix created, but unfilled (tabstops still on stack), creating another matrix gives 'pynvim.api.common.NvimError: Index out of bounds'
