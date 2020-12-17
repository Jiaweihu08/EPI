mapping = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

def phone_mnemonics(phone_num):
	def phone_mnemonics_helper(idx):
		if idx == len(phone_num):
			mnemonics.append(''.join(partial_mnemonic))
		else:
			for char in mapping[int(phone_num[idx])]:
				partial_mnemonic[idx] = char
				phone_mnemonics_helper(idx+1)

	mnemonics = []
	partial_mnemonic = ['0'] * len(phone_num)
	phone_mnemonics_helper(0)
	return mnemonics



if __name__ == '__main__':
	phone_num = '2275'
	print(phone_mnemonics(phone_num))
