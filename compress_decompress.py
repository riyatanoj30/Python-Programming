import zlib 
def compress_string(string): 
  """Function to compress a string using zlib.""" 
  return zlib.compress(string.encode()) 
def decompress_string(compressed): 
  """Function to decompress a zlib compressed string.""" 
  return zlib.decompress(compressed).decode() 
# Taking user input 
user_input = input("Enter a string: ") 
compressed_data = compress_string(user_input) 
decompressed_data = decompress_string(compressed_data) 
print(f"Compressed Data: {compressed_data}") 
print(f"Decompressed Data: {decompressed_data}")