'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory 
subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2
\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 
contains a file file1.ext and an empty second-level sub-directory subsubdir1. 
subdir2 contains a second-level sub-directory subsubdir2 containing a file 
file2.ext.

We are interested in finding the longest (number of characters) absolute path 
to a file within our file system. For example, in the second example above, 
the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its 
length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the 
length of the longest absolute path to a file in the abstracted file system. 
If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
'''

def longest_path(path):
	'''
	Function that takes the path as a string and returns the max length of abs
	location of a file in the directory structure.

	This soltuion is done in O(n) time complexity. Where n is the length of the
	entire directory structure string provided.

	We use number of \t prepended to the each file/folder to determine the 
	depth of the file/folder.
	It maintains the max length of the each level as we traverse. On completion
	of traversal of one sub-directory we remove data of prev sub-directory
	structure until we meet a file(by checking if '.' if present in name)

	On encountering a file it adds up the length and compares with the max_len
	we have been maintaining.
	'''
	max_len = 0
	temp = {}
	#create a list out of the path string
	path_list = path.split('\n')

	for value in path_list:
		level = value.count('\t')
		length = 0
		if level-1 in temp:
			length = temp[level-1][1]
		if '.' not in value:
			value_clean = value.strip('\t')
			length += len(value_clean)+1
			temp[level] = [value_clean, length]
		else:
			value_clean = value.strip('\t')
			length += len(value_clean)
			max_len = max(max_len, length)

	return max_len


if __name__ == '__main__':
	path='''dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\t
			subsubdir2\n\t\t\tfile2ext'''

	print longest_path(path)



