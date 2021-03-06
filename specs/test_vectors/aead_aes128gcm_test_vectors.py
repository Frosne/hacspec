from mypy_extensions import TypedDict
from speclib import array

aes128gcm_test = TypedDict('aes128gcm_test', {
    'input_len': int,
    'input': str,
    'aad_len': int,
    'aad': str,
    'key' :  str,
    'nonce' :  str,
    'output' :  str})

aead_aes128gcm_test_vectors : 'array[aes128gcm_test]' = array([
{
	'key'	: "00000000000000000000000000000000",
	'nonce'	: "000000000000000000000000",
	'aad'	: "",
	'aad_len' : 0,
	'input'	: "",
	'input_len'	: 0,
	'tag'	: "58e2fccefa7e3061367f1d57a4e7455a",
	'output' : ""
},
{
	'key'	: "00000000000000000000000000000000",
	'nonce'	: "000000000000000000000000",
	'aad'	: "",
	'aad_len' : 0,
	'input'	: "00000000000000000000000000000000",
	'input_len'	: 16,
	'tag'	: "ab6e47d42cec13bdf53a67b21257bddf",
	'output' : "0388dace60b6a392f328c2b971b2fe78"
},
{
	'key'	: "feffe9928665731c6d6a8f9467308308",
	'nonce'	: "cafebabefacedbaddecaf888",
	'aad'	: "",
	'aad_len' : 0,
	'input'	: "d9313225f88406e5a55909c5aff5269a86a7a9531534f7da2e4c303d8a318a721c3c0c95956809532fcf0e2449a6b525b16aedf5aa0de657ba637b391aafd255",
	'input_len'	: 64,
	'tag'	: "4d5c2af327cd64a62cf35abd2ba6fab4",
	'output' : "42831ec2217774244b7221b784d0d49ce3aa212f2c02a4e035c17e2329aca12e21d514b25466931c7d8f6a5aac84aa051ba30b396a0aac973d58e091473f5985"
},
{
	'key'	: "feffe9928665731c6d6a8f9467308308",
	'nonce'	: "cafebabefacedbaddecaf888",
	'aad'	: "feedfacedeadbeeffeedfacedeadbeefabaddad2",
	'aad_len' : 0,
	'input'	: "d9313225f88406e5a55909c5aff5269a86a7a9531534f7da2e4c303d8a318a721c3c0c95956809532fcf0e2449a6b525b16aedf5aa0de657ba637b39",
	'input_len'	: 60,
	'tag'	: "5bc94fbc3221a5db94fae95ae7121a47",
	'output' : "42831ec2217774244b7221b784d0d49ce3aa212f2c02a4e035c17e2329aca12e21d514b25466931c7d8f6a5aac84aa051ba30b396a0aac973d58e091"
},
    
   
    ])
