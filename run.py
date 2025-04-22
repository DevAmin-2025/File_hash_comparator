import hashlib
import os
from typing import Tuple, Union

from termcolor import colored


def hash_file(file_path1: str, file_path2: str) -> Tuple[Union[str, None], Union[str, None]]:
	"""
	Compute the SHA-256 hash of two files and compare their hashes.

	This function takes two file paths, converts them to WSL-compatible paths if necessary,
	computes the SHA-256 hash of each file, and returns the hash values.

	:param file_path1: The path to the first file.
	:param file_path2: The path to the second file.
	:return: A tuple containing the SHA-256 hash values of the two files.
	"""
	def convert_path(path: str) -> str:
		"""
		Convert a Windows file path to a WSL-compatible path.

		This function checks if the given path is a Windows path. If it is,
		the function converts it to a WSL-compatible path using the `wslpath`
		command. If the path is not a Windows path, it returns the original path.

		:param path: The file path to be converted.
		:return: The WSL-compatible path if the input is a Windows path; otherwise, the original path.
		"""
		# Check if the path is a Windows path and convert it
		# For users who use windows subsystem for linux
		if path[1:3] == ':\\':
			wsl_path = os.popen(f'wslpath "{path}"').read().strip()
			return wsl_path
		return path

	# Convert paths if necessary
	file_path1 = convert_path(file_path1)
	file_path2 = convert_path(file_path2)

	# Check if file exists
	if not os.path.exists(file_path1):
		print(colored(f'Error: File "{file_path1}" does not exist.', 'red'))
		return None, None
	if not os.path.exists(file_path2):
		print(colored(f'Error: File "{file_path2}" does not exist.', 'red'))
		return None, None

	# Use hashlib to store the hash of a file
	first_sha256 = hashlib.sha256()
	second_sha256 = hashlib.sha256()

	with open(file_path1, 'rb') as f:
		# Use file.read() to read the size of file
		# And read the file in small chunks
		# Because we cannot read the large files.
		while chunk := f.read(8192):
			first_sha256.update(chunk)

	with open(file_path2, 'rb') as f:
		# Use file.read() to read the size of file
		# And read the file in small chunks
		# Because we cannot read the large files.
		while chunk := f.read(8192):
			second_sha256.update(chunk)

	# get the final hash value as a hexadecimal string.
	hash1 = first_sha256.hexdigest()
	hash2 = second_sha256.hexdigest()

	return hash1, hash2


if __name__ == '__main__':
	first_file_path = input('Enter path to the first file: ').strip()
	second_file_path = input('Enter path to the second file: ').strip()

	file1_hash, file2_hash = hash_file(first_file_path, second_file_path)
	if file1_hash is None or file2_hash is None:
		print(colored('File comparison could not be performed due to missing file(s).', 'red'))
	elif file1_hash == file2_hash:
		print(colored('Two files are identical.', 'white', attrs=['reverse']))
	else:
		print(colored('Two files are different.', 'white', attrs=['reverse']))
